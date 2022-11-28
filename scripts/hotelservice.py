import requests

from module.spam_abstraction import Spam

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
url = 'https://hotelservice.spb.ru/contact-us/'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        text = self.get_text()
        data = {
            'zn_form_field_1_0': 'consult',
            'zn_form_field_1_1': text,
            'zn_form_field_1_2': '+7965965965',
            'zn_form_field_email1_3': target,
            'zn_form_field_1_4': target,
            'zn_form_field_1_5': target,
            'zn_form_field_1_6': target,
            'zn_form_field_1_7': target,
            'zn_form_field__152_1_8': 'true',
            'zn_pb_form_submit_1': '1',
            'send_me_copy_eluidb2441ab1': 'true',
        }
        response = requests.post(url, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Спасибо'
    project_name = 'hotelservice'
    promo_link = 'bit.ly/3gs501C'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently(1)
