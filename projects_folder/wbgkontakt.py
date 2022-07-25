import logging
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import cycle
from time import sleep

import requests
from bs4 import BeautifulSoup
from requests import ConnectTimeout
from requests.exceptions import ProxyError

from projects_folder.module.data import get_proxies, get_targets, text_body

proxies = get_proxies()
targets = get_targets(r'C:\Users\Admin\Desktop\projects\ems.txt')


def get(s: requests.Session, proxy):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "cross-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "Referer": "https://www.wbg-kontakt.de/ueber-uns/kontakt",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    get_resp = s.get('https://www.wbg-kontakt.de/ueber-uns/kontakt', headers=headers,
                     proxies={'http': proxy, 'https': proxy})
    return get_resp


def post(s: requests.Session, proxy, request_token: str, captcha_token: str, captcha_answer: int, email: str):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "Referer": "https://www.wbg-kontakt.de/ueber-uns/kontakt",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    body = {'FORM_SUBMIT': 'auto_form_3',
            'REQUEST_TOKEN': request_token,
            'name': '---',
            'Telefonnummer': '380999999999',
            'E-Mail-Adresse': email,
            'wohnadresse': '---',
            'Nachricht': text_body,
            'datenschutz': ['', '1'],
            captcha_token: str(captcha_answer)}
    post_resp = s.post('https://www.wbg-kontakt.de/ueber-uns/kontakt', headers=headers, data=body,
                       allow_redirects=True, proxies={'http': proxy, 'https': proxy})
    return post_resp


def try_to_get(s: requests.Session, proxy):
    response = None
    try:
        response = get(s, proxy)
    except ConnectTimeout as error:
        logging.error(error)
    except ProxyError as error:
        logging.error(error)
        sleep(30)
    except Exception as error:
        logging.exception(error)
    finally:
        return response


def try_to_post(s: requests.Session, proxy: str, captcha_answer, captcha_token, request_token, email):
    post_resp = None
    try:
        post_resp = post(s, proxy=proxy, request_token=request_token, captcha_token=captcha_token,
                         captcha_answer=captcha_answer,
                         email=email)
    except Exception as error:
        logging.error(error)
    finally:
        return post_resp


def parse_site(get_resp):
    soup = BeautifulSoup(get_resp.text, 'lxml')
    request_token = soup.find('input', {'name': 'REQUEST_TOKEN'}).get('value')
    captcha_token = soup.find('input', {'id': 'ctrl_386'}).get('name')
    captcha_question = soup.find('span', {'class': 'prefix captcha_text'}).text
    return captcha_question, captcha_token, request_token


def try_to_spam(target: str, proxy: str):
    s = requests.Session()
    get_resp = try_to_get(s, proxy)
    if get_resp:
        captcha_question, captcha_token, request_token = parse_site(get_resp)
        captcha_answer = sum([int(num) for num in re.findall(r'\d', captcha_question)])
        post_resp = try_to_post(s, proxy, captcha_answer, captcha_token, request_token, target)
        return post_resp, target
    else:
        proxies.remove(proxy)


def spam(target: str):
    result = False
    proxies_cycle = cycle(proxies)
    while result is False:
        proxy = next(proxies_cycle)
        return try_to_spam(target, proxy)


def test_spam():
    print(spam('worksoftum@gmail.com'))


def main():
    with ThreadPoolExecutor(max_workers=10) as worker:
        futures = []
        for target in targets:
            future = worker.submit(spam, target)
            futures.append(future)
        for future in as_completed(futures):
            print(future.result())


if __name__ == '__main__':
    test_spam()
