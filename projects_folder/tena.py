from typing import Optional

import requests
from bs4 import BeautifulSoup

from module.data import get_proxies, try_to, generate_proxy, main

proxies = get_proxies(r'proxies_folder/west_proxy.txt')
proxy_generator = generate_proxy(proxies)
text_body = '''Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf'''


@try_to
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


@try_to
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
        'FirstName': '>>>',
        'LastName': '>>>',
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


def spam(target: str):
    result = None
    while result is None:
        proxy = next(proxy_generator)
        get_result = get(proxy)
        if get_result:
            request_token = find_request_token(get_result.text)
            result = post(request_token, target, proxy)
    return result, target


if __name__ == '__main__':
    test_result = spam('softumwork@gmail.com')
    print(test_result)
    main(spam, targets_file_path=r'targets/all_turk.csv')
