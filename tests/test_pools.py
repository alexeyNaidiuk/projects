import unittest

from module.pools import TurkeyTargetServerPool, ServerPool, RussianDbruTargetServerPool, RussianTargetServerPool, \
    WestProxyServerPool, WwmixProxyServerPool


class TestTargetPools(unittest.TestCase):

    def test_turkey_pool(self):
        target_pool: ServerPool = TurkeyTargetServerPool()
        target = target_pool.pop()
        self.assertTrue('@' in target)

    def test_russian_pool(self):
        target_pool: ServerPool = RussianTargetServerPool()
        target = target_pool.pop()
        self.assertTrue('@' in target)

    def test_dbru_pool(self):
        target_pool: ServerPool = RussianDbruTargetServerPool()
        target = target_pool.pop()
        self.assertTrue('@' in target)


class TestTProxiesPools(unittest.TestCase):

    def test_wwmix_pool(self):
        proxies: ServerPool = WestProxyServerPool()
        self.assertTrue(len(proxies.pool) is not 0)

    def test_west_pool(self):
        proxies: ServerPool = WwmixProxyServerPool()
        self.assertTrue(len(proxies.pool) is not 0)

    def test_checked_pool(self):
        proxies: ServerPool = WwmixProxyServerPool()
        self.assertTrue(len(proxies.pool) is not 0)


class TestTargetFactory(unittest.TestCase):
    ...


class TestProxyFactory(unittest.TestCase):
    ...
