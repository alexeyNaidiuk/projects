import random
from module.data import ProjectController
import unittest


class TestProjectController(unittest.TestCase):

    def test_attributes(self):
        prom_link = 'shortin.us/kCLjH'
        project_name = 'test'
        project = ProjectController(project_name=project_name, prom_link=prom_link)
        self.assertEqual(project.project_name, project_name)
        self.assertEqual(project.prom_link, prom_link)

    def test_statusIsTrue(self):
        prom_link = 'shortin.us/kCLjH'
        project_name = 'test'
        project = ProjectController(project_name=project_name, prom_link=prom_link)
        status = project.status()

        self.assertTrue(status)

    def test_statusIsFalse(self):
        prom_link = 'shortin.us/kCLjH'
        project_name = ''
        project = ProjectController(project_name=project_name, prom_link=prom_link)
        status = project.status()

        self.assertFalse(status)

    def test_statusInLoop(self):
        prom_link = 'shortin.us/kCLjH'
        project_name = 'test'
        project = ProjectController(project_name=project_name, prom_link=prom_link)
        results = []
        for _ in range(10):
            status = project.status()
            results.append(status)
            choice = random.choice([True, False])
            if choice:
                project.send_good_status()
                project.send_count(1)
            else:
                project.send_bad_status()

        self.assertNotIn(False, results)

    def test_sendGoodStatus(self):
        prom_link = 'shortin.us/kCLjH'
        project_name = 'test'
        project = ProjectController(project_name=project_name, prom_link=prom_link)

        self.assertEqual(200, project.send_good_status())
        self.assertEqual(200, project.send_bad_status())
        self.assertEqual(200, project.send_count(1))
