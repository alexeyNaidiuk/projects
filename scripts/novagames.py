import requests

import module

URL = 'https://www.novagames.com/ru/about/vacancies'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryRSmY3rNUinkyxyPd',
}
DATA = '------WebKitFormBoundaryRSmY3rNUinkyxyPd\r\nContent-Disposition: form-data; name="vacancy_request_form[vacancy]"\r\n\r\nДругое\r\n------WebKitFormBoundaryRSmY3rNUinkyxyPd\r\nContent-Disposition: form-data; name="vacancy_request_form[contact]"\r\n\r\ntest\r\n------WebKitFormBoundaryRSmY3rNUinkyxyPd\r\nContent-Disposition: form-data; name="vacancy_request_form[email]"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryRSmY3rNUinkyxyPd\r\nContent-Disposition: form-data; name="vacancy_request_form[message]"\r\n\r\ntest\r\n------WebKitFormBoundaryRSmY3rNUinkyxyPd\r\nContent-Disposition: form-data; name="vacancy_request_form[file]"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryRSmY3rNUinkyxyPd\r\nContent-Disposition: form-data; name="copy"\r\n\r\non\r\n------WebKitFormBoundaryRSmY3rNUinkyxyPd--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('test', self.get_text()).replace('softumwork@gmail.com', target)
        response = requests.post(URL, headers=headers,
                                 data=data.encode(), verify=False)
        return response


if __name__ == '__main__':
    project_name = 'novagames'
    s = 'Спасибо за ваш интерес!'

    project = 'fortuneclock'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3VV7Vzm'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
