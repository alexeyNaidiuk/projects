import logging

import bs4
import requests

import module.data as md

PROMO_LINK = 'bit.ly/3SrUvcb'

proxy_pool = md.WwmixProxyPool()
target_pool = md.TurkeyTargetPool()


def get(proxy):
    headers = {
        'authority': 'www.ocr.org.uk',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    response = requests.get('http://ocr.wufoo.com/forms/z7x3k1', headers=headers,
                            verify=False, proxies={'http': proxy, 'https': proxy})
    return response


def post(idstamp, proxy, target, text):
    data = '------WebKitFormBoundaryI0oEG75gswRoWAQG\r\nContent-Disposition: form-data; name="Field9"\r\n\r\n%(text)s\r\n------WebKitFormBoundaryI0oEG75gswRoWAQG\r\nContent-Disposition: form-data; name="Field2"\r\n\r\n%(target)s\r\n------WebKitFormBoundaryI0oEG75gswRoWAQG\r\nContent-Disposition: form-data; name="Field11"\r\n\r\n%(text)s\r\n------WebKitFormBoundaryI0oEG75gswRoWAQG\r\nContent-Disposition: form-data; name="Field1"\r\n\r\n%(text)s\r\n------WebKitFormBoundaryI0oEG75gswRoWAQG\r\nContent-Disposition: form-data; name="Field8"\r\n\r\n\r\n------WebKitFormBoundaryI0oEG75gswRoWAQG\r\nContent-Disposition: form-data; name="Field8"\r\n\r\nYes\r\n------WebKitFormBoundaryI0oEG75gswRoWAQG\r\nContent-Disposition: form-data; name="currentPage"\r\n\r\nzaekw4wuslashyhediWt2GfGC8SjcugzBqC5xNY9jG3qgaDwY=\r\n------WebKitFormBoundaryI0oEG75gswRoWAQG\r\nContent-Disposition: form-data; name="saveForm"\r\n\r\nSubmit\r\n------WebKitFormBoundaryI0oEG75gswRoWAQG\r\nContent-Disposition: form-data; name="comment"\r\n\r\n\r\n------WebKitFormBoundaryI0oEG75gswRoWAQG\r\nContent-Disposition: form-data; name="idstamp"\r\n\r\n%(idstamp)s\r\n------WebKitFormBoundaryI0oEG75gswRoWAQG\r\nContent-Disposition: form-data; name="encryptedPassword"\r\n\r\n\r\n------WebKitFormBoundaryI0oEG75gswRoWAQG\r\nContent-Disposition: form-data; name="stats"\r\n\r\n{"errors":0,"startTime":1096,"endTime":11391,"referer":"https://www.ocr.org.uk/"}\r\n------WebKitFormBoundaryI0oEG75gswRoWAQG\r\nContent-Disposition: form-data; name="clickOrEnter"\r\n\r\nclick\r\n------WebKitFormBoundaryI0oEG75gswRoWAQG--\r\n' % {
        'idstamp': idstamp, 'text': text, 'target': target}
    request = {'url': 'https://ocr.wufoo.com/forms/?formname=z7x3k1&embed=1&embedKey=z7x3k1547127&entsource=&referrer=',
               'headers': {'content-length': '1480', 'cache-control': 'max-age=0',
                           'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                           'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',
                           'upgrade-insecure-requests': '1', 'origin': 'https://ocr.wufoo.com',
                           'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryI0oEG75gswRoWAQG',
                           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                           'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1',
                           'sec-fetch-dest': 'iframe',
                           'referer': 'https://ocr.wufoo.com/forms/?formname=z7x3k1&embed=1&embedKey=z7x3k1547127&entsource=&referrer=',
                           'accept-encoding': 'gzip, deflate, br',
                           'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                           'cookie': 'ep201=S2MPCg2RRejQvAhqUO2D6wYob4o=; ep202=CD/jseutQKOHgOjdZLYELDOdr90=; _splunk_rum_sid=%7B%22id%22%3A%22e439340b12176e8a42f28accf10ae217%22%2C%22startTime%22%3A1663853979808%7D'},
               'data': data, 'proxies': {'http': proxy, 'https': proxy}}
    resp = requests.post(**request)
    return resp


def try_to_post(target, text):
    content = None
    while not content:
        proxy = proxy_pool.get_unique()
        try:
            get_resp = get(proxy=proxy)
            soup = bs4.BeautifulSoup(get_resp.content.decode(), 'lxml')
            idstamp = soup.find('input', {'id': 'idstamp'})['value'].replace('/', '')
            rep = post(proxy=proxy, target=target, text=text, idstamp=idstamp)
            content = rep.content.decode()
        except Exception as e:
            logging.error(e)
    return content


def spam(target='softumwork@gmail.com'):
    text = md.get_turk_spinned_text(link=PROMO_LINK, with_stickers=False, decoded=True)
    content = try_to_post(target=target, text=text)
    print('thanks' in content, target)


if __name__ == '__main__':
    md.func_mapped_to_pool_concurrently(spam, target_pool, 30)
    # spam()
