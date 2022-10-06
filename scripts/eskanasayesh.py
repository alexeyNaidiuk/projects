import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            'cf5272d251536174225bb3e003a77d13': 'p4bv3uee5d833ljkskb8pupk63',
            'http://eskanasayesh.com/2012-11-29-12-20-39': '0.8125,0.8125',
        }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Origin': 'http://eskanasayesh.com',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://eskanasayesh.com/2012-11-29-12-20-39',
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
            'id': '1:eskan-asayesh',
            '72a79044c82b00b6751d8d8c4c5dbddf': '1',
        }

        response = requests.post('http://eskanasayesh.com/2012-11-29-12-20-39', cookies=cookies, headers=headers,
                                 data=data, verify=False, proxies=proxies)
        return response


if __name__ == '__main__':
    # not working
    success_message = 'از ايميل شما متشکريم'
    project_name = 'eskanasayesh'
    promo_link = 'bit.ly/3rzCxsA'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
