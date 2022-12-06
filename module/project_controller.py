import abc
import datetime
import json
import pathlib
import tempfile
from typing import NoReturn

import requests

from module.config import ZENNO_KEY

STATUS_EXPIRATION_LIMIT_IN_SEC = 60


class ProjectController(abc.ABC):
    __slots__ = ['project_name', 'prom_link']

    def __init__(self, project_name: str = 'test', prom_link: str = 'bit.ly/3Vf3VcM'):
        self.project_name = project_name
        self.prom_link = prom_link

    @abc.abstractmethod
    def send_count(self, count) -> int:
        ...

    @abc.abstractmethod
    def get_status(self) -> bool:
        ...

    @abc.abstractmethod
    def retrieve_attached_link(self):
        ...


class ProjectServerController(ProjectController):
    __url = 'https://zennotasks.com/automation/api.php'
    __key = ZENNO_KEY
    __slots__ = ['prom_link', 'project_name']

    def send_count(self, count) -> int:
        '''https://zennotasks.com/automation/api.php?key=FOO&count=1&project=BAR'''

        params = {'key': self.__key, 'project': self.project_name, 'count': count}
        response = requests.get(self.__url, params=params)
        return response.status_code

    def retrieve_attached_link(self) -> str | None:
        '''https://zennotasks.com/automation/api.php?key=FOO&getlink=1&project=BAR'''

        params = {'key': self.__key, 'getlink': '1', 'project': self.project_name}
        resp = requests.get(self.__url, params=params)
        content = resp.content.decode()
        if 'Undefined variable' in content:
            return None
        else:
            return content

    def get_status(self) -> bool:
        '''https://zennotasks.com/automation/api.php?key=FOO&iswork=1&project=BAR&prom_link=BIT.LY/FOOBAR'''
        if not self.project_name:
            return False

        params = {'key': self.__key, 'iswork': '1', 'project': self.project_name, 'prom_link': self.prom_link}
        resp = requests.get(self.__url, params=params)
        cont = resp.content.decode()
        if cont == '1':
            return True
        else:
            return False


def _dump_json(file_path: pathlib.Path, status: dict) -> NoReturn:
    with open(file_path, 'w') as file:
        json.dump(status, file, default=str)


def _load_json(file_path: pathlib.Path) -> dict:
    with open(file_path) as file:
        result = json.load(file)
    return result


class ProjectServerControllerCached(ProjectServerController):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cached_status_file = pathlib.Path(tempfile.mktemp('.json', self.project_name))

    def get_status(self) -> bool:  # refactor testme
        if not self.project_name:
            return False

        if self.cached_status_file.exists():
            cached_status_dict: dict = _load_json(self.cached_status_file)
            timestamp = datetime.datetime.fromisoformat(cached_status_dict['timestamp'])
            status: bool = cached_status_dict['status']

            if datetime.datetime.now() > timestamp + datetime.timedelta(seconds=STATUS_EXPIRATION_LIMIT_IN_SEC):
                status: bool = super().get_status()
                _dump_json(self.cached_status_file, {'status': status, 'timestamp': datetime.datetime.now()})
        else:
            status: bool = super().get_status()
            _dump_json(self.cached_status_file, {'status': status, 'timestamp': datetime.datetime.now()})

        return status
