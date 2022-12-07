import abc
import logging
from threading import Thread
from time import sleep
from typing import NoReturn

import requests

import module

SLEEP_TIMER = 60


def get_logger(*args, **kwargs):
    info = ' '.join(args)
    project_name = kwargs['project_name']
    logger = logging.getLogger(project_name)
    logging.basicConfig(format=f'%(name)s {info} %(asctime)s: %(message)s')
    logger.setLevel(logging.INFO)
    return logger


class Spam:  # todo tests

    __slots__ = ['success_message', 'project_controller', 'text', 'target_pool', 'proxy_pool', 'logger']

    def __init__(self,
                 project_name,
                 success_message,
                 target_pool_name='mixru',
                 proxy_pool_name='vlad',
                 lang='ru',
                 referal_project_name: str = 'luckybird',
                 promo_link: str | None = None):
        self.success_message: str = success_message

        project_name = project_name + target_pool_name + referal_project_name
        self.project_controller = module.ProjectServerControllerCached(project_name=project_name)
        if not promo_link:
            promo_link = module.LinkShortner.get_link(target_pool_name, referal_project_name)
        self.project_controller.prom_link = promo_link
        self.project_controller.get_status()

        self.text: module.Text = module.Text(lang=lang, link=promo_link, project=referal_project_name)
        self.target_pool: module.ServerPool = module.TargetServerPool(pool_name=target_pool_name)
        self.proxy_pool: module.ServerPool = module.ProxyServerPool(pool_name=proxy_pool_name)

        self.logger = get_logger(
            self.project_controller.prom_link, proxy_pool_name, target_pool_name, referal_project_name, lang,
            project_name=self.project_controller.project_name
        )
        self.logger.info('Spam initialized')

    @abc.abstractmethod
    def post(self, target: str) -> requests.Response:
        ...

    def get_text(self, with_stickers: bool = True):
        text = self.text.get_text(with_stickers=with_stickers)
        return text

    def get_proxies(self):
        proxy = self.proxy_pool.pop()
        proxies = {'http': proxy, 'https': proxy}
        return proxies

    def get_target(self):
        target = self.target_pool.pop()
        return target

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
        result = self.success_message in content
        self.logger.info(f'{result} {target}')
        return result

    def get_controller_status(self) -> bool:
        controller_status = self.project_controller.get_status()
        return controller_status

    def send_results(self, result):
        if result:
            self.project_controller.send_count(1)
            return True
        else:
            self.project_controller.send_count(0)
            return False

    def main(self) -> bool:
        get_controller_status = self.get_controller_status()
        if not get_controller_status:
            self.logger.info(f'controller status is %s' % get_controller_status)
            sleep(SLEEP_TIMER)
            return False
        target = self.get_target()
        result = self.send_post(target)
        self.send_results(result)
        return result

    def infinite_main(self):
        result = True
        while result is True:
            self.main()

    def run_concurrently(self, threads_amount: int = 100) -> NoReturn:
        threads = []
        for _ in range(threads_amount):
            t = Thread(target=self.infinite_main)
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()
