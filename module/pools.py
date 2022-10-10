import abc
import os
from typing import NoReturn

import requests
from dotenv import load_dotenv

load_dotenv()

TARGETS_FOLDER = os.environ['TARGETS_FOLDER']
PROXIES_FOLDER = os.environ['PROXIES_FOLDER']
SERV_HOST = os.environ.get('SERV_HOST')


class Pool:
    pool: list = []

    def pop(self) -> str:
        ...

    def append(self, value) -> None:
        ...

    def clear(self) -> None:
        ...

    def get_pool(self) -> None:
        ...

    def __len__(self) -> int:
        ...


class FilePool(Pool):
    path = None

    def __init__(self) -> NoReturn:
        self.get_pool()

    def get_pool(self) -> NoReturn:
        with open(self.path) as file:
            self.pool = file.read().split('\n')

    def pop(self) -> str:
        if len(self.pool) == 0:
            self.get_pool()
        value = self.pool.pop()
        return value

    def __len__(self):
        return len(self.pool)


class ServerPool(Pool):
    _host = SERV_HOST
    _url = f'http://{_host}'


class TurkeyTargetFilePool(FilePool):
    path = f'{TARGETS_FOLDER}/all_turk.csv'


class WwmixProxyFilePool(FilePool):
    path = f'{PROXIES_FOLDER}/wwmix.txt'


class TurkeyTargetServerPool(ServerPool):
    __database = 'turkey'

    def pop(self):
        return requests.get(f'{self._url}/targets/{self.__database}/random').content.decode('latin-1')

    def append(self, value) -> None:
        ...


class WwmixProxyServerPool(ServerPool):  # todo implement server endpoint for this
    __database = 'wwmix'

    def __init__(self):
        self.get_pool()

    def get_pool(self) -> None:
        response = requests.get(f'{self._url}/proxies/{self.__database}/pool')
        content = response.content.decode()  # text lines
        self.pool = content.split('\n')


class Factory:
    pools = {}

    @classmethod
    def get_pool(cls, factory_name) -> Pool:
        return cls.pools[factory_name]()


class ProxyFileFactory(Factory):
    pools = {
        'wwmix': WwmixProxyFilePool
    }


class TargetServerFactory(Factory):
    pools = {
        'turkey': TurkeyTargetServerPool
    }
