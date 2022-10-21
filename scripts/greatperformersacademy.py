import requests

from module import Spam

cookies = {
    'bbd0cfdf526da7f4c4cd902d52e43556': '95msiupqukatqqmm8qcs2qu0a2',
    '__atssc': 'google%3B1',
    '_ga': 'GA1.2.1463671656.1666347259',
    '_gid': 'GA1.2.282486168.1666347259',
    '__gads': 'ID=208cb2da53c6d6e4-224128d442b4006e:T=1666347253:RT=1666347253:S=ALNI_MYir63aKTtbx_3_8ikoPB0DTYIaug',
    '__gpi': 'UID=00000888dd69b776:T=1666347253:RT=1666347253:S=ALNI_MaXLKClDBlYLqr4i86Fx3yXtlZ4wA',
    '__atuvc': '3%7C42',
    '__atuvs': '6352a58f0b5bd35f000',
    '_gat': '1',
}

headers = {
    'authority': 'greatperformersacademy.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'origin': 'https://greatperformersacademy.com',
    'referer': 'https://greatperformersacademy.com/contribute',
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
url = 'https://greatperformersacademy.com/contribute'


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        data = {
            'jform[contact_name]': text,
            'jform[contact_email]': target,
            'jform[contact_subject]': text,
            'jform[contact_message]': text,
            'jform[contact_email_copy]': '1',
            'option': 'com_contact',
            'task': 'contact.submit',
            'return': '',
            'id': '1:about-us',
            '2863c739fc4e8048b50d82376e85b95e': '1',
        }

        response = requests.post(url, cookies=cookies, headers=headers, data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Thank you for your email.'
    project_name = 'greatperformersacademy'
    promo_link = 'bit.ly/3SgfEFL'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently(6)
