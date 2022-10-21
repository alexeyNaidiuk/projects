import requests

from module import Spam

cookies = {
    'paradigm-win-switcher': '1',
    'PHPSESSID': '433lpl91qo0i1nkb83cqaqon91',
    '__atssc': 'google%3B1',
    '__atuvc': '5%7C42',
    '__atuvs': '635120584d8b89a6002',
}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'paradigm-win-switcher=1; PHPSESSID=433lpl91qo0i1nkb83cqaqon91; __atssc=google%3B1; __atuvc=5%7C42; __atuvs=635120584d8b89a6002',
    'Origin': 'https://www.encryptoo.es',
    'Referer': 'https://www.encryptoo.es/contact/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        data = {
            'rt-contact-name': text,
            'rt-contact-email': target,
            'rt-contact-subject': text,
            'rt-contact-message': text,
            'rt-send-copy': 'true',
            'submit': '',
            'submitted': 'true',
        }

        response = requests.post('https://www.encryptoo.es/contact/', cookies=cookies, headers=headers, data=data,
                                 proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Thank you!'
    project_name = 'encryptoo'
    promo_link = 'bit.ly/3SpCGtW'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
