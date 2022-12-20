import requests

from module.config import *


class ServerPool:
    _url = f'http://{SERV_HOST}'

    pool: list = []

    def __init__(self, pool_name: str):
        self.pool_name = pool_name

    def pop(self) -> str:
        ...

    def get_pool(self) -> None:
        ...

    def __len__(self) -> int:
        return len(self.pool)


class TargetServerPool(ServerPool):

    def pop(self) -> str:
        return requests.get(f'{self._url}/targets/{self.pool_name}/pop', timeout=10).content.decode('latin-1')


class ProxyServerPool(ServerPool):

    def __init__(self, pool_name: str):
        super().__init__(pool_name)

    def pop(self) -> str:
        if len(self) == 0:
            self.get_pool()
        value = self.pool.pop()
        return value

    def get_pool(self) -> None:
        self.pool = requests.get(f'{self._url}/proxies/{self.pool_name}/pool', timeout=10).content.decode().split('\n')
