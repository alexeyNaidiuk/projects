import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            '3d22de3047dfdb8e38d7e6e28b54e0b1': 'i2u7lmgjnf4f42c61h5l1mhjo6',
        }
        headers = {
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
            '17c6d395b4f0100b2e5f0cebaea3f4b2': '1',
        }
        response = requests.post('https://www.vimapoliti.gr/politis/epikoinonia', cookies=cookies, headers=headers,
                                 data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Σας ευχαριστούμε για το μήνυμά σας.'
    project_name = 'vimapoliti'
    promo_link = 'bit.ly/3CtxBuA'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently(10)
