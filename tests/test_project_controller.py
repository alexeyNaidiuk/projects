import datetime
import logging
import random
import string
import unittest

from module.project_controller import ProjectServerController, ProjectServerControllerCached


def generate_string():
    letters_ = [random.choice(string.ascii_letters + string.digits) for _ in range(15)]
    return ''.join(letters_)


class TestProjectServerController(unittest.TestCase):

    def test_attributes(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = 'test'
        project_name = 'fortuneclock'
        target_database = 'mixru'

        projects = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name,
                                           targets_base=target_database)
        self.assertEqual(projects.name, name)
        self.assertEqual(projects.prom_link, prom_link)

    def test_statusIsTrue(self):
        prom_link = 'bit.ly/3yi2UXW'
        name = 'teststatus'
        project_name = 'fortuneclock'
        target_database = 'mixru'
        project = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name,
                                          targets_base=target_database)
        status = project.get_status()
        self.assertTrue(status)

    def test_statusIsFalse(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = ''
        project_name = 'fortuneclock'
        target_database = 'mixru'
        project = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name,
                                          targets_base=target_database)
        status = project.get_status()
        self.assertFalse(status)

    def test_random_status_in_loop(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = 'test'
        project_name = 'fortuneclock'
        target_database = 'mixru'
        project = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name,
                                          targets_base=target_database)
        results = []
        for _ in range(10):
            status = project.get_status()
            results.append(status)
            choice = random.choice([True, False])
            if choice:
                project.send_count(1)
            else:
                project.send_count(0)

        self.assertNotIn(False, results)

    def test_retrieve_attached_link(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = 'test'
        project_name = 'fortuneclock'
        target_database = 'mixru'
        project = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name,
                                          targets_base=target_database)

        project.get_status()

        attached_link = project.retrieve_attached_link()
        self.assertEqual(attached_link, prom_link)


class TestCachedController(unittest.TestCase):

    def test_init(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = 'test'
        project_name = 'fortuneclock'
        target_database = 'mixru'
        controller = ProjectServerControllerCached(
            name=name, prom_link=prom_link, project_name=project_name,
            targets_base=target_database
        )

        # checking that on init status is None
        status_dict = controller._load_status()
        self.assertEqual(status_dict['status'], None)

        # checking dump method
        controller._dump_status(False)
        status_dict = controller._load_status()
        self.assertEqual(status_dict['status'], False)

        # expired
        status_expired: bool = controller._check_status(str(datetime.datetime.now()))  # False
        self.assertFalse(status_expired)

        # expired
        status_expired: bool = controller._check_status('2022-12-20 12:31:27.016684')  # True
        self.assertTrue(status_expired)

        # check expired timestamp
        expired_timestamp = '2022-12-20 12:31:27.016684'
        controller._dump_status(True, expired_timestamp)
        status_dict = controller._load_status()
        controller_status_timestamp_loaded = status_dict['timestamp']
        status_expired: bool = controller._check_status(controller_status_timestamp_loaded)  # True
        self.assertTrue(status_expired)

        # check not expired timestamp
        controller._dump_status()
        status_dict = controller._load_status()
        controller_status_timestamp_loaded = status_dict['timestamp']
        status_expired: bool = controller._check_status(controller_status_timestamp_loaded)  # False
        self.assertFalse(status_expired)

    def test_status(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = 'test'
        project_name = 'fortuneclock'
        target_database = 'mixru'
        controller = ProjectServerControllerCached(
            name=name, prom_link=prom_link, project_name=project_name,
            targets_base=target_database
        )
        # takes status from cache
        controller._dump_status(True)
        status = controller.get_status()
        logging.info(status)

        # retrieves status form server
        expired_timestamp = '2022-12-20 12:31:27.016684'
        controller._dump_status(True, expired_timestamp)
        status = controller.get_status()
        logging.info(status)
