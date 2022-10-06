import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            '72ede69985074582ddeaa5372978422f': 'igpg139au9tecpn75adneho6am',
            '__utma': '137002344.1349856939.1664978478.1664978478.1664978478.1',
            '__utmc': '137002344',
            '__utmz': '137002344.1664978478.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
            '__utmt': '1',
            '__gads': 'ID=f6b3ad9fad5faaa2-223372b53ace00d0:T=1664978462:RT=1664978462:S=ALNI_MY0gb92dcLT2Er1F8VMkhF36JIjOw',
            '__utmb': '137002344.3.10.1664978478',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Origin': 'http://www.ilredattore.it',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://www.ilredattore.it/contattaci.html',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }

        data = {
            'jform[contact_name]': text,
            'jform[contact_email]': target,
            'jform[contact_subject]': text,
            'jform[contact_email_copy]': '1',
            'jform[contact_message]': text,
            'option': 'com_contact',
            'task': 'contact.submit',
            'return': '',
            'id': '2:contattaci',
            'b8dc30e45ce45ab2fa055ea7c8a35a9e': '1',
        }

        response = requests.post('http://www.ilredattore.it/contattaci.html', cookies=cookies, headers=headers,
                                 data=data, verify=False, proxies=proxies)
        return response


if __name__ == '__main__':
    # not working
    success_message = 'Oggetto del messaggio'
    project_name = 'ilredattore'
    promo_link = 'bit.ly/3RxKclL'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
