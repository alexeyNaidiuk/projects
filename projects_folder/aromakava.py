from typing import Optional

import requests
from faker import Faker
from requests.models import Response

from module.data import generate_proxy, main, try_to, get_proxies

proxy_generator = generate_proxy(set(get_proxies(r'proxies_folder/west_proxy.txt')))
text_body = '''50 фриспинов за регистрацию в клубе Slottica Переходи по ссылке ниже и забирай свой бонус! https://bit.ly/3c6QoSO'''


@try_to
def post(target: str, proxy: Optional[str] = None) -> Response:
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
        'e-mail': target,
        'misto-dlya-vidkrittya-kavyarni': text_body,
        'bazhaniy-format': text_body,
        'vashe-povidomlennya': text_body
    }
    resp = requests.post('https://aromakava.ua/api/form/2', headers=headers, data=body,
                         proxies={'http': proxy, 'https': proxy},
                         verify=False, timeout=5)
    return resp


def spam(target):
    result = None
    while result is None:
        proxy = next(proxy_generator)
        result = post(target, proxy)
    return result, target


if __name__ == '__main__':
    test_result = spam('softumwork@gmail.com')
    print(test_result)
    main(spam)
