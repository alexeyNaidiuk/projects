import abc
import logging
from threading import Thread
from time import sleep
from typing import NoReturn

import requests

from module.pools import Pool
from module.project_controller import ProjectController
from module.texts import Text

SLEEP_TIMER = 60


def get_logger(logging_level: str, project_name: str, promo_link: str, proxy_pool: str, target_pool: str, lang: str):
    match logging_level:
        case 'debug':
            logging_level = logging.DEBUG
        case 'info':
            logging_level = logging.INFO
    logger = logging.getLogger(project_name)
    logging.basicConfig(
        format=f'%(name)s {promo_link} {proxy_pool} {target_pool} {lang} %(asctime)s: %(message)s')
    logger.setLevel(logging_level)
    return logger


class Spam:  # todo tests

    def __init__(self, project_controller: ProjectController, proxy_pool: Pool, target_pool: Pool, text: Text,
                 success_message: str = '', logging_level: str = 'info'):
        self.logger = get_logger(logging_level, project_controller.project_name, project_controller.prom_link,
                                 proxy_pool.__class__.__name__, target_pool.__class__.__name__, text.lang)
        self.logger.info('Spam initialized')
        self.success_message: str = success_message
        self.project_controller = project_controller
        self.proxy_pool = proxy_pool
        self.target_pool = target_pool
        self.text = text

    @abc.abstractmethod
    def post(self, target: str) -> requests.Response:
        ...

    def get_text(self, with_stickers: bool = True):
        return self.text.get_text(promo_link=self.project_controller.prom_link, with_stickers=with_stickers)

    def get_proxies(self):
        proxy = self.proxy_pool.pop()
        proxies = {'http': proxy, 'https': proxy}
        return proxies

    def try_to_post(self, target: str) -> requests.Response:
        response = None
        while response is None:
            try:
                response = self.post(target=target)
                self.logger.debug(response)
            except Exception as e:
                self.logger.error(e)
        return response

    def send_post(self, target: str = 'softumwork@gmail.com') -> bool:
        response: requests.Response = self.try_to_post(target=target)
        content: str = response.text
        self.logger.debug(content)
        result = self.success_message in content
        self.logger.info(f'{result} {target}')
        return result

    def main(self) -> bool:
        controller_status = self.project_controller.get_status()
        if not controller_status:
            self.logger.info(f'controller status is %s' % controller_status)
            sleep(SLEEP_TIMER)
            return False
        target = self.target_pool.pop()
        result = self.send_post(target)
        if result:
            self.project_controller.send_count(1)
            return True
        else:
            self.project_controller.send_count(0)
            return False

    def infinite_main(self):
        result = True
        while result is True:
            self.main()

    def run_concurrently(self, threads_amount: int = 5) -> NoReturn:
        threads = []
        for _ in range(threads_amount):
            t = Thread(target=self.infinite_main)
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()
