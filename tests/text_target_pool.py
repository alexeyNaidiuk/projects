import os
import unittest

from module.data import TurkeyTargetPool


class TestFiles(unittest.TestCase):

    def test_file_is_in_folder(self):
        path_folder = r'C:\Users\Admin\Desktop\projects'
        file_name = 'all_turk.csv'
        files = os.listdir(path_folder)
        self.assertTrue(file_name, files)


class TestTurkeyTargetPool(unittest.TestCase):
    def setUp(self) -> None:
        self.pool = TurkeyTargetPool()

    def test_pool_is_not_empty(self):
        self.assertTrue(len(self.pool) != 0)

    def test_pool_updates(self):
        for _ in range(1000):
            self.pool.get_unique()

        self.assertNotEqual(len(self.pool), 0)

    def test_gets_random(self):
        with open(r'C:\Users\Admin\Desktop\projects\all_turk.csv') as f:
            self.targets_from_file = f.read().split('\n')
        target_pool = TurkeyTargetPool()
        target = self.pool.get_unique()
        self.assertTrue(target in self.targets_from_file)

        result = []
        for _ in range(1500):
            target = target_pool.get_unique()
            result.append(target)
        self.assertTrue(len(result) == len(set(result)))
