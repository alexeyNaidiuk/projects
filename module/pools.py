import requests

from module.config import *


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


class ServerPool(Pool):
    _url = f'http://{SERV_HOST}'

    def __len__(self):
        return len(self.pool)

    def pop(self) -> str:
        return self.pool.pop()


class TurkeyTargetServerPool(ServerPool):
    __database = 'turkey'

    def pop(self):
        return requests.get(f'{self._url}/targets/{self.__database}/random').content.decode('latin-1')


class RussianTargetServerPool(ServerPool):
    __database = 'alotof'

    def pop(self):
        return requests.get(f'{self._url}/targets/{self.__database}/random').content.decode('latin-1')


class RussianDbruTargetServerPool(ServerPool):
    __database = 'dbru'

    def pop(self):
        return requests.get(f'{self._url}/targets/{self.__database}/random').content.decode('latin-1')


class WwmixProxyServerPool(ServerPool):
    __database = 'wwmix'

    def __init__(self):
        self.get_pool()

    def get_pool(self) -> None:
        response = requests.get(f'{self._url}/proxies/{self.__database}')
        content = response.content.decode()
        self.pool = content.split('\n')


class WestProxyServerPool(ServerPool):
    __database = 'west'

    def __init__(self):
        self.get_pool()

    def get_pool(self) -> None:
        response = requests.get(f'{self._url}/proxies/{self.__database}')
        content = response.content.decode()
        self.pool = content.split('\n')


class CheckedProxyServerPool(ServerPool):
    __database = 'checked'

    def __init__(self):
        self.get_pool()

    def get_pool(self) -> None:
        response = requests.get(f'{self._url}/proxies/{self.__database}')
        content = response.content.decode()
        self.pool = content.split('\n')


class Factory:
    pools = {}

    @classmethod
    def get_pool(cls, factory_name) -> Pool:
        return cls.pools[factory_name]()


class ProxyServerFactory(Factory):
    pools = {
        'wwmix': WwmixProxyServerPool,
        'west': WestProxyServerPool,
        'checked': CheckedProxyServerPool
    }


class TargetServerFactory(Factory):
    pools = {
        'turkey': TurkeyTargetServerPool,
        'alotof': RussianTargetServerPool,
        'dbru': RussianDbruTargetServerPool,
    }
