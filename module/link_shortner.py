import requests

from module.config import SERV_HOST


class Shortner:

    @classmethod
    def get_link(cls, target_pool_name: str, referal_to_project: str) -> str:
        ...


class LinkShortner(Shortner):

    @classmethod
    def get_link(cls, target_pool_name: str, referal_to_project: str) -> str:
        link = requests.get(
            f'http://{SERV_HOST}/link',
            params={'targets_base': target_pool_name, 'project_name': referal_to_project}
        ).text
        return link
