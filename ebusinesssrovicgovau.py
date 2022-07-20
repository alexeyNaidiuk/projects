import concurrent
import json
import logging
from concurrent.futures import ThreadPoolExecutor

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

from data import get_targets, get_proxies, RuCaptchaSolver, text_body, generate_proxy

url = 'https://www.e-business.sro.vic.gov.au/contactus/contact'
sitekey = '6LeI2SYUAAAAAJc85fplLQOvbFL6RQ880oF364DR'
captcha_solver = RuCaptchaSolver('1b755845270ee8614f617701ef345132')
print(captcha_solver.balance())

all_proxies = get_proxies(r'C:\Users\Admin\Desktop\projects\west_proxy.txt')
proxy_generator = generate_proxy(all_proxies)


def post(email, captcha_token, proxy: str = None):
    url = 'https://www.e-business.sro.vic.gov.au/contactusservice/submit/contact/489'

    json_data = {
        'firstName': '---',
        'lastName': '---',
        'sroCustomerNumber': '',
        'email': email,
        'countryCode': 'Australia +61',
        'phoneNumber': '38099999999',
        'subject': text_body,
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


def try_to_post(result, proxy, target, captcha_token):
    try:
        result = post(email=target, proxy=proxy, captcha_token=captcha_token)
    except Exception as e:
        logging.exception(e)
    finally:
        return result


def spam(target: str):
    result = None
    if not target:
        return result, target
    answer = captcha_solver.recaptcha(sitekey=sitekey, url=url)
    while result is None:
        proxy = next(proxy_generator)
        result = try_to_post(target=target, result=result, captcha_token=answer, proxy=proxy)
    return result, target


def main():
    targets = get_targets(r'C:\Users\Admin\Desktop\projects\all_turk.csv')
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
