import logging
from time import sleep

import requests

import module.data as md

PROMO_LINK = 'bit.ly/3UuZhHB'

proxy_pool = md.WwmixProxyPool()
target_pool = md.TurkeyTargetPool()

project_controller = md.ProjectController('wufoo', PROMO_LINK)


def get(s, proxy):
    headers = {
        'authority': 'www.xpressbees.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    response = s.get('https://www.xpressbees.com/contact-us/', headers=headers,
                     proxies={'http': proxy, 'https': proxy})
    return response


def post(s, proxy, target):
    text = f"🔥 Get 50 FreeSpins {PROMO_LINK} 🔥".encode().decode('latin-1')
    data = f'------WebKitFormBoundaryGFS0PG6vpRfUlUfz\r\nContent-Disposition: form-data; name="csrf_test_name"\r\n\r\n{s.cookies.get("csrf_cookie_name")}\r\n------WebKitFormBoundaryGFS0PG6vpRfUlUfz\r\nContent-Disposition: form-data; name="feedtype"\r\n\r\nservice\r\n------WebKitFormBoundaryGFS0PG6vpRfUlUfz\r\nContent-Disposition: form-data; name="feedname"\r\n\r\n{text}\r\n------WebKitFormBoundaryGFS0PG6vpRfUlUfz\r\nContent-Disposition: form-data; name="feedmobile"\r\n\r\n1212121212\r\n------WebKitFormBoundaryGFS0PG6vpRfUlUfz\r\nContent-Disposition: form-data; name="feedemail"\r\n\r\n{target}\r\n------WebKitFormBoundaryGFS0PG6vpRfUlUfz\r\nContent-Disposition: form-data; name="feedawb"\r\n\r\n123112123\r\n------WebKitFormBoundaryGFS0PG6vpRfUlUfz\r\nContent-Disposition: form-data; name="feedarea"\r\n\r\ntestreq\r\n------WebKitFormBoundaryGFS0PG6vpRfUlUfz\r\nContent-Disposition: form-data; name="feedsubmitpolicy"\r\n\r\n\r\n------WebKitFormBoundaryGFS0PG6vpRfUlUfz\r\nContent-Disposition: form-data; name="feedsubmit"\r\n\r\nSubmit\r\n------WebKitFormBoundaryGFS0PG6vpRfUlUfz--\r\n'
    kwargs = {'url': 'https://www.xpressbees.com/feedback', 'headers': {'content-length': '1009',
                                                                        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                                                                        'accept': 'application/json, text/javascript, */*; q=0.01',
                                                                        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryGFS0PG6vpRfUlUfz',
                                                                        'x-requested-with': 'XMLHttpRequest',
                                                                        'sec-ch-ua-mobile': '?0',
                                                                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                                                                        'sec-ch-ua-platform': '"Windows"',
                                                                        'origin': 'https://www.xpressbees.com',
                                                                        'sec-fetch-site': 'same-origin',
                                                                        'sec-fetch-mode': 'cors',
                                                                        'sec-fetch-dest': 'empty',
                                                                        'referer': 'https://www.xpressbees.com/contact-us/',
                                                                        'accept-encoding': 'gzip, deflate, br',
                                                                        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'},
              'data': data}
    resp = s.post(**kwargs, proxies={'http': proxy, 'https': proxy})
    return resp


def try_to_post(target):
    content = None
    while not content:
        proxy = proxy_pool.get_unique()
        s = requests.Session()
        try:
            get(s, proxy)
            rep = post(s, proxy=proxy, target=target)
            content = rep.content.decode()
        except Exception as e:
            logging.error(e)
    return content


def spam(target='softumwork1@gmail.com'):
    if not project_controller.status():
        sleep(120)
        print('sleeping')
        return False
    content = try_to_post(target=target.encode().decode('latin-1'))
    result = 'Success' in content
    print(result, target)
    if result:
        project_controller.send_good_status()
        project_controller.send_count(1)
    else:
        project_controller.send_bad_status()


if __name__ == '__main__':
    spam()
    md.func_mapped_to_pool_concurrently(spam, target_pool, 50)
