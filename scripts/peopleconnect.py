import requests

import module

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
url = 'http://www.peopleconnect.com.au/refer-a-friend'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': '/wEPDwUKMjExNDUyMzEwMA9kFgJmD2QWAgIDD2QWAgILD2QWAmYPZBYCAgUPDxYEHghDc3NDbGFzcwUHY3VycmVudB4EXyFTQgICZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFHmN0bDAwJE1haW5Db250ZW50JEltYWdlQnV0dG9uMegtU4axxtT5deIf5LyONFg3USlC4HaUjr0q8KQiVbUp',
            '__VIEWSTATEGENERATOR': 'CB80D24E',
            '__EVENTVALIDATION': '/wEdAAiH2jUBzOMbBRxUYYe3BFB5XDTsqOiWfjOuHDcHFU+PI3V8fJKCYdhkVJdO+DIfQ0XRvDs5OXQ11rod7fgapnny0xahiDZxRyh5Q2CFuD1fpcm4Dg4her8nMjNi/Z4apy3HZuu2POyOjiZ3O+PdOLc3wcycRn+m1LKiok37o6zL/kLiEtm5syH0VNyxpRKwpHJ0XV89MQrEQIwiZFStbjPM',
            'ctl00$MainContent$txtYourName': self.get_text(),
            'ctl00$MainContent$txtYourEmail': target,
            'ctl00$MainContent$txtName': self.get_text(),
            'ctl00$MainContent$txtEmail': target,
            'ctl00$MainContent$txtPhone': self.get_text(),
            'ctl00$MainContent$txtComments': self.get_text(),
            'ctl00$MainContent$ImageButton1.x': '57',
            'ctl00$MainContent$ImageButton1.y': '13',
        }

        response = requests.post(url, headers=headers, data=data, verify=False, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    project_name = 'peopleconnect'
    s = 'Thank you for contacting People Connect!'

    link = 'bit.ly/3gLbZTC'
    project = 'fortuneclock'  # supercat luckybird allright fortuneclock
    spam = ConcreteSpam(project_name, s, referal_project_name=project, promo_link=link)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
