import requests

from module.spam_abstraction import Spam

url = 'https://hhisolutions.com/contact-us/'

headers = {
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = {
            'contact_name': target,
            'contact_email': target,
            'contact_subject': self.get_text(),
            'contact_message': 'Получи 50 free spins за Регистрацию в клубе по ссылке ниже https://bit.ly/3NXJdev Торопись, время действия приза ограничено!',
            'contact_email_copy': '1',
            'submit': '1',
        }

        response = requests.post(url, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Thank you!'
    project_name = 'hhisolutions'
    promo_link = 'bit.ly/3ABYNXE'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post('worksoftum@gmail.com')
    if res:
        spam.run_concurrently()
