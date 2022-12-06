import requests

import module

url = 'http://www.safestoragesolutions.com/wp-admin/admin-ajax.php'

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

params = {
    'action': 'pwebcontact_sendEmail',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = {
            'mid': '2',
            'format': 'json',
            'ignoreMessages': 'true',
            'fields[name]': 'test',
            'fields[phone]': '122121',
            'fields[email]': target,
            'fields[pickone]': '5x5',
            'fields[startdate]': '30-10-2022',
            'fields[message]': self.get_text(),
            'copy': '1',
            '21e858c022': '1',
            'title': 'Request a Quote – Safe Storage Solutions',
            'url': 'http://www.safestoragesolutions.com/request-a-quote/',
            'screen_resolution': '1920x1080',
        }
        response = requests.post(
            url,
            params=params,
            headers=headers,
            data=data,
            verify=False,
            proxies=self.get_proxies(),
            timeout=10
        )
        return response


if __name__ == '__main__':
    project_name = 'safestoragesolutions'
    s = 'success":true'

    project = 'supercat'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3h6ba82'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link,
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
