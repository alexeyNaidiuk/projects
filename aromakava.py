from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor
from time import sleep
from typing import Optional

import requests
from faker import Faker
from requests.exceptions import ConnectTimeout, ProxyError
from requests.models import Response

from data import get_targets, get_proxies, generate_proxy, text_body, logger, get_proxies_from_json, target_generator

URL = 'https://aromakava.ua/api/form/2'
all_proxies = get_proxies('west_proxy.txt')
proxy_generator = generate_proxy(all_proxies)


def post(email: str, proxy: Optional[str] = None) -> Response:
    headers = {
        'user-agent': Faker().chrome(),
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.6',
        'accept-encoding': 'utf-8',
        'x-localization': 'uk',
        'sec-ch-ua': '"Google Chrome";v="101", "Chromium";v="101", ";Not A Brand";v="99"',
        'sec-ch-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'connection': 'keep-alive',
        'referer': 'https://aromakava.ua/',
    }

    body = {
        'prizvishche': text_body,
        'imya': text_body,
        'kontaktniy-telefon': text_body,
        'e-mail': email,
        'misto-dlya-vidkrittya-kavyarni': text_body,
        'bazhaniy-format': text_body,
        'vashe-povidomlennya': text_body
    }
    resp = requests.post(URL, headers=headers, data=body, proxies={'http': proxy, 'https': proxy},
                         verify=False, timeout=5)
    return resp


def try_to_post(proxy, result, target):
    try:
        result = post(email=target, proxy=proxy)
    except ProxyError:
        sleep(20)
    except Exception:
        pass
    return result


def spam(target):
    result = None
    if not target:
        return result, target
    while result is None:
        proxy = next(proxy_generator)
        result = try_to_post(proxy, result, target)
    return result, target


def main():
    with ThreadPoolExecutor(max_workers=100) as worker:
        futures = []
        for target in target_generator(r'C:\Users\Admin\Desktop\projects\all_turk.csv'):
            future = worker.submit(spam, target)
            futures.append(future)
        for future in as_completed(futures):
            print(future.result())


def test():
    print(spam('softumwork@gmail.com'))


if __name__ == '__main__':
    test()
