import logging
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import cycle
from random import choice
from string import Template
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
        self.send_good_status()

    def send_count(self, count) -> int:
        '''https://zennotasks.com/automation/api.php?key=softumXasHq1!&project={-Variable.project_name-}&count={-Variable.Counter0-}'''

        self.__params['count'] = count
        response = requests.get(self.__url, params=self.__params)
        return response.status_code

    def send_good_status(self) -> int:
        '''https://zennotasks.com/automation/api.php?key=softumXasHq1!&project={-Variable.project_name-}&status=0'''
        self.__params['status'] = 0
        resp = requests.get(self.__url, params=self.__params)
        return resp.status_code

    def send_bad_status(self) -> int:
        '''https://zennotasks.com/automation/api.php?key=softumXasHq1!&project={-Variable.project_name-}&status=1'''

        self.__params['status'] = 1
        resp = requests.get(self.__url, params=self.__params)
        return resp.status_code

    def status(self) -> bool:  # fixme
        '''https://zennotasks.com/automation/api.php?key=softumXasHq1!&project={-Variable.project_name-}&iswork=1&prom_link={-Variable.prom_link-}'''

        self.__params['iswork'] = '1'
        self.__params['prom_link'] = self.prom_link
        resp = requests.get(self.__url, params=self.__params)
        cont = resp.content.decode()

        if cont in ['', 'successful']:
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


class RuCaptchaSolver(Solver):
    post_url = 'https://rucaptcha.com/in.php'
    get_url = 'https://rucaptcha.com/res.php'

    @property
    def balance(self):
        params = {
            'key': self.api_key,
            'action': 'getbalance'
        }
        return float(requests.get(self.get_url, params=params).content)

    def solve(self, sitekey, url, timeout=120) -> Optional[str]:
        result = None
        post_params = {
            'key': self.api_key,
            'method': 'userrecaptcha',
            'googlekey': sitekey,
            'pageurl': url,
            'json': '1'

        }
        post_response: requests.Response = requests.post(self.post_url, params=post_params)
        if not post_response.ok:
            return result
        c = 0
        while result is None or c > timeout * 2:
            c += 1
            get_params = {
                'key': self.api_key,
                'action': 'get',
                'id': post_response.json().get('request'),
                'json': '1'
            }
            get_response = requests.get(self.get_url, params=get_params)
            if get_response.json()['status']:
                result = get_response.json()['request']
            sleep(.5)
        return result


def try_to(func):
    def decorator(*args, **kwargs) -> requests.Response | None:
        result = None
        try:
            result = func(*args, **kwargs)
        except Exception as error:
            logging.error(error)
        finally:
            return result

    return decorator


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
    with ThreadPoolExecutor(threads_amount) as executor:
        executor.map(func, pool.pool)
