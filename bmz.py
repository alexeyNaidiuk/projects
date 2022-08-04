from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.webdriver import Service
from webdriver_manager.chrome import ChromeDriverManager
from requests_toolbelt import MultipartEncoder
from multiprocessing import Process

from module.data import main, target_generator

TEXT_BODY = '🔥 Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://cutt.ly/SZnNqlC'


# TEXT_BODY = 'test'


def get_page_source_by_selenium():
    options = ChromeOptions()
    options.headless = False
    driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('https://www.bmz.de/de/service/kontakt')
    return driver


def post(csrf_token: str, cookies: dict, target="softumwork@gmail.com"):
    data = MultipartEncoder(fields={
        "values['form-51724']": TEXT_BODY,
        "values['form-51728']": TEXT_BODY,
        "values['form-51722']": target,
        "values['form-51752']": "General enquiry",
        "values['form-51720']": TEXT_BODY,
        "values['form-51726']": TEXT_BODY,
        "values['form-51736']": "agreement_accepted",
        "companyFullName": "BMZ",
        'countryFullName': "",
        "_csrf": csrf_token
    })
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "content-type": data.content_type,
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }
    url = 'https://www.bmz.de/dynamic/forms/en/services/contact-51770'
    res = requests.post(url, data, headers=headers, cookies=cookies)
    return res


def get_csfr_token(r):
    try:
        soup = BeautifulSoup(r.page_source, 'lxml')
        csrf_token = soup.find('input', {'name': '_csrf'}).get('value')
        return csrf_token
    except AttributeError:
        return None


def spam(target):
    result = None
    while result is None:
        r = get_page_source_by_selenium()
        sleep(2)
        csrf_token = get_csfr_token(r)
        if csrf_token:
            cookies = {value.get('name'): value.get('value') for value in r.get_cookies()}
            result = post(csrf_token, cookies, target=target)
    return result, target


if __name__ == '__main__':
    test_res = spam('softumwork@gmail.com')
    print(test_res)
    processes = []
    for target in target_generator(r'targets\all_turk.csv'):
        process = Process(target=spam, args=(target,))
        process.start()
        processes.append(process)
        sleep(3)
    for process in processes:
        process.join()
