import logging
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import cycle
from random import choice
from string import Template
from threading import Thread
from time import sleep
from typing import Optional, NoReturn

import requests
from spintax import spintax


class ProjectController:
    __url = 'https://zennotasks.com/automation/api.php'
    __key = 'softumXasHq1!'

    def __init__(self, project_name, prom_link):
        self.project_name = project_name
        self.prom_link = prom_link
        self.__params = {'key': self.__key, 'project': self.project_name}

    def send_count(self, count) -> int:
        '''https://zennotasks.com/automation/api.php?key=softumXasHq1!&project={-Variable.project_name-}&count={-Variable.Counter0-}'''

        response = requests.get(self.__url, params={'key': self.__key, 'project': self.project_name, 'count': count})
        return response.status_code

    def send_good_status(self) -> int:
        '''https://zennotasks.com/automation/api.php?key=softumXasHq1!&project={-Variable.project_name-}&status=0'''

        resp = requests.get(self.__url, params={'key': self.__key, 'status': 0, 'project': self.project_name})
        return resp.status_code

    def send_bad_status(self) -> int:
        '''https://zennotasks.com/automation/api.php?key=softumXasHq1!&project={-Variable.project_name-}&status=1'''

        resp = requests.get(self.__url, params={'key': self.__key, 'status': 1, 'project': self.project_name})
        return resp.status_code

    def retrieve_attached_link(self):  # todo test
        '''https://zennotasks.com/automation/api.php?key=softumXasHq1!&project=80ac3afga1amc&getlink=1'''

        resp = requests.get(self.__url,
                            params={'key': self.__key, 'getlink': '1', 'project': self.project_name}).content.decode()
        return resp

    def status(self) -> bool:
        '''https://zennotasks.com/automation/api.php?key=softumXasHq1!&project={-Variable.project_name-}&iswork=1&prom_link={-Variable.prom_link-}'''

        resp = requests.get(self.__url,
                            params={'key': self.__key, 'iswork': '1', 'project': self.project_name,
                                    'prom_link': self.prom_link})
        cont = resp.content.decode()

        if cont == '1':
            return True
        else:
            return False


def get_turk_spinned_text(link: str | None = '', with_stickers: bool = True, decoded: bool = True) -> str:
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
    if decoded:
        message = message.encode().decode('latin-1')
    return message


def get_set(path: str) -> set:
    with open(path, encoding='utf-8') as f:
        return set(f.read().split('\n'))


class Pool:
    _pool: list = []
    path = None

    def __init__(self) -> NoReturn:
        self._update_pool()

    def _update_pool(self) -> NoReturn:
        with open(self.path) as file:
            self._pool = list(set(file.read().split('\n')))

    def get_unique(self) -> str:
        if len(self) == 0:
            self._update_pool()
        value = choice(self._pool)
        self._pool.remove(value)
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
    path = r'C:\Users\Admin\Desktop\projects\all_turk.csv'


class WwmixProxyPool(ProxyPool):
    path = r'C:\Users\Admin\Desktop\projects\proxies_folder\wwmix.txt'


class WebShareProxyPool(ProxyPool):
    path = r'C:\Users\Admin\Desktop\projects\proxies_folder\webshare socks5.txt'


class DeutcheProxyPool(ProxyPool):
    path = r'C:\Users\Admin\Desktop\projects\proxies_folder\500 DEe.txt'


class Solver(ABC):
    def __init__(self, api_key: str):
        self.api_key = api_key

    @property
    @abstractmethod
    def balance(self) -> float:
        ...

    @abstractmethod
    def solve(self, *args, **kwargs) -> str:
        ...


class SpamInterface:  # todo test
    proxies: dict | None = None
    session: requests.Session | None = None

    def __init__(self, use_session: bool = False, proxy_pool: ProxyPool = None):
        if proxy_pool:
            proxy = proxy_pool.get_unique()
            self.proxies = {'http': proxy, 'https': proxy}
        if use_session:
            self.session = requests.Session()

    @abstractmethod
    def get(self, *args, **kwargs) -> requests.Response:
        ...

    @abstractmethod
    def post(self, *args, target, text) -> requests.Response:
        ...


def func_mapped_to_pool_concurrently(func, pool: Pool, threads_amount: int | None = None):  # todo test
    while True:
        threads = []
        for _ in range(threads_amount):
            t = Thread(target=func, args=(pool.get_unique(),))
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()
