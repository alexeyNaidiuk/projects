import os

import unittest

from dotenv import load_dotenv

from module.data import TurkeyTargetPool

TARGETS_FOLDER = os.environ['TARGETS_FOLDER']
load_dotenv()


class TestFiles(unittest.TestCase):

    def test_file_is_in_folder(self):
        file_name = 'all_turk.csv'
        files = os.listdir(TARGETS_FOLDER)
        self.assertIn(file_name, files)


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
        with open(f'{TARGETS_FOLDER}/all_turk.csv') as f:
            self.targets_from_file = f.read().split('\n')
        target_pool = TurkeyTargetPool()
        target = self.pool.get_unique()
        self.assertTrue(target in self.targets_from_file)

        result = []
        for _ in range(1500):
            target = target_pool.get_unique()
            result.append(target)
        self.assertTrue(len(result) == len(set(result)))
