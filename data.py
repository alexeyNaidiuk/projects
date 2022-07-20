import logging
from abc import abstractproperty, ABC
from time import sleep
from typing import Optional

import requests

subject = '{Зарегистрируйтесь|Присоединяйтесь|Примите участие} и {получите|заберите|заполучайте} {бонус|приз|подарок}{ -|} {Your|The} 50 {FS|freespins|free spins|spins} {is|are} {ready|waiting}{!|}'
text_body = '''Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf'''
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)


def get_targets(path: str = r'C:\Users\Admin\Desktop\projects\emails.txt') -> set:
    with open(path, encoding='utf-8') as f:
        return set(f.read().split('\n'))


def get_proxies(proxies_path_to_file: str = r'C:\Users\Admin\Desktop\projects\proxies.txt') -> list:
    with open(proxies_path_to_file, encoding='utf-8') as f:
        return f.read().split('\n')


def generate_proxy(iterable: list):
    while True:
        for proxy in iterable:
            yield proxy


class Solver(ABC):
    def __init__(self, api_key: str):
        self.api_key = api_key

    @property
    def balance(self) -> int:
        ...


class RuCaptchaSolver(Solver):
    post_url = 'https://rucaptcha.com/in.php'
    get_url = 'https://rucaptcha.com/res.php'

    def balance(self):
        params = {
            'key': self.api_key,
            'action': 'getbalance'
        }
        return float(requests.get(self.get_url, params=params).content)

    def recaptcha(self, sitekey, url, timeout=120) -> Optional[str]:
        result = None
        post_params = {
            'key': self.api_key,
            'method': 'userrecaptcha',
            'googlekey': sitekey,
            'pageurl': url,
            'json': '1'

        }
        post_response: requests.Response = requests.post(self.post_url, params=post_params)
        c = 0
        if post_response.ok:
            while result is None or c > timeout*2:
                c += 1
                get_params = {
                    'key': self.api_key,
                    'action': 'get',
                    'id': post_response.json().get('request'),
                    'json': '1'
                }
                get_response = requests.get(self.get_url, params=get_params)
                if get_response.json()['status']:
                    result = get_response.json()['request']
                sleep(.5)
        return result
