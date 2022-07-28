import logging
from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor

import requests
from requests.exceptions import ConnectTimeout, ProxyError, ReadTimeout
from requests_toolbelt import MultipartEncoder

from module.data import get_proxies, generate_proxy, get_targets, RuCaptchaSolver

targets: set = get_targets(r'C:\Users\Admin\Desktop\projects\all_turk.csv')
all_proxies: list = get_proxies()
proxy_generator = generate_proxy(all_proxies)
text_body = '''🔥 Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf'''
SITE_KEY = '6Ld4ySATAAAAAGIZBqPB5Gjxr6ejsPi67tvc0QX4'
PAGE_URL = 'https://www.versace.com/us/en-us/contact-us/'
API_KEY = '4bb3691437b264f494c6669381a643e9'
solver = RuCaptchaSolver(API_KEY)
print(solver.balance)

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)


def get(proxy: str):
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
        "Referer": "https://www.google.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    return requests.get(PAGE_URL, headers=headers, proxies={'http': proxy, 'https': proxy}, timeout=10)


def post(target: str, proxy: str, captcha_response):
    body = MultipartEncoder(
        fields={
            'dwfrm_contactus_myquestion': (None, None, None),
            'dwfrm_contactus_firstname': (None, '----', None),
            'dwfrm_contactus_lastname': (None, '----', None),
            'dwfrm_contactus_email': (None, target, None),
            'dwfrm_contactus_phone': (None, None, None),
            'dwfrm_contactus_ordernumber': (None, None, None),
            'dwfrm_contactus_language': (None, 'EN', None),
            'dwfrm_contactus_country': (None, 'USA', None),
            'dwfrm_contactus_comment': (None, text_body, None),
            'g-recaptcha-type': (None, 'v2', None),
            'g-recaptcha-response': (None, captcha_response, None),
            'dwfrm_contactus_send': (None, 'yes', None),
            'format': (None, 'ajax', None),
        },
    )

    headers = {
        "accept": "*/*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": body.content_type,
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest",
        "Referer": "https://www.versace.com/us/en-us/contact-us/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    post_response = requests.post("https://www.versace.com/us/en-us/contact-us/?dwcont=C1669283149",
                                  headers=headers,
                                  proxies={'http': proxy, 'https': proxy}, data=body, timeout=10)
    return post_response


def try_to_post(proxy, result, target: str, captcha_resp):
    try:
        result = post(target=target, proxy=proxy, captcha_response=captcha_resp)
    except ConnectTimeout as e:
        logger.error(e)
    except ProxyError as e:
        logger.error(e)
    except Exception as e:
        logger.exception(e)
    finally:
        return result


def try_to_get(proxy):
    result = None
    try:
        result = get(proxy)
    except ReadTimeout as error:
        logger.error(error)
    except ConnectTimeout as error:
        logger.error(error)
    except Exception as error:
        logger.exception(error)
    finally:
        return result


def spam(target):
    result = None
    captcha_resp = solver.recaptcha(SITE_KEY, PAGE_URL)
    while result is None:
        proxy = next(proxy_generator)
        result = try_to_post(proxy, result, target, captcha_resp)
    print(result)


def main():
    with ThreadPoolExecutor(max_workers=1) as worker:
        futures = []
        for target in targets:
            future = worker.submit(spam, target)
            futures.append(future)
        for future in as_completed(futures):
            future.result()


def test():
    spam('softumwork@gmail.com')


if __name__ == '__main__':
    test()
