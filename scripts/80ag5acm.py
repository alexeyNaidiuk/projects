import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            '_ga': 'GA1.2.985887142.1664976153',
            '_ym_uid': '1664976153846129477',
            '_ym_d': '1664976153',
            '492b99ac380a23b7c4cb70f29c1107da': '4ca27b52a23a7028c75091051a1ff5bb',
            '_gid': 'GA1.2.40531276.1665501480',
            '_ym_isad': '2',
            '_ym_visorc': 'w',
            '_gat': '1',
        }

        headers = {
            'authority': 'xn--80ag5acm.xn--80asehdb',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'origin': 'https://xn--80ag5acm.xn--80asehdb',
            'referer': 'https://xn--80ag5acm.xn--80asehdb/%D0%BD%D0%B0%D0%BF%D0%B8%D1%81%D0%B0%D1%82%D1%8C',
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
            'id': '1:форма-обратной-связи',
            'f65efd0e47b9c2ef04902234c482c273': '1',
        }

        response = requests.post('https://xn--80ag5acm.xn--80asehdb/%D0%BD%D0%B0%D0%BF%D0%B8%D1%81%D0%B0%D1%82%D1%8C',
                                 cookies=cookies, headers=headers, data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Спасибо'
    project_name = '80ag5acm'
    promo_link = 'bit.ly/3rN7BW4'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
