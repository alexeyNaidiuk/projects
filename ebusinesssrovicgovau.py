import concurrent
import json
import logging
from concurrent.futures import ThreadPoolExecutor
from random import choice
from time import sleep

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from twocaptcha import TwoCaptcha

from data import get_targets, get_proxies

text_body = '''🏆 50 фриспинов за регистрацию в клубе Slottica Переходи по ссылке ниже и забирай свой бонус! https://bit.ly/3c6QoSO'''
url = 'https://www.e-business.sro.vic.gov.au/contactus/contact'
sitekey = '6LeI2SYUAAAAAJc85fplLQOvbFL6RQ880oF364DR'
captcha_solver = TwoCaptcha('2bc08ce6750eb3ff4b9a6615529e8213', server='rucaptcha.com')
print(captcha_solver.balance())

proxies = get_proxies()


def post(email, subject, text_body, captcha_token, proxy=None):
    url = 'https://www.e-business.sro.vic.gov.au/contactusservice/submit/contact/215'

    json_data = {
        'firstName': '---',
        'lastName': '---',
        'sroCustomerNumber': '',
        'email': email,
        'countryCode': 'Australia +61',
        'phoneNumber': '38099999999',
        'subject': subject,
        'recaptchaV2Token': captcha_token,
        'category': 'Other',
        'subCategory': '',
        'message': text_body,
        'categoryId': '12',
    }

    mp_encoder = MultipartEncoder(
        fields={
            'contactDetails': ('blob', json.dumps(json_data).encode('utf-8'), 'application/json'),
        },
    )
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': mp_encoder.content_type,
        'Origin': 'https://www.e-business.sro.vic.gov.au',
        'Referer': 'https://www.e-business.sro.vic.gov.au/contactus/contact',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    proxies = {'https': proxy, 'http': proxy}
    response = requests.post(url, headers=headers, proxies=proxies, data=mp_encoder)
    return response


def spam(target: str):
    if not target:
        return None
    answer = captcha_solver.recaptcha(sitekey=sitekey, url=url)
    while True:
        proxy = choice(proxies)
        try:
            r = post(target, text_body, text_body, answer['code'], proxy=proxy)
            return r, target
        except Exception as err:
            logging.error(err)
            sleep(10)


def main():
    targets = get_targets(r'C:\Users\Admin\Desktop\projects\ems.txt')
    with ThreadPoolExecutor(max_workers=10) as worker:
        futures = []
        for target in targets:
            future = worker.submit(spam, target)
            futures.append(future)
        for future in concurrent.futures.as_completed(futures):
            print(future.result())


def test():
    r = spam('softumwork@gmail.com')
    print(r)


if __name__ == '__main__':
    test()
