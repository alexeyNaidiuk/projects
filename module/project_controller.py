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
    __slots__ = ['name', 'prom_link', 'project_name', 'targets_base']

    def __init__(self, name: str, prom_link: str, project_name: str, targets_base: str):
        self.project_name = project_name
        self.name = name
        self.prom_link = prom_link
        self.targets_base = targets_base

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

    def send_count(self, count) -> int:

        params = {'key': self.__key, 'project': self.name, 'count': count}
        response = requests.get(self.__url, params=params)
        return response.status_code

    def retrieve_attached_link(self) -> str | None:

        params = {'key': self.__key, 'getlink': '1', 'project': self.name}
        resp = requests.get(self.__url, params=params)
        content = resp.content.decode()
        if 'Undefined variable' in content:
            return None
        else:
            return content

    def get_status(self) -> bool:
        if not self.name:
            return False
        params = {
            'key': self.__key,
            'iswork': '1',
            'project': self.name,
            'prom_link': self.prom_link,
            'project_name': self.project_name,
            'targets_base': self.targets_base
        }
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
        self.__slots__.append('cached_status_file')
        self.cached_status_file = pathlib.Path(tempfile.mktemp(suffix='.json', prefix=self.name))

    def get_status(self) -> bool:
        if not self.name:
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
