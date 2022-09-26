import logging
from time import sleep

import requests

import module.data as md

proxy_pool = md.WwmixProxyPool()
target_pool = md.TurkeyTargetPool()
PROMO_LINK = 'bit.ly/3dzxKnL'
project_controller = md.ProjectController('boddingtonparish', PROMO_LINK)


def post(proxy, target, text):
    data = '------WebKitFormBoundary0IKCxg647jyLZcqu\r\nContent-Disposition: form-data; name="ff_nm_councillorselect[]"\r\n\r\nBertie Allonby Briggs\r\n------WebKitFormBoundary0IKCxg647jyLZcqu\r\nContent-Disposition: form-data; name="ff_nm_bfQuickMode3859112[]"\r\n\r\ntext\r\n------WebKitFormBoundary0IKCxg647jyLZcqu\r\nContent-Disposition: form-data; name="ff_nm_bfQuickMode2338639[]"\r\n\r\n%(text)s\r\n------WebKitFormBoundary0IKCxg647jyLZcqu\r\nContent-Disposition: form-data; name="ff_nm_bfQuickMode789310[]"\r\n\r\n%(target)s\r\n------WebKitFormBoundary0IKCxg647jyLZcqu\r\nContent-Disposition: form-data; name="mailbackSender[bfQuickMode789310]"\r\n\r\ntrue\r\n------WebKitFormBoundary0IKCxg647jyLZcqu\r\nContent-Disposition: form-data; name="ff_nm_bfQuickMode1858078[]"\r\n\r\n%(text)s\r\n------WebKitFormBoundary0IKCxg647jyLZcqu\r\nContent-Disposition: form-data; name="ff_nm_emailsendcopy[]"\r\n\r\nCopy Sent\r\n------WebKitFormBoundary0IKCxg647jyLZcqu\r\nContent-Disposition: form-data; name="mailbackConnectWith[bfQuickMode789310]"\r\n\r\ntrue_emailsendcopy\r\n------WebKitFormBoundary0IKCxg647jyLZcqu\r\nContent-Disposition: form-data; name="ff_contentid"\r\n\r\n0\r\n------WebKitFormBoundary0IKCxg647jyLZcqu\r\nContent-Disposition: form-data; name="ff_applic"\r\n\r\n\r\n------WebKitFormBoundary0IKCxg647jyLZcqu\r\nContent-Disposition: form-data; name="ff_record_id"\r\n\r\n\r\n------WebKitFormBoundary0IKCxg647jyLZcqu\r\nContent-Disposition: form-data; name="ff_module_id"\r\n\r\n0\r\n------WebKitFormBoundary0IKCxg647jyLZcqu\r\nContent-Disposition: form-data; name="ff_form"\r\n\r\n15\r\n------WebKitFormBoundary0IKCxg647jyLZcqu\r\nContent-Disposition: form-data; name="ff_task"\r\n\r\nsubmit\r\n------WebKitFormBoundary0IKCxg647jyLZcqu\r\nContent-Disposition: form-data; name="option"\r\n\r\ncom_content\r\n------WebKitFormBoundary0IKCxg647jyLZcqu\r\nContent-Disposition: form-data; name="Itemid"\r\n\r\n230\r\n------WebKitFormBoundary0IKCxg647jyLZcqu\r\nContent-Disposition: form-data; name="id"\r\n\r\n93\r\n------WebKitFormBoundary0IKCxg647jyLZcqu--\r\n' % {
        'text': text, 'target': target}
    request = {'url': 'https://www.boddingtonparish.co.uk/index.php/contact-form',
               'headers': {'content-length': '1925', 'cache-control': 'max-age=0',
                           'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                           'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',
                           'upgrade-insecure-requests': '1', 'origin': 'https://www.boddingtonparish.co.uk',
                           'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary0IKCxg647jyLZcqu',
                           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                           'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1',
                           'sec-fetch-dest': 'document',
                           'referer': 'https://www.boddingtonparish.co.uk/index.php/contact-form',
                           'accept-encoding': 'gzip, deflate, br',
                           'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                           'cookie': 'b2ee7abd406e6be1b88a66b52be512d6=afc890cff58b4c9a709636eed644dea0; _ga=GA1.3.906801494.1663855399; _gid=GA1.3.1926554695.1663855399; _gat_gtag_UA_30244976_1=1'},
               'data': data}
    resp = requests.post(**request, proxies={'http': proxy, 'https': proxy}, timeout=10)
    return resp


def try_to_post(target, text):
    content = None
    while not content:
        proxy = proxy_pool.get_unique()
        try:
            rep = post(proxy=proxy, target=target, text=text)
            content = rep.content.decode()
        except Exception as e:
            logging.error(e)
    return content


def spam(target='softumwork1@gmail.com'):
    if not project_controller.status():
        sleep(120)
        print('sleeping')
        return False

    text = md.get_turk_spinned_text(link=PROMO_LINK, with_stickers=True, decoded=True)
    content = try_to_post(target=target.encode().decode('latin-1'), text=text)
    result = 'successfully' in content
    print(result, target)

    if result:
        project_controller.send_good_status()
        project_controller.send_count(1)
    else:
        project_controller.send_bad_status()


if __name__ == '__main__':
    spam()
    md.func_mapped_to_pool_concurrently(spam, target_pool, 50)
