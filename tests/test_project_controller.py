import random
import unittest

from module.project_controller import ProjectServerController


class TestProjectServerController(unittest.TestCase):

    def test_attributes(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = 'test'
        project_name = 'fortuneclock'

        projects = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name)

        self.assertEqual(projects.name, name)
        self.assertEqual(projects.prom_link, prom_link)

    def test_statusIsTrue(self):
        prom_link = 'bit.ly/3yi2UXW'
        name = 'teststatus'
        project_name = 'fortuneclock'

        project = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name)
        status = project.get_status()

        self.assertTrue(status)

    def test_statusIsFalse(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = ''
        project_name = 'fortuneclock'

        project = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name)
        status = project.get_status()

        self.assertFalse(status)

    def test_random_status_in_loop(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = 'test'
        project_name = 'fortuneclock'
        project_name = 'fortuneclock'
        project = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name)

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

    # def test_send_bad_status(self):
    #     prom_link = 'bit.ly/3qXjAzN'
    #     project_name = 'test'
    #     project = ProjectServerController(project_name=project_name, prom_link=prom_link)
    #     results = []
    #     for _ in range(110):
    #         status = project.get_status()
    #         results.append(status)
    #         project.send_count(0)
    #     self.assertIn(False, results)

    def test_retrieve_attached_link(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = 'test'
        project_name = 'fortuneclock'
        project = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name)

        project.get_status()

        attached_link = project.retrieve_attached_link()
        self.assertEqual(attached_link, prom_link)

        name = 'awdv43'
        project_name = 'fortuneclock'
        project = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name)
        link = project.retrieve_attached_link()

        self.assertIsNone(link)


class TestProjectControllerCached(unittest.TestCase):
    def test_get_status(self):
        prom_link = 'bit.ly/3qXjAzN'
        name = 'test'
        project_name = 'fortuneclock'
        project = ProjectServerController(name=name, prom_link=prom_link, project_name=project_name)

        results = []

        for _ in range(2):
            status = project.get_status()
            results.append(status)
