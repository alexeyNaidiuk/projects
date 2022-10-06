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

    def pop(self):
        ...

    def append(self, value):
        ...

    def clear(self):
        ...

    def reload(self):
        ...

    def __len__(self):
        ...


class FilePool(Pool):
    pool: list = []
    path = None

    def __init__(self) -> NoReturn:
        self.reload()

    def reload(self) -> NoReturn:
        with open(self.path) as file:
            self.pool = file.read().split('\n')

    def pop(self) -> str:
        if len(self.pool) == 0:
            self.reload()
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


class Factory:

    @abc.abstractmethod
    def get_pool(self) -> Pool:
        ...


class ProxyFileFactory:
    pools = {
        'wwmix': WwmixProxyFilePool
    }

    def get_pool(self, factory_name) -> FilePool:
        return self.pools[factory_name]()


class TargetServerFactory:
    pools = {
        'turkey': TurkeyTargetServerPool
    }

    def get_pool(self, factory_name) -> ServerPool:
        return self.pools[factory_name]()
