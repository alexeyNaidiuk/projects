import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            '5d48211d582934135adc2d1bc45c4d6d': 'eebeae4fcd4e0561debcf8f45ee8a347',
        }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': '5d48211d582934135adc2d1bc45c4d6d=eebeae4fcd4e0561debcf8f45ee8a347',
            'Origin': 'http://escan-av.ir',
            'Referer': 'http://escan-av.ir/index.php/contact-us',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
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
            'id': '12:contact-us',
            '1f8b7fd384110d692b756ea9cb0c9fe7': '1',
        }

        response = requests.post('http://escan-av.ir/index.php/contact-us', cookies=cookies, headers=headers, data=data,
                                 verify=False, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'از ایمیل شما متشکریم'
    project_name = 'escan'
    promo_link = 'bit.ly/3SFv7Qy'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
