from typing import Optional

import requests

from module.data import get_proxies, generate_proxy, try_to, RuCaptchaSolver

proxy_generator = generate_proxy(set(get_proxies(r'C:\Users\Admin\Desktop\projects\proxies_folder\west_proxy.txt')))
solver = RuCaptchaSolver('a9ff25bbd91b50a49ce85a659ee53a08')


@try_to
def post(target, captcha_token: str, proxy: Optional[str] = None):
    proxies = {'http': proxy, 'https': proxy}
    url = 'https://www.anglia.com/about/feedback/feedback2.asp'
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
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }
    data = {'firstname': 'Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
            'lastName': 're',
            'company': 're',
            'custNumber': 're',
            'tel': '1964965416',
            'email': target,
            'subject': 'Order question',
            'message': 're',
            'formComment': '',
            'hdCapatchaToken': captcha_token,
            'btn_Send': 'Send'}
    return requests.post(url, headers=headers, data=data, proxies=proxies, timeout=10)


def spam(target: str):
    captcha_token = solver.solve('6Le8240UAAAAAN4CVS90rs3K3yN4TT-JgUB3efXD',
                                 'https://www.anglia.com/about/feedback/feedback.asp',
                                 method='hcaptcha')
    result = None
    while result is None:
        proxy = next(proxy_generator)
        result = post(target, captcha_token, proxy)
    return result, target


if __name__ == '__main__':
    test_res = spam('worksoftum@gmail.com')
    print(test_res)
    # main(spam)
