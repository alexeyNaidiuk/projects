import unittest

import requests

from module.config import SERV_HOST
from module.pools import TargetServerPool, ProxyServerPool


class TestTargetPools(unittest.TestCase):

    def test_server_status(self):
        response = requests.get(f'http://{SERV_HOST}/', timeout=5).content.decode()
        self.assertIn('ok', response)

    def test_target_pool(self):
        pools = {'turkey', 'alotof', 'dbru', 'mixru', 'rub36'}

        for pool in pools:
            target_pool = TargetServerPool(pool)

            target = target_pool.pop()
            self.assertTrue('@' or '.' in target)

    def test_proxy_pool(self):
        pools = ['wwmix', 'west', 'checked', 'vlad']

        for pool in pools:
            proxy_pool = ProxyServerPool(pool)
            proxy_pool.get_pool()
            proxy = proxy_pool.pop()
            self.assertTrue('http' or 'socks' in proxy)
