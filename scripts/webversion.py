import requests

from module.spam_abstraction import Spam

url = 'https://webversion.net/1FEB31F9A313DF68F9C7060C0FF15F878C165DFBF94B4501D67B4FAE84624CAB067A1699C53A903916751F5D74D145E5/show.aspx'

headers = {
    'authority': 'webversion.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'origin': 'https://webversion.net',
    'referer': 'https://webversion.net/A771CD1A5C4941635830A050A37F2F372A2A8537CC91167F05583ABF0E1E806167AF8DFA6A6C056F6E14DAC91D896620/show.aspx?&addRows=true&curRows=4',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        text = self.get_text()
        data = {
            'senderName': text,
            'name0': text,
            'email0': target,
            'name1': text,
            'email1': target,
            'name2': text,
            'email2': target,
            'name3': text,
            'email3': target,
            'name4': text,
            'email4': target,
            'personalMessage': text,
            'sendType': 'html',
        }
        response = requests.post(url, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'המייל נשלח בהצלחה'
    project_name = 'webversion'
    promo_link = 'bit.ly/3GS9aLa'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
