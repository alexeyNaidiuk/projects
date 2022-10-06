import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            '5504e135cb4b28c99390ca36175162fa': '7d1e55192bc46956beebcf2663aad5ce',
        }
        headers = {
            'authority': 'maloobchod.svetkamenov.sk',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            # 'cookie': '5504e135cb4b28c99390ca36175162fa=7d1e55192bc46956beebcf2663aad5ce',
            'origin': 'https://maloobchod.svetkamenov.sk',
            'referer': 'https://maloobchod.svetkamenov.sk/Kontaktujte-Nas.Html',
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
            'id': '2:our-address',
            '9a0aa178f8ddd7f6e5dc5d4a46336a11': '1',
            'gdpr_privacy_policy_checkbox': '1',
        }
        response = requests.post('https://maloobchod.svetkamenov.sk/kontaktujte-nas.html', cookies=cookies,
                                 headers=headers, data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    # False
    success_message = 'Vďaka za váš e-mail.'
    project_name = 'maloobchod'
    promo_link = 'bit.ly/3CyZ4vT'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
