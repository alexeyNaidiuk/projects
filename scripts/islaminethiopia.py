import requests

from module.spam_abstraction import Spam

url = 'http://islaminethiopia.com/index.php/contact'

cookies = {
    'humans_21909': '1',
    'f193dd4b178456f08fbbfa8cee27c068': 'f3b3f40262d4cfec991876f5c94b8f26',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'humans_21909=1; f193dd4b178456f08fbbfa8cee27c068=f3b3f40262d4cfec991876f5c94b8f26',
    'Origin': 'http://islaminethiopia.com',
    'Referer': 'http://islaminethiopia.com/index.php/contact',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = {
            'jform[contact_name]': target,
            'jform[contact_email]': target,
            'jform[contact_subject]': '50 Фриспинов за регистрацию в клубе!',
            'jform[contact_message]': self.get_text(),
            'jform[contact_email_copy]': '1',
            'option': 'com_contact',
            'task': 'contact.submit',
            'return': '',
            'id': '10:contact-us',
            '09b17eb97afc83bdd51e3be48dd08694': '1',
        }

        response = requests.post(url, cookies=cookies, headers=headers, data=data, verify=False,
                                 proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Thank you for your email.'
    project_name = 'islaminethiopia'
    promo_link = 'bit.ly/3gh4Utw'
    spam = ConcreteSpam(promo_link, project_name, success_message, with_stickers=False)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)
