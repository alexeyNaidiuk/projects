import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            '9af67c8d2780d9b2dbfbd03235587c6a': 'f3fe18b78cf1faef520ad280916c41aa',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            # 'Cookie': '9af67c8d2780d9b2dbfbd03235587c6a=f3fe18b78cf1faef520ad280916c41aa',
            'Origin': 'http://www.acusticabrasilia.com',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://www.acusticabrasilia.com/contato.html',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }

        data = {
            'jform[contact_name]': text,
            'jform[contact_email]': target,
            'jform[contact_subject]': text,
            'jform[contact_message]': text,
            'jform[contact_email_copy]': '1',
            'jform[consentbox]': '0',
            'option': 'com_contact',
            'task': 'contact.submit',
            'return': '',
            'id': '1:benjamimjr',
            '0e1768d4d0865fb3ca2d73b761ad1048': '1',
        }
        response = requests.post('http://www.acusticabrasilia.com/contato.html', cookies=cookies, headers=headers,
                                 data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = ''
    project_name = 'acusticabrasilia'
    promo_link = 'bit.ly/3M8ZqwF'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
