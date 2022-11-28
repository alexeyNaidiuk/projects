import requests

from module.spam_abstraction import Spam

url = 'https://webversion.net/1FEB31F9A313DF68F9C7060C0FF15F878C165DFBF94B4501D67B4FAE84624CAB067A1699C53A903916751F5D74D145E5/show.aspx'

headers = {
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
