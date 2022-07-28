import requests

from module.data import get_proxies, generate_proxy, test_main, try_to, main

proxy_generator = generate_proxy(set(get_proxies(r'../proxies_folder/bad_proxies.txt')))


@try_to
def get(proxy: str = None):
    url = 'https://form.jotformpro.com/70654271017956'
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "cross-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }
    proxies = {'http': proxy, 'https': proxy}
    resp = requests.get(url, headers=headers, proxies=proxies)
    return resp


@try_to
def post(target: str, proxy: str = None):
    url = 'https://submit.jotformpro.com/submit/70654271017956/'
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }
    data = {
        'formID': '70654271017956',
        'q21_21': '🔥 Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'q29_29': '🔥 Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'q22_22': target,
        'q31_31': '🔥 Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'q23_23': '🔥 Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'q26_26': '🔥 Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'simple_spc': '70654271017956-70654271017956',
        'event_id': '1658756038607_70654271017956_0KdQSpP'  # var
    }
    proxies = {'http': proxy, 'https': proxy}
    resp = requests.post(url, headers=headers, data=data, proxies=proxies, verify=False, timeout=5)
    return resp


def spam(target: str):
    result = None
    while result is None:
        proxy = next(proxy_generator)
        post_resp = post(target, proxy)
        if post_resp:
            if 'captcha' not in post_resp.text:
                result = post_resp
    return result, target


if __name__ == '__main__':
    test_main(spam)
    main(spam, 5)
