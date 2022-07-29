import requests

from module.data import generate_proxy, main, try_to, get_proxies


text_body = '\u0020\u0035\u0030\u0020\u0444\u0440\u0438\u0441\u043f\u0438\u043d\u043e\u0432\u0020\u0437\u0430\u0020\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044e\u0020\u0432\u0020\u043a\u043b\u0443\u0431\u0435\u0020\u0053\u006c\u006f\u0074\u0074\u0069\u0063\u0061\u0020\u041f\u0435\u0440\u0435\u0445\u043e\u0434\u0438\u0020\u043f\u043e\u0020\u0441\u0441\u044b\u043b\u043a\u0435\u0020\u043d\u0438\u0436\u0435\u0020\u0438\u0020\u0437\u0430\u0431\u0438\u0440\u0430\u0439\u0020\u0441\u0432\u043e\u0439\u0020\u0431\u043e\u043d\u0443\u0441\u0021\u0020\u0068\u0074\u0074\u0070\u0073\u003a\u002f\u002f\u0062\u0069\u0074\u002e\u006c\u0079\u002f\u0033\u0063\u0036\u0051\u006f\u0053\u004f'
proxy_generator = generate_proxy(get_proxies(r'proxies_folder/west_proxy.txt'))


@try_to
def post(target='softumwork@gmail.com', proxy = None):
    proxy = {'http': proxy, 'https': proxy}
    url = 'https://www.karlstorz.com/de/ru/contact-karlstorz.htm'
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }
    params = {
        'backlink': '',
        'ff_285': '\u0020\u0035\u0030\u0020\u0444\u0440\u0438\u0441\u043f\u0438\u043d\u043e\u0432\u0020',
        'ff_288': text_body,
        'ff_300_left': text_body,
        'ff_300_right': '<<<',
        'ff_290': '\u0020\u0035\u0030\u0020\u0444\u0440\u0438\u0441\u043f\u0438\u043d\u043e\u0432\u0020\u0437\u0430\u0020\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044e\u0020\u0432\u0020\u043a\u043b\u0443\u0431\u0435\u0020\u0053\u006c\u006f\u0074\u0074\u0069\u0063\u0061\u0020\u041f\u0435\u0440\u0435\u0445\u043e\u0434\u0438\u0020\u043f\u043e\u0020\u0441\u0441\u044b\u043b\u043a\u0435\u0020\u043d\u0438\u0436\u0435\u0020\u0438\u0020\u0437\u0430\u0431\u0438\u0440\u0430\u0439\u0020\u0441\u0432\u043e\u0439\u0020\u0431\u043e\u043d\u0443\u0441\u0021\u0020',
        'ff_291': '^^^^^^^^^^^^^^^^^',
        'ff_292': '^^^^^^^^^^^^^^^^^',
        'ff_293': '^^^^^^^^^^^^^^^^^',
        'ff_294': '^^^^^^^^^^^^^^^^^',
        'ff_295': '^^^^^^^^^^^^^^^^^',
        'ff_4094': 'AU',
        'ff_297': '^^^^^^^^^^^^^^^^^',
        'ff_298': '^^^^^^^^^^^^^^^^^',
        'ff_299': target,
        'ff_301': '^^^^^^^^^^^^^^^^^',
        'ff_4139': '1',
        'email': '',
        'formsend': '1',
    }
    return requests.get(url, params, headers=headers, proxies=proxy)


def spam(target):
    res = None
    while res is None:
        proxy = next(proxy_generator)
        res = post(target, proxy)
    return res, target


if __name__ == '__main__':
    test = spam('softumwork@gmail.com')
    print(test)
    main(spam, targets_file_path=r'targets/all_turk.csv')
