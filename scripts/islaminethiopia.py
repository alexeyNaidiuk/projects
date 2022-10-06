import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            'humans_21909': '1',
            'f193dd4b178456f08fbbfa8cee27c068': 'be5c82030f64dc1307bedb87a6fd6e24',
        }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Origin': 'http://islaminethiopia.com',
            'Referer': 'http://islaminethiopia.com/index.php/contact',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }
        data = {
            'jform[contact_name]': 'twat',
            'jform[contact_email]': target,
            'jform[contact_subject]': text,
            'jform[contact_message]': text,
            'jform[contact_email_copy]': '1',
            'option': 'com_contact',
            'task': 'contact.submit',
            'return': '',
            'id': '10:contact-us',
            'e94ea6dc67281277eeab501a42642134': '1',
        }
        response = requests.post('http://islaminethiopia.com/index.php/contact',
                                 cookies=cookies, headers=headers, data=data)
        return response


if __name__ == '__main__':
    # not working
    success_message = 'Thank you for your email.'
    project_name = 'islaminethiopia'
    promo_link = 'bit.ly/3Ca3mZd'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
