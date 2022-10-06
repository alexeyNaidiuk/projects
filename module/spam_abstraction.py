import abc
import logging
from threading import Thread
from time import sleep

import requests

from module import FilePool, ProxyFileFactory, ProjectController, ServerPool, TargetServerFactory
from module.texts import get_turk_spinned_text


class Spam:

    def __init__(self,
                 promo_link: str,
                 project_name: str,
                 success_message: str,
                 logging_level: int = 'info',
                 proxy_pool: str = 'wwmix', target_pool: str = 'turkey',
                 with_stickers=True, text_encoding: str = 'utf-8'):
        match logging_level:
            case 'debug':
                logging_level = logging.DEBUG
            case 'info':
                logging_level = logging.INFO
        self.logger = logging.getLogger(project_name)
        logging.basicConfig(format=f'%(name)s {promo_link} %(asctime)s: %(message)s')
        self.logger.setLevel(logging_level)

        self.promo_link = promo_link
        self.project_name = project_name
        self.success_message = success_message
        self.text_with_stickers = with_stickers
        self.text_encoding = text_encoding

        self.project_controller: ProjectController = ProjectController(project_name=project_name, prom_link=promo_link)
        self.target_pool: ServerPool = TargetServerFactory().get_pool(target_pool)
        self.proxy_pool: FilePool = ProxyFileFactory().get_pool(proxy_pool)

    @abc.abstractmethod
    def post(self, text, target, proxies) -> requests.Response:
        ...

    def try_to_post(self, target, text) -> requests.Response:
        response = None
        while response is None:
            proxy = self.proxy_pool.pop()
            try:
                response = self.post(proxies={'http': proxy, 'https': proxy}, target=target, text=text)
                self.logger.debug(response)
            except Exception as e:
                self.logger.error(e)
        return response

    def send_post(self, target='softumwork@gmail.com', text: str | None = None):
        if not text:
            text = get_turk_spinned_text(link=self.promo_link, with_stickers=self.text_with_stickers,
                                         encoding=self.text_encoding)
        response = self.try_to_post(target=target, text=text)
        content = response.content.decode()
        self.logger.debug(content)
        result = self.success_message in content
        self.logger.info(f'{result} {target}')
        return result

    def main(self):
        if not self.project_controller.status():
            self.logger.info('sleeping')
            sleep(120)
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

    def run_concurrently(self, threads_amount: int = 30):
        while True:
            threads = []
            for _ in range(threads_amount):
                t = Thread(target=self.main)
                t.start()
                threads.append(t)
            for thread in threads:
                thread.join()
