import logging
from concurrent.futures import ThreadPoolExecutor

import requests

from module.data import get_turk_spinned_text, TurkeyTargetPool, WwmixProxyPool, ProjectController

PROM_LINK = 'shortin.us/qhIqi'
PROJECT_NAME = 'bnaibrith'
target_pool = TurkeyTargetPool()
PROXY_POOL = WwmixProxyPool()
project = ProjectController(PROJECT_NAME, PROM_LINK)


def post(target, text, proxy):
    headers = {
        'authority': 'www.bnaibrith.ca',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarysUnqBT5yw13EWEKJ',
        'origin': 'https://www.bnaibrith.ca',
        'referer': 'https://www.bnaibrith.ca/ecards-sm4tmpnp/',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    data = '------WebKitFormBoundarysUnqBT5yw13EWEKJ\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n18459' \
           '\r\n------WebKitFormBoundarysUnqBT5yw13EWEKJ\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n18928' \
           '\r\n------WebKitFormBoundarysUnqBT5yw13EWEKJ\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0' \
           '\r\n------WebKitFormBoundarysUnqBT5yw13EWEKJ\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1' \
           '\r\n------WebKitFormBoundarysUnqBT5yw13EWEKJ\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from' \
           '\r\n------WebKitFormBoundarysUnqBT5yw13EWEKJ\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\n%(text)s' \
           '\r\n------WebKitFormBoundarysUnqBT5yw13EWEKJ\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\n%(target)s' \
           '\r\n------WebKitFormBoundarysUnqBT5yw13EWEKJ\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\n%(text)s' \
           '\r\n------WebKitFormBoundarysUnqBT5yw13EWEKJ\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\n%(target)s' \
           '\r\n------WebKitFormBoundarysUnqBT5yw13EWEKJ\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\n%(text)s' \
           '\r\n------WebKitFormBoundarysUnqBT5yw13EWEKJ\r\nContent-Disposition: form-data; name="wp_iec_schedule"\r\n\r\n' \
           '\r\n------WebKitFormBoundarysUnqBT5yw13EWEKJ\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1' \
           '\r\n------WebKitFormBoundarysUnqBT5yw13EWEKJ--\r\n' % {'target': target, 'text': text}

    response = requests.post('https://www.bnaibrith.ca/ecards-sm4tmpnp/',
                             headers=headers, data=data, allow_redirects=True, timeout=30
                             # proxies=proxy
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
    succ = 'Thank you!' in response.content.decode()
    return succ


def main(target='worksoftum@gmail.com'):
    # project_is_work = project.is_work()
    # print(project_is_work)
    # if project_is_work not in ['1', 'successful']:
    #     print('sleeping')
    #     sleep(240)
    #     return False
    target = target.encode().decode('latin-1')
    text = get_turk_spinned_text(PROM_LINK, with_stickers=True, decoded=True)
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
