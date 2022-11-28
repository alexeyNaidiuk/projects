import requests

from module.spam_abstraction import Spam

url = 'http://www.advantagebenefitsconsulting.com/forward.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        text = self.get_text()
        data = {
            'name': text,
            'email': target,
            'name2': text,
            'email2': target,
            'submit': 'refer',
            'submitted': 'TRUE',
        }

        response = requests.post(url, headers=headers, data=data, verify=False, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'has been sent'
    project_name = 'advantagebenefitsconsulting'
    promo_link = 'bit.ly/3VwfdsH'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
