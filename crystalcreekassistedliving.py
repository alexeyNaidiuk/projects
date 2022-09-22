import logging
from concurrent.futures import ThreadPoolExecutor

import requests

from module.data import get_turk_spinned_text, TurkeyTargetPool, WwmixProxyPool, ProjectController

PROM_LINK = 'shortin.us/JI0hK'
PROJECT_NAME = 'crystalcreekassistedlivingpy'
target_pool = TurkeyTargetPool()
PROXY_POOL = WwmixProxyPool()
project = ProjectController(PROJECT_NAME, PROM_LINK)


def post(target, text, proxy):
    cookies = {
        '_gid': 'GA1.2.1938891353.1663239892',
        '_ga': 'GA1.2.1900052821.1663239864',
        '_gat': '1',
        '_ga_LT25E62HKT': 'GS1.1.1663239864.1.1.1663240027.0.0.0',
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryzNHQht0TtSK8pN5R',
        'Origin': 'https://crystalcreekassistedliving.com',
        'Referer': 'https://crystalcreekassistedliving.com/send-a-greeting/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    data = f'------WebKitFormBoundaryzNHQht0TtSK8pN5R\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n818\r\n------WebKitFormBoundaryzNHQht0TtSK8pN5R\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n816\r\n------WebKitFormBoundaryzNHQht0TtSK8pN5R\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n1\r\n------WebKitFormBoundaryzNHQht0TtSK8pN5R\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundaryzNHQht0TtSK8pN5R\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundaryzNHQht0TtSK8pN5R\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\n{text}\r\n------WebKitFormBoundaryzNHQht0TtSK8pN5R\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\n{target}\r\n------WebKitFormBoundaryzNHQht0TtSK8pN5R\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\n{target}\r\n------WebKitFormBoundaryzNHQht0TtSK8pN5R\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\n{text}\r\n------WebKitFormBoundaryzNHQht0TtSK8pN5R\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundaryzNHQht0TtSK8pN5R--\r\n'
    return requests.post(
        'https://crystalcreekassistedliving.com/send-a-greeting/',
        cookies=cookies, headers=headers, data=data, proxies=proxy
    )


def spam(text, target):
    response = None
    while not response:
        proxy = next(PROXY_POOL)
        proxy = {'http': proxy, 'https': proxy}
        try:
            response = post(text=text, target=target, proxy=proxy)
        except Exception as e:
            logging.error(e)
    return 'successfully' in response.content.decode()


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
    with ThreadPoolExecutor(50) as executor:
        executor.map(main, [target for target in target_pool])


if __name__ == '__main__':
    main()
