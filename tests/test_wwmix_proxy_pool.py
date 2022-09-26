import os
import random
import unittest
from concurrent.futures import ThreadPoolExecutor

import requests

from module.data import WwmixProxyPool


class TestWwmixProxyPool(unittest.TestCase):

    def test_proxyfile_is_in_folder(self):
        path_folder = r'C:\Users\Admin\Desktop\projects\proxies_folder'
        file_name = 'wwmix.txt'
        files = os.listdir(path_folder)
        self.assertTrue(file_name, files)

    def test_pool_is_not_empty(self):
        pool = WwmixProxyPool()

        self.assertTrue(len(pool) != 0)

    def test_pool_updates(self):
        pool = WwmixProxyPool()
        for _ in range(12000):
            pool.get_unique()
        self.assertNotEqual(len(pool), 0)

    def test_gets_random_proxy(self):
        with open(r'C:\Users\Admin\Desktop\projects\proxies_folder\wwmix.txt') as f:
            self.proxies_from_file = f.read().split('\n')
        proxy_pool = WwmixProxyPool()
        proxy = proxy_pool.get_unique()
        self.assertTrue(proxy in self.proxies_from_file)

        result = []
        for _ in range(1500):
            proxy = proxy_pool.get_unique()
            result.append(proxy)
        self.assertTrue(len(result) == len(set(result)))


class TestWwmixProxies(unittest.TestCase):

    def test_at_least_10_percent_of_proxy_is_working(self):
        pool = WwmixProxyPool()

        result = []

        def _check_proxy(proxy):
            try:
                res = requests.get('https://api.ipify.org/', proxies={'http': proxy, 'https': proxy})
                if res.ok:
                    result.append(proxy)
            except Exception as e:
                print(e)

        amount = 100
        random_start = random.randint(0, len(pool._pool) - amount)
        proxies_slice = pool._pool[random_start:random_start + 500]

        with ThreadPoolExecutor(amount) as worker:
            worker.map(_check_proxy, proxies_slice)

        working_proxies_amount = len(result)
        total_result = working_proxies_amount > amount / 10
        self.assertTrue(total_result, working_proxies_amount)
