import unittest

from module.pools import TargetServerPool, ProxyServerPool


class TestTargetPools(unittest.TestCase):

    def test_target_pool(self):
        pools = ('turkey', 'alotof', 'dbru', 'mixru', 'rub36', 'dadru')

        for pool in pools:
            target_pool = TargetServerPool(pool)

            target = target_pool.pop()
            print(target, pool)
            self.assertTrue('@' in target or '.' in target)

    def test_proxy_pool(self):
        pools = ('wwmix', 'west', 'parsed', 'vlad')

        for pool in pools:
            proxy_pool = ProxyServerPool(pool)
            proxy_pool.get_pool()
            proxy = proxy_pool.pop()
            self.assertTrue('http' in proxy or 'socks' in proxy)
