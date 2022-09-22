import logging
from concurrent.futures import ThreadPoolExecutor

import requests

from module.data import get_turk_spinned_text, TurkeyTargetPool, WwmixProxyPool, ProjectController

PROM_LINK = 'shortin.us/nuSYN'
PROJECT_NAME = 'absoluteblack'
target_pool = TurkeyTargetPool()
PROXY_POOL = WwmixProxyPool()
project = ProjectController(PROJECT_NAME, PROM_LINK)


def post(target, proxy, text):
    cookies = {
        'fe20530fcfd42ba40391491763a4fb74': '3bd032d736ba22583e54bedda5777c4d',
        # '_gid': 'GA1.2.1445359140.1663251353',
        # '_fbp': 'fb.1.1663251353563.717900884',
        # '_gat_gtag_UA_27561537_1': '1',
        # '_ga_4JNB3JVPNR': 'GS1.1.1663251353.1.1.1663252012.49.0.0',
        # '_ga': 'GA1.2.517688975.1663251353',
    }
    headers = {
        'authority': 'absoluteblack.cc',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://absoluteblack.cc',
        'referer': 'https://absoluteblack.cc/contact.html',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    params = {
        'option': 'com_ajax',
        'module': 'pwebcontact',
        'Itemid': '616',
        'lang': 'en',
        'method': 'sendEmail',
    }
    data = {
        'mid': '212',
        'format': 'json',
        'ignoreMessages': 'true',
        'fields[name]': text,
        'fields[email]': target,
        'fields[country]': text,
        'fields[message]': text,
        'newsletter[]': '5',
        '8041629e30816007bda238c8a61344e9': '1',
        'title': 'absoluteBLACK | Contact us',
        'url': 'https://absoluteblack.cc/contact.html',
        'screen_resolution': '1920x1080',
    }
    response = requests.post(
        'https://absoluteblack.cc/index.php', params=params, proxies=proxy, cookies=cookies, headers=headers, data=data
    )
    return response


def spam(text, target):
    response = None
    while not response:
        proxy = next(PROXY_POOL)
        proxy = {'http': proxy, 'https': proxy}
        try:
            response = post(text=text, target=target, proxy=proxy)
        except Exception as e:
            logging.error(e)
    return 'Thanks' in response.content.decode()


def main(target='softumwork@gmail.com'):
    target = target.encode().decode('latin-1')
    text = get_turk_spinned_text(PROM_LINK, with_stickers=True, decoded=False)
    succ = spam(text=text, target=target)
    if succ:
        project.send_good_status()
        project.send_count(1)
    else:
        project.send_bad_status()
    print(succ, target)


def threaded_main():
    with ThreadPoolExecutor(30) as executor:
        executor.map(main, [target for target in target_pool])


if __name__ == '__main__':
    main()
