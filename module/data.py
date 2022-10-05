import abc
import logging
import os
from string import Template
from threading import Thread
from time import sleep
from typing import NoReturn

import requests
from dotenv import load_dotenv
from spintax import spintax

load_dotenv()


class RetrieveFromServer:
    __host = os.environ.get('SERV_HOST')
    __url = f'http://{__host}'

    def get_target(self, data_base: str = 'turkey'):
        return requests.get(f'{self.__url}/targets/{data_base}/random').content.decode()

    def append_target(self, target: str, data_base: str = 'turkey'):
        requests.post(f'{self.__url}/targets/{data_base}/append', json={'email': target})


class ProjectController:
    __url = 'https://zennotasks.com/automation/api.php'
    __key = os.environ.get('ZENNO_KEY')

    def __init__(self, project_name, prom_link):
        self.project_name = project_name
        self.prom_link = prom_link

    def send_count(self, count) -> int:
        '''https://zennotasks.com/automation/api.php?key=softumXasHq1!&project={-Variable.project_name-}&count={-Variable.Counter0-}'''

        params = {'key': self.__key, 'project': self.project_name, 'count': count}
        response = requests.get(self.__url, params=params)
        return response.status_code

    def send_good_status(self) -> int:
        '''https://zennotasks.com/automation/api.php?key=softumXasHq1!&project={-Variable.project_name-}&status=0'''

        params = {'key': self.__key, 'status': 0, 'project': self.project_name}
        resp = requests.get(self.__url, params=params)
        return resp.status_code

    def send_bad_status(self) -> int:
        '''https://zennotasks.com/automation/api.php?key=softumXasHq1!&project={-Variable.project_name-}&status=1'''

        params = {'key': self.__key, 'status': 1, 'project': self.project_name}
        resp = requests.get(self.__url, params=params)
        return resp.status_code

    def retrieve_attached_link(self):
        '''https://zennotasks.com/automation/api.php?key=softumXasHq1!&project=80ac3afga1amc&getlink=1'''

        params = {'key': self.__key, 'getlink': '1', 'project': self.project_name}
        resp = requests.get(self.__url, params=params)
        content = resp.content.decode()
        return content

    def status(self) -> bool:
        '''https://zennotasks.com/automation/api.php?key=softumXasHq1!&project={-Variable.project_name-}&iswork=1&prom_link={-Variable.prom_link-}'''

        params = {'key': self.__key, 'iswork': '1', 'project': self.project_name, 'prom_link': self.prom_link}
        resp = requests.get(self.__url, params=params)
        cont = resp.content.decode()
        if cont == '1':
            return True
        else:
            return False


def get_turk_spinned_text(link: str | None = '', with_stickers: bool = True, encoding: str = 'utf-8') -> str:
    text = "🔥 {Get|Take|Kullan} 50 {ücretsiz dönüş|FS|freespins|ücretsiz dönüş|ücretsiz dönüş}" \
           " {Kulübe kaydolmak|Kulübe girmek|Projeye girmek|katılmak|oynamak} Slottica'yı takip " \
           "{etmek|bu} bağlantı {aşağıda |} {-|:|} 👉 $link 👈 {Acele|Acele|Acele|Gecikme}," \
           " {bonus|ödül|hediye} süresi {sınırlı|sınırlı}! 🔥"
    spinned_text = spintax.spin(text)
    template = Template(spinned_text)
    message = template.substitute(link=link)
    if not with_stickers:
        message = message.replace('🔥', '')
        message = message.replace('👉', '')
        message = message.replace('👈', '')
    message = message.encode().decode(encoding)
    return message


class Pool:
    _pool: list = []
    path = None

    def __init__(self) -> NoReturn:
        self._update_pool()

    def _update_pool(self) -> NoReturn:
        with open(self.path) as file:
            self._pool = list(set(file.read().split('\n')))

    def get_unique(self) -> str:
        if len(self._pool) == 0:
            self._update_pool()
        value = self._pool.pop()
        return value

    @property
    def pool(self):
        return self._pool

    def __len__(self):
        return len(self._pool)


class ProxyPool(Pool):
    ...


class TargetPool(Pool):
    ...


class TurkeyTargetPool(TargetPool):
    path = f'{os.environ["TARGETS_FOLDER"]}/all_turk.csv'


class WwmixProxyPool(ProxyPool):
    path = f'{os.environ["PROXIES_FOLDER"]}/wwmix.txt'


class ProxyFactory:
    pools = {
        'wwmix': WwmixProxyPool
    }

    def get_pool(self, proxy_name) -> ProxyPool:
        return self.pools[proxy_name]()


def func_concurrently(func, threads_amount: int = 30):
    while True:
        threads = []
        for _ in range(threads_amount):
            t = Thread(target=func)
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()


class Spam:
    _serv_controller = RetrieveFromServer()

    def __init__(self,
                 promo_link: str,
                 project_name: str,
                 success_message: str,
                 logging_level: int = 'info',
                 proxy_pool: str = 'wwmix',
                 with_stickers=True, text_encoding: str = 'utf-8'):
        match logging_level:
            case 'debug':
                logging_level = logging.DEBUG
            case 'info':
                logging_level = logging.INFO
        self.text_with_stickers = with_stickers
        self.text_encoding = text_encoding
        self.promo_link = promo_link
        self.project_name = project_name
        self.project_controller = ProjectController(project_name=project_name, prom_link=promo_link)
        self.project_controller.status()
        self.success_message = success_message
        self.proxy_pool: ProxyPool = ProxyFactory().get_pool(proxy_pool)
        self.logger = logging.getLogger(project_name)
        logging.basicConfig(format=f'%(name)s {promo_link} %(asctime)s: %(message)s')
        self.logger.setLevel(logging_level)

    @abc.abstractmethod
    def post(self, text, target, proxies) -> requests.Response:
        ...

    def try_to_post(self, target, text) -> requests.Response:
        response = None
        while response is None:
            proxy = self.proxy_pool.get_unique()
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
        target = self._serv_controller.get_target('turkey').encode().decode('latin-1')
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
