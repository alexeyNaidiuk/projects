import re
from random import choice
from string import ascii_letters, digits

import requests

from module.spam_abstraction import Spam


def create_random_chars(amount):
    value = ''.join([choice(ascii_letters + digits) for _ in range(amount)])
    return value


class ConcreteSpam(Spam):
    def try_to_get(self, s) -> requests.Response:
        get_response = None
        while get_response is None:
            try:
                get_response: requests.Response | None = self.get(s)
            except Exception as error:
                print(error)
        return get_response

    def try_to_post_response(self, s: requests.Session, target: str, token: str) -> requests.Response:
        post_response = None
        while post_response is None:
            try:
                post_response: requests.Response | None = self.post(s=s, target=target, token=token)
            except Exception as error:
                print(error)
        return post_response

    def try_to_post(self, target) -> requests.Response:
        s = requests.Session()
        get_response: requests.Response = self.try_to_get(s)
        get_content = get_response.content.decode()

        pattern = re.compile('(?<=name="security_hash" class="cm-no-hide-input" value=").*(?=" /></form>)')
        token = pattern.search(get_content).group()
        post_response = self.try_to_post_response(s=s, target=target, token=token)
        return post_response

    def get(self, s: requests.Session) -> requests.Response:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://rareglobalfood.com/profiles-add/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        }

        url = 'http://rareglobalfood.com/profiles-add/'
        response = s.get(url, headers=headers, verify=False)
        return response

    def post(self, s: requests.Session, target, token) -> requests.Response:
        url = 'http://rareglobalfood.com/'
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryVeg0lCqIXPZ7GYT4',
            'Origin': 'http://rareglobalfood.com',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://rareglobalfood.com/profiles-add/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        }
        data = '------WebKitFormBoundaryVeg0lCqIXPZ7GYT4\r\nContent-Disposition: form-data; name="ship_to_another"\r\n\r\n1\r\n------WebKitFormBoundaryVeg0lCqIXPZ7GYT4\r\nContent-Disposition: form-data; name="user_data[firstname]"\r\n\r\ntest\r\n------WebKitFormBoundaryVeg0lCqIXPZ7GYT4\r\nContent-Disposition: form-data; name="user_data[lastname]"\r\n\r\ntest\r\n------WebKitFormBoundaryVeg0lCqIXPZ7GYT4\r\nContent-Disposition: form-data; name="user_data[company]"\r\n\r\ntest\r\n------WebKitFormBoundaryVeg0lCqIXPZ7GYT4\r\nContent-Disposition: form-data; name="user_data[phone]"\r\n\r\n123123123\r\n------WebKitFormBoundaryVeg0lCqIXPZ7GYT4\r\nContent-Disposition: form-data; name="user_data[email]"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryVeg0lCqIXPZ7GYT4\r\nContent-Disposition: form-data; name="user_data[password1]"\r\n\r\nZxcasdqwe123\r\n------WebKitFormBoundaryVeg0lCqIXPZ7GYT4\r\nContent-Disposition: form-data; name="user_data[password2]"\r\n\r\nZxcasdqwe123\r\n------WebKitFormBoundaryVeg0lCqIXPZ7GYT4\r\nContent-Disposition: form-data; name="dispatch[profiles.update]"\r\n\r\n\r\n------WebKitFormBoundaryVeg0lCqIXPZ7GYT4\r\nContent-Disposition: form-data; name="security_hash"\r\n\r\ne56c263673fc4488563c7db2117953ba\r\n------WebKitFormBoundaryVeg0lCqIXPZ7GYT4--\r\n'
        data = data.replace('softumwork@gmail.com', target)
        data = data.replace('test', self.get_text(False))
        data = data.replace('e56c263673fc4488563c7db2117953ba', token)
        response = s.post(url, headers=headers, data=data.encode(), verify=False, timeout=10)
        return response


if __name__ == '__main__':
    success_message = 'successfully'
    project_name = 'rareglobalfood'

    referal_project_name = 'allright'
    link = 'bit.ly/3FgK7yR'
    spam = ConcreteSpam(
        project_name, success_message, referal_project_name=referal_project_name,
        promo_link=link
    )
    random_letters = create_random_chars(10)
    res = spam.send_post(f'softumwork+food{random_letters}@gmail.com')
    if res:
        spam.run_concurrently()
