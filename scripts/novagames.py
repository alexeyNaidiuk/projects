import requests

import module

URL = 'https://www.novagames.com/ru/about/vacancies'
cookies = {
    '_ga': 'GA1.2.2072384461.1670948568',
    '_gid': 'GA1.2.651308233.1670948568',
    '_gat': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryRSmY3rNUinkyxyPd',
    # 'Cookie': '_ga=GA1.2.2072384461.1670948568; _gid=GA1.2.651308233.1670948568; _gat=1',
    'Origin': 'https://www.novagames.com',
    'Referer': 'https://www.novagames.com/ru/about/vacancies',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
DATA = '------WebKitFormBoundaryRSmY3rNUinkyxyPd\r\nContent-Disposition: form-data; name="vacancy_request_form[vacancy]"\r\n\r\nДругое\r\n------WebKitFormBoundaryRSmY3rNUinkyxyPd\r\nContent-Disposition: form-data; name="vacancy_request_form[contact]"\r\n\r\ntest\r\n------WebKitFormBoundaryRSmY3rNUinkyxyPd\r\nContent-Disposition: form-data; name="vacancy_request_form[email]"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryRSmY3rNUinkyxyPd\r\nContent-Disposition: form-data; name="vacancy_request_form[message]"\r\n\r\ntest\r\n------WebKitFormBoundaryRSmY3rNUinkyxyPd\r\nContent-Disposition: form-data; name="vacancy_request_form[file]"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryRSmY3rNUinkyxyPd\r\nContent-Disposition: form-data; name="copy"\r\n\r\non\r\n------WebKitFormBoundaryRSmY3rNUinkyxyPd--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('test', self.get_text()).replace('softumwork@gmail.com', target)
        response = requests.post(URL, cookies=cookies, headers=headers,
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
