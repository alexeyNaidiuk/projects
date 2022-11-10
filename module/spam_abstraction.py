import abc
import logging
from threading import Thread
from time import sleep
from typing import NoReturn

import requests

from module.pools import TargetServerFactory, ProxyServerFactory
from module.project_controller import ProjectController
from module.texts import TextFactoryServer

SLEEP_AMOUNT_IN_MINUTES = 60 * 5


def get_logger(logging_level, project_name, promo_link, proxy_pool, target_pool, text_lang):
    match logging_level:
        case 'debug':
            logging_level = logging.DEBUG
        case 'info':
            logging_level = logging.INFO
    logger = logging.getLogger(project_name)
    logging.basicConfig(
        format=f'%(name)s {promo_link} {proxy_pool} {target_pool} {text_lang} %(asctime)s: %(message)s')
    logger.setLevel(logging_level)
    return logger


class Spam:  # todo tests

    def __init__(self, promo_link: str = 'google.com', project_name: str = 'spam', success_message: str = '',
                 logging_level: str = 'info',
                 proxy_pool: str = 'checked', target_pool: str = 'alotof', text_lang: str = 'ru', with_stickers=True):
        self.logger = get_logger(logging_level, project_name, promo_link, proxy_pool, target_pool, text_lang)

        self.success_message: str = success_message
        self.target_pool = TargetServerFactory.get_pool(factory_name=target_pool)
        self.proxy_pool = ProxyServerFactory.get_pool(factory_name=proxy_pool)
        self.text = TextFactoryServer(promo_link=promo_link, with_stickers=with_stickers, text_lang=text_lang)
        self.project_controller: ProjectController = ProjectController(project_name=project_name, prom_link=promo_link)
        self.project_controller.status()

    @abc.abstractmethod
    def post(self, text: str, target: str) -> requests.Response:
        ...

    def get_text(self):  # todo
        ...

    def get_target(self):  # todo
        ...

    def get_proxies(self):
        proxy = self.proxy_pool.pop()
        proxies = {'http': proxy, 'https': proxy}
        return proxies

    def try_to_post(self, target: str, text: str) -> requests.Response:
        response = None
        while response is None:
            try:
                response = self.post(target=target, text=text)
                self.logger.debug(response)
            except Exception as e:
                self.logger.error(e)
        return response

    def send_post(self, target: str = 'softumwork@gmail.com', text: str | None = None):
        if not text:
            text = self.text.get_text()
        response: requests.Response = self.try_to_post(target=target, text=text)
        content: str = response.content.decode()
        self.logger.debug(content)
        result = self.success_message in content
        self.logger.info(f'{result} {target}')
        return result

    def main(self) -> bool:
        controller_status = self.project_controller.status()
        if not controller_status:
            self.logger.info(f'controller status is %s' % controller_status)
            sleep(SLEEP_AMOUNT_IN_MINUTES)
            return False
        target = self.target_pool.pop()
        result = self.send_post(target)
        if result:
            self.project_controller.send_good_status()
            self.project_controller.send_count(1)
            return True
        else:
            self.project_controller.send_bad_status()
            # self._serv_controller.append_target(target)
            return False

    def infinite_main(self):
        while True:
            self.main()

    def run_concurrently(self, threads_amount: int = 30) -> NoReturn:
        threads = []
        for _ in range(threads_amount):
            t = Thread(target=self.infinite_main)
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()
