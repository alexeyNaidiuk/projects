import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import cycle
from time import sleep
from typing import Optional

import requests
from bs4 import BeautifulSoup
from requests.adapters import ConnectTimeout, ProxyError

from projects_folder.module.data import get_targets, get_proxies

text_body = '''50 фриспинов за регистрацию в клубе Slottica Переходи по ссылке ниже и забирай свой бонус! https://bit.ly/3c6QoSO'''
proxies = get_proxies()
targets = get_targets(r'C:\Users\Admin\Desktop\projects\ems.txt')


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

    response = requests.get('https://www.tena.ua/ru/tenalady/kontakty', headers=headers,
                            proxies={'http': proxy, 'https': proxy}, timeout=5)
    return response


def post(request_token: str, body: str, name: str, surname: str, email: str, proxy: str = Optional[str]):
    cookies = {
        '.ASPXANONYMOUS': 'EHl_rgtStfTlT-KmRPDztJRrccWsT3ygBq0psSlSr63A2LLPo5AZ9cVg8NRpcmQlySUGznyL6Z_0Sbprqje6POPz-YLFeqiJbWLQyH9U6oNQwlRKy8Q4-S_0h2LDCCwt8JX41g2',
        'EPi:StateMarker': 'true',
        'MaxMindCulture': 'us',
        '__RequestVerificationToken': 'fTfjs38mXDqydEalSysAx6fGEYvCPmx5DpINeiFUCPx14pKoWvsSBqE7Ot85xStH-GRzec_LDfIGJgOi-Qdl5FPv1aA1',
    }

    headers = {
        'authority': 'profoto.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://profoto.com',
        'referer': 'https://profoto.com/ru/contact',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        '__RequestVerificationToken': 'EcOFd67FgesmvnlR3U-eS6eFA9AKMQWlzXkkUbI38w-YEyGF5B_XowVTPbe5BdUUFWAMq15JA7J3xdILQg_44jFEuWo1',
        # var
        'EmarsysTransactionId': '4263',
        'HowCanWeHelp': 'onlinepurchase',
        'Country': 'us-185',
        'FirstName': 'testFirstName',
        'LastName': 'testLastName',
        'EmailAddress': 'rabotasoftum@gmail.com',
        'MobileNumber': '+3809999999',
        'Subject': 'testSubj',
        'Message': 'testBody',
        'AgreeToTerms': [
            'true',
            'false',
        ],
        'g-recaptcha-response': '03ANYolqtTBi9_vF4PEdAJ_69p6aXmXmN-4md03-q0GhFUhWG8LEzRpa5VBUlPxWlnVBIZoD5Q3OCixAxAJokH4-nuB-DuCa8KWLUMPLGrOncCaT7we6jVxbNBO8vPQJiEn6fuIB49yi5TbRepVD_i2aCQLBlz_AykwdKxSblYsbV7j26Zl_Ob-bjQ-q9St2fnKDZEdcd9xPnVchgS0vcz9_Bzyi50_Mv2-8Ipq-DqH43xaFqki7Kpn7vBtAe9HVNs7dYdzDl8BpfD6aZSksz72a8k9pBvrIfXtfX_L4Hjr299ZBRAzmxG7xjwF8hX8kT8jFl1xrcNCci5sKVnyoolqZtEZGgvhFXnfsZqBPngzXXWG8in2AKBhNXJdPHhyN1MlkiDSJLRfs7g99WHyifhtks0OcVcaMvBU1fFOXW5s7Or6MU4rLdSTk3q9Jtqg2tVshDbDgtOfiG59tYUw0CMVA1RM0ks147AwCwlRErp1cuxTn3DQ7C-PAUuJS8NzOe9GwWuiQVOFplO',
        'RecaptchaVerificationToken': '03ANYolqtTBi9_vF4PEdAJ_69p6aXmXmN-4md03-q0GhFUhWG8LEzRpa5VBUlPxWlnVBIZoD5Q3OCixAxAJokH4-nuB-DuCa8KWLUMPLGrOncCaT7we6jVxbNBO8vPQJiEn6fuIB49yi5TbRepVD_i2aCQLBlz_AykwdKxSblYsbV7j26Zl_Ob-bjQ-q9St2fnKDZEdcd9xPnVchgS0vcz9_Bzyi50_Mv2-8Ipq-DqH43xaFqki7Kpn7vBtAe9HVNs7dYdzDl8BpfD6aZSksz72a8k9pBvrIfXtfX_L4Hjr299ZBRAzmxG7xjwF8hX8kT8jFl1xrcNCci5sKVnyoolqZtEZGgvhFXnfsZqBPngzXXWG8in2AKBhNXJdPHhyN1MlkiDSJLRfs7g99WHyifhtks0OcVcaMvBU1fFOXW5s7Or6MU4rLdSTk3q9Jtqg2tVshDbDgtOfiG59tYUw0CMVA1RM0ks147AwCwlRErp1cuxTn3DQ7C-PAUuJS8NzOe9GwWuiQVOFplO',
    }

    response = requests.post('https://profoto.com/contactformblock/SubmitContactForm', cookies=cookies, headers=headers,
                             data=data)


def find_request_token(content) -> str:
    soup = BeautifulSoup(content, 'lxml')
    request_token = soup.find('input', {'name': '__RequestVerificationToken'}).get('value')
    return request_token


def try_to_get(**kwargs):
    r = None
    try:
        r = get(**kwargs)
    except ConnectTimeout as error:
        logging.error(error)
    except ProxyError as error:
        logging.error(error)
        sleep(30)
    except Exception as error:
        logging.exception(error)
    finally:
        return r


def try_to_post(**kwargs):
    post_result = None
    try:
        post_result = post(**kwargs)
    except Exception as error:
        logging.error(error)
    finally:
        return post_result


def spam(target: str):
    result = False
    proxies_cycle = cycle(proxies)

    while result is False:
        proxy = next(proxies_cycle)
        get_response = try_to_get(proxy=proxy)
        if get_response:
            request_token = find_request_token(get_response.text)
            post_response = try_to_post(request_token=request_token,
                                        proxy=proxy,
                                        body=text_body,
                                        name='---',
                                        surname='---',
                                        email=target)
            return post_response, target
        else:
            proxies.remove(proxy)


def main():
    with ThreadPoolExecutor(max_workers=150) as worker:
        futures = []
        for target in targets:
            future = worker.submit(spam, target)
            futures.append(future)
        for future in as_completed(futures):
            print(future.result())


def test():
    for target in targets:
        print(spam(target))


if __name__ == '__main__':
    main()
