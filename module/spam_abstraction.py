import abc
import logging
from threading import Thread
from time import sleep
from typing import NoReturn

import requests
from requests.exceptions import ProxyError, ConnectTimeout, SSLError
from urllib3.exceptions import ReadTimeoutError

from module import FilePool, ProxyFileFactory, ProjectController, ServerPool, TargetServerFactory
from module.texts import get_turk_spinned_text

SLEEP_AMOUNT_IN_MINUTES = 60 * 5


class Spam:

    def __init__(self, promo_link: str, project_name: str, success_message: str,
                 logging_level: int = 'info', proxy_pool: str = 'wwmix', target_pool: str = 'turkey',
                 with_stickers=True):

        match logging_level:
            case 'debug':
                logging_level = logging.DEBUG
            case 'info':
                logging_level = logging.INFO
        self.logger = logging.getLogger(project_name)
        logging.basicConfig(format=f'%(name)s {promo_link} %(asctime)s: %(message)s')
        self.logger.setLevel(logging_level)

        self.promo_link: str = promo_link
        self.project_name: str = project_name
        self.success_message: str = success_message
        self.text_with_stickers: bool = with_stickers
        self.target_pool: ServerPool = TargetServerFactory.get_pool(factory_name=target_pool)
        self.proxy_pool: FilePool = ProxyFileFactory.get_pool(factory_name=proxy_pool)
        self.project_controller: ProjectController = ProjectController(project_name=project_name, prom_link=promo_link)
        self.project_controller.status()

    @abc.abstractmethod
    def post(self, text: str, target: str, proxies: dict) -> requests.Response:
        ...

    def try_to_post(self, target: str, text: str) -> requests.Response:
        response = None
        while response is None:
            proxy = self.proxy_pool.pop()
            proxies = {'http': proxy, 'https': proxy}
            try:
                response = self.post(proxies=proxies, target=target, text=text)
                self.logger.debug(response)
            except (ProxyError, ReadTimeoutError, SSLError, ConnectTimeout, TimeoutError) as e:
                self.logger.debug(e)
            except Exception as e:
                self.logger.exception(e)
                raise Exception
        return response

    def send_post(self, target: str = 'softumwork@gmail.com', text: str | None = None):
        if not text:
            text = get_turk_spinned_text(link=self.promo_link, with_stickers=self.text_with_stickers)
        response = self.try_to_post(target=target, text=text)
        content = response.content.decode()
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

    def run_concurrently(self, threads_amount: int = 30) -> NoReturn:
        while True:
            threads = []
            for _ in range(threads_amount):
                t = Thread(target=self.main)
                t.start()
                threads.append(t)
            for thread in threads:
                thread.join()
