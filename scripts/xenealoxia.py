import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            'a848a72d01da156f1d0d7fa2fa64fd7e': '8fbe700cf3e8152a6826ffd7173f729e',
            '_ga': 'GA1.2.520972090.1665137332',
            '_gid': 'GA1.2.192882209.1665137332',
            '__gads': 'ID=70bfa692c874cd2a-22584cdd3dce0039:T=1665137312:RT=1665137312:S=ALNI_MbCE1bBnRX-U9cfyFzJLJnm1KFbtA',
            '__gpi': 'UID=00000b62691a9158:T=1665137312:RT=1665137312:S=ALNI_MYDOdu_v8cQ0enxdg8TOAaj0h47pA',
        }

        headers = {
            'authority': 'xenealoxia.org',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'a848a72d01da156f1d0d7fa2fa64fd7e=8fbe700cf3e8152a6826ffd7173f729e; _ga=GA1.2.520972090.1665137332; _gid=GA1.2.192882209.1665137332; __gads=ID=70bfa692c874cd2a-22584cdd3dce0039:T=1665137312:RT=1665137312:S=ALNI_MbCE1bBnRX-U9cfyFzJLJnm1KFbtA; __gpi=UID=00000b62691a9158:T=1665137312:RT=1665137312:S=ALNI_MYDOdu_v8cQ0enxdg8TOAaj0h47pA',
            'origin': 'https://xenealoxia.org',
            'referer': 'https://xenealoxia.org/xenealoxia/autores/30-ana-garcia',
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
            'jform[consentbox]': '0',
            'option': 'com_contact',
            'task': 'contact.submit',
            'return': '',
            'id': '30:ana-garcia',
            '150870d071dd07f6ef4eddbec8954f03': '1',
        }

        response = requests.post('https://xenealoxia.org/xenealoxia/autores', cookies=cookies, headers=headers,
                                 data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Gracias por su correo.'
    project_name = 'xenealoxia'
    promo_link = 'bit.ly/3CBGqnf '
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
