import logging

from bs4 import BeautifulSoup
import requests
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.webdriver import Service
from webdriver_manager.chrome import ChromeDriverManager

from module.data import get_proxies, generate_proxy, get_proxy_file_extension


all_proxies = get_proxies()
driver_path = ChromeDriverManager().install()


def get_from_browser(proxy):
    proxy_file_extension = get_proxy_file_extension(proxy.replace('http://', ''))
    url = "https://caljan.com/reach-out/subscribe-to-newsletter/"
    options = ChromeOptions()
    options.headless = False
    options.add_extension(proxy_file_extension)
    driver = Chrome(service=Service(driver_path), options=options)
    driver.get(url)
    return driver.page_source


def get(proxies: dict = None):
    headers = {}
    url = 'https://caljan.com/reach-out/subscribe-to-newsletter/'
    resp = requests.get(url, headers=headers, proxies=proxies)
    return resp


def post(target: str, proxies: dict = None):
    params = {
        'CONTACT_EMAIL': target,
        'FIRSTNAME': 'requests no proxy',
        'LASTNAME': 'requests',
        'SIGNUP_SUBMIT_BUTTON': 'Join Now',
        'zc_trackCode': 'ZCFORMVIEW',
        'viewFrom': 'URL_ACTION',
        'submitType': 'optinCustomView',
        'lD': '12db3bd677bcbb',
        'zx': '13abc43d',
        'zcvers': '3.0',
        'mode': 'OptinCreateView',
        'zcld': '12db3bd677bcbb',
        'zc_formIx': '3za74deb241a328df6bb46392a2f6b66a4',
        'lf': '1658407459332',  # var
        'di': '114470921023093825871658407459333',  # var
        'responseMode': 'inline',
        'sourceURL': 'https://caljan.com/reach-out/subscribe-to-newsletter/',
        'tpIx': '3z2007fa6189e4ea7d62bdbfba920552de',  # var
        'custIx': '3zf42485822644527cacd9cbf9f7f3c612'  # var
    }
    headers = {
        "accept": "*/*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site"
    }
    url = 'https://publ.maillist-manage.com/weboptin.zc'
    resp = requests.get(url, headers=headers, params=params)
    return resp


def spam(target):
    result = None
    while result is None:
        proxy = next(generate_proxy(all_proxies))
        get_resp = try_to_get(proxy)
        soup = BeautifulSoup(get_resp.text, 'lxml')
        result = try_to_post(result, proxy, target)
        with open('page.html', 'w') as file:
            file.write(result.text)
    return result


def try_to_get(proxy):
    return get(proxies={'http': proxy, 'https': proxy})


def try_to_post(result, proxy, target):
    try:
        result = post(target, proxies={'http': proxy, 'https': proxy})
    except Exception as err:
        logging.exception(err)
    finally:
        return result


def test():
    print(spam('worksoftum@gmail.com'))


if __name__ == '__main__':
    test()
