import requests
from faker import Faker

from module.spam_abstraction import Spam

cookies = {
    'ASP.NET_SessionId': 'oxu5u01liqsfnzysjxhiilzk',
    '_ga': 'GA1.2.751671806.1668770618',
    '_gid': 'GA1.2.1547697915.1668770618',
    '_gat': '1',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'http://www.plastemart.com',
    'Referer': 'http://www.plastemart.com/contact-reach-plastemart-details',
}

url = 'http://www.plastemart.com/FooterPages/SaveContactUsData'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        headers['User-Agent'] = Faker().user_agent()
        text = self.get_text()
        json_data = {
            'cont': {
                'FName': text,
                'LName': text,
                'Company': text,
                'Email': target,
                'Mobile': '12212121',
                'CountryName': 'African Continent',
                'Remarks': text,
                'Address': text,
            },
            'currenturl': 'http://www.plastemart.com/contact-reach-plastemart-details',
        }

        response = requests.post(url, cookies=cookies, headers=headers, json=json_data, verify=False,
                                 proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = ''
    project_name = 'plastemart'
    promo_link = 'bit.ly/3tHWsa4'
    spam = ConcreteSpam(promo_link, project_name, success_message, logging_level='debug')
    res = spam.send_post()
    if res:
        spam.run_concurrently()
