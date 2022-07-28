import requests
from module.data import generate_proxy, get_proxies, try_to, main

proxy_pool = get_proxies(r'proxies_folder/west_proxy.txt')
proxy_generator = generate_proxy(proxy_pool)
text_body = '🔥 Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf'


@try_to
def post(target, proxy):
    proxies = {'http': proxy, 'https': proxy}
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'upgrade-insecure-requests': '1',
        'sec-fetch-user': '?1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'referer': 'https://windscribe.com/support/ticket',
        'origin': 'https://windscribe.com',
        'content-type': 'application/x-www-form-urlencoded',
        'cache-control': 'max-age=0',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'authority': 'windscribe.com'
    }
    url = 'https://windscribe.com/support/ticket'
    data = {
        'ticketsubmit': '1',
        'article_count': '0',
        'ticket_os': '',
        'ticket_type': '',
        't_email': target,
        't_username': 'testreqs',
        't_subject': text_body,
        't_message': text_body

    }
    resp = requests.post(url, headers=headers, data=data, proxies=proxies, timeout=10)
    return resp


def spam(target: str):
    result = None
    while result is None:
        proxy = next(proxy_generator)
        result = post(target, proxy)
    return result, target


if __name__ == '__main__':
    test_res = spam('softumwork@gmail.com')
    print(test_res)
    main(spam, targets_file_path='targets/all_turk.csv')
