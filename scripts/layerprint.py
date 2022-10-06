import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            '77b41a3f011471b1880f4b738934b019': 'aqd67hkjiofsvqjf755utc49b4',
            '18fca2d48e7846c9c4e34776235822a6': 'de-DE',
            '_ga': 'GA1.2.109849073.1664978490',
            '_gid': 'GA1.2.513796877.1664978490',
        }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Origin': 'http://layerprint.de',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://layerprint.de/kontakt-de',
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
            'id': '1:kontakt',
            '05f559ffee848d902a7eafd6b9fa05de': '1',
        }

        response = requests.post('http://layerprint.de/kontakt-de', cookies=cookies, headers=headers, data=data,
                                 verify=False, proxies=proxies)
        return response


if __name__ == '__main__':
    # not working
    success_message = 'Danke für die E-Mail!'
    project_name = 'layerprint'
    promo_link = 'bit.ly/3rv7pdS'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
