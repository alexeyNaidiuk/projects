import json
import logging
from abc import abstractproperty, ABC
from time import sleep
from typing import Optional
from zipfile import ZipFile

import requests

text_body = '''Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf'''
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)


def get_proxies_from_json():
    with open('working_proxies.json') as f:
        proxies = json.load(f)

    list_proxy = [''.join([proxy['type'][0] + '://', proxy['proxy']]) for proxy in proxies]
    return list_proxy


def get_proxy_file_extension(proxy: str):
    user, password, host, port = [b for a in proxy.split('@') for b in a.split(':')]
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """
    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt(%s)
            },
            bypassList: ["localhost"]
            }
        };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (host, port, user, password)
    plugin_filename = 'proxy_auth_plugin.zip'

    with ZipFile(plugin_filename, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    return plugin_filename


def get_targets(path: str = r'C:\Users\Admin\Desktop\projects\emails.txt') -> set:
    with open(path, encoding='utf-8') as f:
        return set(f.read().split('\n'))


def target_generator(path: str = r'C:\Users\Admin\Desktop\projects\emails.txt') -> str:
    for target in get_targets(path):
        yield target


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
