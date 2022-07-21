from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep
from typing import Optional

import requests
from faker import Faker
from requests import ConnectTimeout
from requests.exceptions import ProxyError

from data import get_targets, get_proxies, generate_proxy, text_body, logger

all_proxies = get_proxies(r'C:\Users\Admin\Desktop\projects\west_proxy.txt')
proxy_generator = generate_proxy(all_proxies)


def post(email, proxy: Optional[dict] = None):
    headers = {
        "accept": "*/*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "Referer": "https://pointreturn.com/newsletter/",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        'user-agent': Faker().chrome()
    }
    body = {
        'action': 'alo_em_pubblic_form_check',
        'alo_em_opt_name': text_body,
        'alo_em_opt_email': email,
        'alo_em_privacy_agree': '1',
        'alo_easymail_txt_generic_error': 'Error during operation.',
        'alo_em_error_email_incorrect': 'The e-mail address is not correct',
        'alo_em_error_name_empty': 'The name field is empty',
        'alo_em_error_privacy_empty': 'The Privacy Policy field is empty',
        'alo_em_error_email_added': 'Warning: this email address has already been subscribed, but not activated. We are now sending another activation email',
        'alo_em_error_email_activated': 'Error during sending: please try again',
        'alo_em_error_on_sending': 'Error during sending: please try again',
        'alo_em_txt_ok': 'Subscription successful. You will receive an e-mail with a link. You have to click on the link to activate your subscription.',
        'alo_em_txt_subscribe': text_body,
        'alo_em_lang_code': '',
        'alo_em_form_lists': '',
        'alo_em_nonce': '46265149d2',
        'rndval': '1658321814208',
    }

    url = 'https://pointreturn.com/wp-admin/admin-ajax.php'
    resp = requests.post(url, headers=headers, data=body, proxies=proxy, timeout=5)
    return resp


def try_to_post(proxy, result, target):
    try:
        result = post(email=target, proxy=proxy)
    except ConnectTimeout as e:
        logger.error(e)
        pass
    except ProxyError as e:
        logger.error(e)
        sleep(20)
    except Exception as e:
        logger.error(e)
    return result


def spam(target: str):
    result = None
    if not target:
        return result, target
    while result is None:
        proxy = next(proxy_generator)
        proxy = {'http': proxy, 'https': proxy}
        result = post(target, proxy)
    return result, target


def main():
    with ThreadPoolExecutor(max_workers=50) as worker:
        futures = []
        for target in get_targets(r'C:\Users\Admin\Desktop\projects\all_turk.csv'):
            future = worker.submit(spam, target)
            futures.append(future)
        for future in as_completed(futures):
            print(future.result())


def test():
    print(spam('softumwork@gmail.com'))


if __name__ == '__main__':
    test()
