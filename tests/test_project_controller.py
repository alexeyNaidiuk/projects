import random
import unittest

from module.project_controller import ProjectController, ProjectServerController


class TestProjectServerController(unittest.TestCase):

    def test_attributes(self):
        prom_link = 'bit.ly/3qXjAzN'
        project_name = 'test'
        project = ProjectServerController(project_name=project_name, prom_link=prom_link)
        self.assertEqual(project.project_name, project_name)
        self.assertEqual(project.prom_link, prom_link)

    def test_statusIsTrue(self):
        prom_link = 'bit.ly/3yi2UXW'
        project_name = 'teststatus'
        project = ProjectServerController(project_name=project_name, prom_link=prom_link)
        status = project.get_status()

        self.assertTrue(status)

    def test_statusIsFalse(self):
        prom_link = 'bit.ly/3qXjAzN'
        project_name = ''
        project = ProjectServerController(project_name=project_name, prom_link=prom_link)
        status = project.get_status()

        self.assertFalse(status)

    def test_random_status_in_loop(self):
        prom_link = 'bit.ly/3qXjAzN'
        project_name = 'test'
        project = ProjectServerController(project_name=project_name, prom_link=prom_link)
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

    def test_send_bad_status(self):
        prom_link = 'bit.ly/3qXjAzN'
        project_name = 'test'
        project = ProjectServerController(project_name=project_name, prom_link=prom_link)
        results = []
        for _ in range(110):
            status = project.get_status()
            results.append(status)
            project.send_count(0)
        project.send_count(1)
        self.assertIn(False, results)

    def test_retrieve_attached_link(self):
        prom_link = 'bit.ly/3qXjAzN'
        project_name = 'test'
        project = ProjectServerController(project_name=project_name, prom_link=prom_link)
        project.get_status()

        attached_link = project.retrieve_attached_link()
        self.assertEqual(attached_link, prom_link)
