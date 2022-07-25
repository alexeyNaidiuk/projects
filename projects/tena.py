import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import cycle
from time import sleep
from typing import Optional

import requests
from bs4 import BeautifulSoup
from requests.adapters import ConnectTimeout, ProxyError

from module.data import get_targets, get_proxies

proxies = get_proxies()
targets = get_targets()
text_body = '''50 фриспинов за регистрацию в клубе Slottica Переходи по ссылке ниже и забирай свой бонус! https://bit.ly/3c6QoSO'''


def get(proxy: Optional[str] = None):
    headers = {
        'authority': 'www.tena.ua',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
    }
    return requests.get('https://www.tena.ua/ru/tenalady/kontakty', headers=headers,
                        proxies={'http': proxy, 'https': proxy}, timeout=5, verify=False)


def post(request_token: str, email: str, proxy: str = Optional[str]):
    headers = {
        'authority': 'www.tena.ua',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.tena.ua',
        'referer': 'https://www.tena.ua/ru/tenalady/kontakty',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'formId': '57016-106617',
        'formParentId': '24884-106605',
        'Message': text_body,
        'FirstName': '---',
        'LastName': '---',
        'Email': email,
        'email_check': email,
        'PhoneNumber': '380999999999',
        'Address': '---',
        'City': '---',
        'Country': 'Украина',
        'termsandcondition': 'true',
        '__RequestVerificationToken': request_token,
        'IdentificationSourceId': '27',
        'PageType': 'ContactUs',
        'LanguageCode': 'RU',
        'CountryCode': 'UA',
        'PageId': '',
        'SegmentName': 'woman_acc',
        'IsSampleOrderForm': 'False',
    }
    return requests.post('https://www.tena.ua/ru/Forms/ProcessForm', headers=headers, data=data,
                         proxies={'http': proxy, 'https': proxy})


def find_request_token(content) -> str:
    return BeautifulSoup(content, 'lxml').find('input', {'name': '__RequestVerificationToken'}).get('value')


def try_to_get(**kwargs):
    response = None
    try:
        response = get(**kwargs)
    except ConnectTimeout as error:
        logging.error(error)
        sleep(30)
    except ProxyError as error:
        logging.error(error)
    except Exception as error:
        logging.exception(error)
    finally:
        return response


def try_to_post(**kwargs):
    post_result = None
    try:
        post_result = post(**kwargs)
    except Exception as error:
        logging.error(error)
    finally:
        return post_result


def try_to_spam(target: str, proxy: str):
    get_response = try_to_get(proxy=proxy)
    if get_response:
        request_token = find_request_token(get_response.text)
        post_response = try_to_post(request_token=request_token, proxy=proxy, email=target)
        return post_response, target
    else:
        proxies.remove(proxy)


def spam(target: str):
    proxies_cycle = cycle(proxies)
    while True:
        proxy = next(proxies_cycle)
        return try_to_spam(target, proxy)


def main():
    with ThreadPoolExecutor(max_workers=75) as worker:
        futures = []
        for target in targets:
            future = worker.submit(spam, target)
            futures.append(future)
        for future in as_completed(futures):
            print(future.result())


def test():
    print(spam('softumwork@gmail.com'))


if __name__ == '__main__':
    main()
