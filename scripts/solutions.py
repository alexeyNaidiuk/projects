import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            '9bcccaabb11db5e9457512f37e15f680': 'h57v0cpasrpjsi87oji1lu15p1',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            # 'Cookie': '9bcccaabb11db5e9457512f37e15f680=h57v0cpasrpjsi87oji1lu15p1',
            'Origin': 'http://www.ag-solutions.it',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://www.ag-solutions.it/index.php?option=com_contact&view=contact&id=1&Itemid=163',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }

        params = {
            'option': 'com_contact',
            'view': 'contact',
            'id': '1',
            'Itemid': '163',
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
            'id': '1:amministratore',
            '4bad1bf3e7713386c55db6dc2c055182': '1',
        }

        response = requests.post('http://www.ag-solutions.it/index.php', params=params, cookies=cookies,
                                 headers=headers, data=data, verify=False, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Grazie per la tua email.'
    project_name = 'solutions'
    promo_link = 'bit.ly/3SElcuC'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()  # False
    # if res:
    #     spam.run_concurrently()
