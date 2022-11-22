import requests

from module.config import ZENNO_KEY


class ProjectController:
    __slots__ = ['project_name', 'prom_link']
    __url = 'https://zennotasks.com/automation/api.php'
    __key = ZENNO_KEY

    def __init__(self, project_name, prom_link):
        self.project_name = project_name
        self.prom_link = prom_link

    def send_count(self, count) -> int:
        '''https://zennotasks.com/automation/api.php?key=FOO&count=1&project=BAR'''

        params = {'key': self.__key, 'project': self.project_name, 'count': count}
        response = requests.get(self.__url, params=params)
        return response.status_code

    def send_good_status(self) -> int:
        '''https://zennotasks.com/automation/api.php?key=&status=0&project='''

        params = {'key': self.__key, 'status': 0, 'project': self.project_name}
        resp = requests.get(self.__url, params=params)
        return resp.status_code

    def send_bad_status(self) -> int:
        '''https://zennotasks.com/automation/api.php?key=&status=1&project='''

        params = {'key': self.__key, 'status': 1, 'project': self.project_name}
        resp = requests.get(self.__url, params=params)
        return resp.status_code

    def retrieve_attached_link(self):
        '''https://zennotasks.com/automation/api.php?key=FOO&getlink=1&project=BAR'''

        params = {'key': self.__key, 'getlink': '1', 'project': self.project_name}
        resp = requests.get(self.__url, params=params)
        content = resp.content.decode()
        return content

    def status(self) -> bool:
        '''https://zennotasks.com/automation/api.php?key=FOO&iswork=1&project=BAR&prom_link=BIT.LY/FOOBAR'''

        params = {'key': self.__key, 'iswork': '1', 'project': self.project_name, 'prom_link': self.prom_link}
        resp = requests.get(self.__url, params=params)
        cont = resp.content.decode()
        if cont == '1':
            return True
        else:
            return False
