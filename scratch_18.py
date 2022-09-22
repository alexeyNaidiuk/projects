import logging

import requests

import module.data as md

prom_link = 'bit.ly/3duOHjj'

proxy_pool = md.WwmixProxyPool()
target_pool = md.TurkeyTargetPool()


def post(proxy, target, text):
    request = {'url': 'https://www.eulenschlupf-spreewald.de/preise_und_kontakt.php?lang=en',
               'headers': {'content-length': '334', 'cache-control': 'max-age=0',
                           'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                           'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',
                           'upgrade-insecure-requests': '1', 'origin': 'https://www.eulenschlupf-spreewald.de',
                           'content-type': 'application/x-www-form-urlencoded',
                           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                           'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1',
                           'sec-fetch-dest': 'document',
                           'referer': 'https://www.eulenschlupf-spreewald.de/preise_und_kontakt.php?lang=en',
                           'accept-encoding': 'gzip, deflate, br',
                           'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                           'cookie': 'PHPSESSID=pakn8ujlqr5ipeibed89ak69im'}, 'data': {
            'name': 'name', 'email': target, 'betreff': 'ref', 'nachricht': text, 'kopie': 'ja', 'Absenden': 'Submit'},
               'proxies': {'http': proxy, 'https': proxy}}
    response = requests.post(**request)
    return response


def try_to_post(target, text):
    content = None
    while not content:
        proxy = proxy_pool.get_unique()
        try:
            rep = post(proxy, target, text)
            content = rep.content.decode()
        except Exception as e:
            logging.error(e)
    return content


def spam(target='softumwork@gmail.com'):
    text = md.get_turk_spinned_text(link=prom_link, with_stickers=True, decoded=False)
    content = try_to_post(target=target, text=text)
    print('Thank you for your message.' in content, target)


if __name__ == '__main__':
    md.func_mapped_to_pool_concurrently(spam, target_pool, 30)
    # spam()
