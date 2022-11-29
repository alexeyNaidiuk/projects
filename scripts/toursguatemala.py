import requests

from module.spam_abstraction import Spam

url = 'https://www.toursguatemala.com/index.php/packages/short-breaks/242-escape-to-nature'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = {
            'formSent': '1',
            'jform[name]': target,
            'jform[Phone]': target,
            'jform[email]': target,
            'jform[Adults Child]': '1',
            'jform[Child]': '1',
            'jform[Arrival]': '2022-11-25',
            'jform[Departure]': '2022-11-30',
            'jform[Total budget (estimate):]': '5000',
            'jform[Additional Comments]': self.get_text(),
            'jform[sendcopy]': '1',
            'moduleId': '91',
        }

        response = requests.post(url, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Thank you!'
    project_name = 'toursguatemala'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3UeN4VZ'
    spam = ConcreteSpam(project_name, success_message, referal_project_name=project, promo_link=promo_link)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
