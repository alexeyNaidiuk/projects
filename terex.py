import requests

from module.data import generate_proxy, main, try_to, get_proxies

proxy_generator = generate_proxy(get_proxies(r'proxies_folder/west_proxy.txt'))
text_body = '50 фриспинов за регистрацию в клубе Slottica Переходи по ссылке ниже и забирай свой бонус! https://bit.ly/3c6QoSO'


@try_to
def post(target, proxy=None):
    proxy = {'http': proxy, 'https': proxy}
    url = 'https://info.terex.com/l/28742/2021-09-17/99gw3q'
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Linux",
        "sec-fetch-dest": "iframe",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }
    data = {
        '28742_228995pi_28742_228995': 'Фриспины https://bit.ly/3c6QoSO',
        '28742_228997pi_28742_228997': text_body,
        '28742_228999pi_28742_228999': text_body,
        '28742_229001pi_28742_229001': target,
        '28742_229003pi_28742_229003': '2278459',
        '28742_229005pi_28742_229005': '2278493',
        'pi_extra_field': '',
        '_utf8': '☃',
        'hiddenDependentFields': ''
    }
    resp = requests.post(url, data, headers=headers, proxies=proxy)
    return resp


def spam(target):
    res = None
    while res is None:
        res = post(target, None)
    return res, target


if __name__ == '__main__':
    test = spam('softumwork@gmail.com')
    print(test)
    main(spam, 'targets/emails.txt')
