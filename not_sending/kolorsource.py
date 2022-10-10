import requests

from module import Spam


class ConcreteSpam(Spam):
    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            '_ga': 'GA1.2.1519921357.1664976166',
            '_gid': 'GA1.2.515859662.1664976166',
            'trustedsite_visit': '1',
            '0316b6cb7c699ccf8845410331805f3e': '8bda1b58fee5945123219c1d66af692a',
            '_gat_gtag_UA_8282430_6': '1',
            'trustedsite_tm_float_seen': '1',
        }

        headers = {
            'authority': 'kolorsource.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            # Requests sorts cookies= alphabetically
            # 'cookie': '_ga=GA1.2.1519921357.1664976166; _gid=GA1.2.515859662.1664976166; trustedsite_visit=1; 0316b6cb7c699ccf8845410331805f3e=8bda1b58fee5945123219c1d66af692a; _gat_gtag_UA_8282430_6=1; trustedsite_tm_float_seen=1',
            'origin': 'https://kolorsource.com',
            'referer': 'https://kolorsource.com/contact/contact-customer-care',
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
            'id': '1:information',
            '334c6fc4591feda4b2893a263e3649c9': '1',
        }

        response = requests.post('https://kolorsource.com/contact/contact-customer-care', cookies=cookies,
                                 headers=headers, data=data)
        return response


if __name__ == '__main__':
    # not working
    success_message = 'Thank you for your email.'
    project_name = 'kolorsource'
    promo_link = 'bit.ly/3rxWekQ'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
