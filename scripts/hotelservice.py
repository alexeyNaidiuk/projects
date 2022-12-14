import requests

import module

url = 'https://hotelservice.spb.ru/contact-us/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = {
            'zn_form_field_1_0': 'other',
            'zn_form_field_1_1': self.get_text(),
            'zn_form_field_1_2': '+79659659659',
            'zn_form_field_email1_3': target,
            'zn_form_field_1_4': target,
            'zn_form_field_1_5': target,
            'zn_form_field_1_6': target,
            'zn_form_field_1_7': target,
            'zn_form_field__152_1_8': 'true',
            'zn_pb_form_submit_1': '1',
            'send_me_copy_eluidb2441ab1': 'true',
        }
        response = requests.post(url, headers=headers, data=data)
        return response


if __name__ == '__main__':
    project_name = 'hotelservice'
    s = 'Спасибо за Ваше обращение!'

    project = 'supercat'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3UYguZ9'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
