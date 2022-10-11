import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            '_ga': 'GA1.2.2043476603.1664983623',
            '__gads': 'ID=5317a01dc2fe17e4-2245003e3bce0096:T=1664983605:RT=1664983605:S=ALNI_MYByGLB3zJgJyua6E06bMGfwLjJPw',
            '3d22de3047dfdb8e38d7e6e28b54e0b1': 'rfdkf2fofg30ub9etm242vcml0',
            '_gid': 'GA1.2.1274630612.1665132008',
        }
        headers = {
            'authority': 'www.vimapoliti.gr',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            # Requests sorts cookies= alphabetically
            # 'cookie': '_ga=GA1.2.2043476603.1664983623; __gads=ID=5317a01dc2fe17e4-2245003e3bce0096:T=1664983605:RT=1664983605:S=ALNI_MYByGLB3zJgJyua6E06bMGfwLjJPw; 3d22de3047dfdb8e38d7e6e28b54e0b1=rfdkf2fofg30ub9etm242vcml0; _gid=GA1.2.1274630612.1665132008',
            'origin': 'https://www.vimapoliti.gr',
            'referer': 'https://www.vimapoliti.gr/politis/epikoinonia',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }
        data = {
            'jform[contact_name]': text,
            'jform[contact_email]': target,
            'jform[contact_subject]': text,
            'jform[contact_message]': text,
            'jform[contact_email_copy]': '1',
            'option': 'com_contact',
            'task': 'contact.submit',
            'return': '',
            'id': '1:diaxeiristes',
            'a5a802d1d1cd01bc9a5201a003a054ff': '1',
        }
        response = requests.post('https://www.vimapoliti.gr/politis/epikoinonia', cookies=cookies, headers=headers,
                                 data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Σας ευχαριστούμε για το μήνυμά σας.'
    project_name = 'vimapoliti'
    promo_link = 'bit.ly/3STX9aO'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
