import os
import random
import unittest
from concurrent.futures import ThreadPoolExecutor

import requests

from module import WwmixProxyFilePool, PROXIES_FOLDER


class TestWwmixProxyPool(unittest.TestCase):

    def test_proxyfile_is_in_folder(self):
        file_name = 'wwmix.txt'
        files = os.listdir(PROXIES_FOLDER)
        self.assertTrue(file_name, files)

    def test_pool_is_not_empty(self):
        pool = WwmixProxyFilePool()

        self.assertTrue(len(pool) != 0)

    def test_pool_updates(self):
        pool = WwmixProxyFilePool()
        for _ in range(12000):
            pool.pop()
        self.assertNotEqual(len(pool), 0)

    def test_gets_random_proxy(self):
        with open(f'{PROXIES_FOLDER}/wwmix.txt') as f:
            self.proxies_from_file = f.read().split('\n')
        proxy_pool = WwmixProxyFilePool()
        proxy = proxy_pool.pop()
        self.assertTrue(proxy in self.proxies_from_file)

        result = []
        for _ in range(1500):
            proxy = proxy_pool.pop()
            result.append(proxy)
        self.assertTrue(len(result) == len(set(result)))


class TestWwmixProxies(unittest.TestCase):

    def test_at_least_10_percent_of_proxy_is_working(self):
        must_to_work_percents = 10
        pool = WwmixProxyFilePool()
        working_proxies = []

        def _check_proxy(proxy):
            try:
                res = requests.get('https://api.ipify.org/', proxies={'http': proxy, 'https': proxy})
                if res.ok:
                    working_proxies.append(proxy)
            except Exception:
                pass

        amount = 200
        random_start = random.randint(0, len(pool) - amount)
        proxies_slice = pool.pool[random_start:random_start + amount]

        with ThreadPoolExecutor() as worker:
            worker.map(_check_proxy, proxies_slice)

        working_proxies_amount = len(working_proxies)
        print(f'{amount} / {working_proxies_amount}')
        total_result = working_proxies_amount > amount / must_to_work_percents
        self.assertTrue(total_result, working_proxies_amount)
