import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            'frontend': 'k5tmss7om0aepn75lsjh5e0ij6',
            'frontend_cid': 'EF5I0hg3uXgd7FA7',
            '_ga': 'GA1.2.1380673643.1666011246',
            '_gid': 'GA1.2.1271959684.1666011246',
            '_fbp': 'fb.1.1666011246513.52481250',
            '__zlcmid': '1CUlJ6aEcqnWf3A',
        }
        headers = {
            'authority': 'mashoonya.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'origin': 'https://mashoonya.com',
            'referer': 'https://mashoonya.com/customer/account/create/',
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
            'success_url': '',
            'error_url': '',
            'form_key': 'de4bz0Pl5TZUhKVe',
            'prefix': 'Mr',
            'firstname': text,
            'lastname': '',
            'email': target,
            'mobile': '3626236231',
            'is_subscribed': '1',
            'password': 'MgZqgMUx3q6b041pCX',
            'confirmation': 'MgZqgMUx3q6b041pCX',
            'persistent_remember_me': 'on',
            'terms': 'on',
        }
        response = requests.post('https://mashoonya.com/customer/account/createpost/', cookies=cookies, headers=headers,
                                 data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Kindly'
    project_name = 'mashoonya'
    promo_link = 'bit.ly/3VCqMzI'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post(target='softumwork+12@gmail.com')
    if res:
        spam.run_concurrently()
