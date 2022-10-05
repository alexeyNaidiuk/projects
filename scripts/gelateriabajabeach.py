import logging

import requests
from requests_toolbelt import MultipartEncoder

from module.data import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            'bdbc9d9971ae3dc21b3b0ed4274c464c': 'en-GB',
            '785fada071385ad99c803d3b8a02b9b2': 'b55lq3jo6hvfh0rqombo0i6jv3',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Origin': 'http://www.gelateriabajabeach.com',
            'Referer': 'http://www.gelateriabajabeach.com/en/contact-us-2.html',
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
            'id': '1:website-owner',
            'ac817af459d7b8d0234a817bd99c685f': '1',
        }
        response = requests.post('http://www.gelateriabajabeach.com/en/contact-us-2.html', cookies=cookies,
                                 headers=headers, data=data, verify=False)
        return response


if __name__ == '__main__':
    success_message = 'Thank you for your email.'
    project_name = 'gelateriabajabeach'
    promo_link = 'bit.ly/3SyPkHG'
    spam = ConcreteSpam(promo_link, project_name, success_message=success_message, logging_level=logging.INFO)
    result = spam.send_post()
    if result:
        spam.run_concurrently()
