import requests

from module import Spam

cookies = {
    'dnn_IsMobile': 'False',
    'language': 'en-US',
    '.ASPXANONYMOUS': 'Sjc4e_1JkR09zCQVmp8wV0Fe-_aTIbPvoIj3Pwi5Rt88KcUhnrYINrOA3c4UngO_q2Jm5LXeEGTGATLGk1fXzG7d0kMpkDeSXjts8DPAg4-um59P0',
    'Analytics_VisitorId': '9f8a1e19-e876-4926-afa0-c66655a048bc',
    '__RequestVerificationToken': 'lsn8FjcloUnATJbOV3K-vAhoZTgPVcu-YkHXk2JopDdA0GrM4z7XWu0i8lbUrCjD3FUBKA2',
    '_ga': 'GA1.2.76703644.1666347308',
    '_gid': 'GA1.2.1393305623.1666347308',
    'nmstat': 'fff6bc09-91f8-5c9e-93dd-b12fe366f533',
    'Analytics': 'SessionId=88b0a6a7-f2d9-4f58-a264-7468c16c5f36&TabId=137&ContentItemId=-1',
    '_gat_gtag_UA_6718836_1': '1',
}
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.lacoe.edu',
    'Referer': 'https://www.lacoe.edu/Contact-Us',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
params = {
    'TabId': '137',
    'language': 'en-US',
    'alias': 'www.lacoe.edu',
    'mid': '6971',
    'event': 'click',
    'b': '1320',
    'referrer': '',
    '_url': 'https://www.lacoe.edu/Contact-Us',
}
url = 'https://www.lacoe.edu/DesktopModules/DnnSharp/ActionForm/Submit.ashx'


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        data = {
            'Instructions': 'Please fill out all fields before submitting your inquiry.  Someone will respond to your request during normal business hours.',
            'Email': target,
            'Name': text,
            'MultipleChoicewithDropdown': '/Macias_Salvador@lacoe.edu',
            'Message': text,
            'CAPTCHAcaptchaenc': '6F00F86C92524EB5B583EDB47C6CDA6DF8B894A2EF1A6D226DEA1DD43ECE1CB19035C8FD22CF08C0C2747C06A53F567E9315D1FDCC1ED05F915BC081A3555337A1C2A7FC929C0500BBC4686D4A085927201AB30590FF14714EBD96AEEC1100F0C6C36177823EC2E706DD08C0484573185FA32CD4D2AA6F143C356180',
            'CAPTCHA': 'KmPdoi',
            'SendCopytoYourself': 'True',
        }
        response = requests.post(url,
                                 params=params, cookies=cookies, headers=headers, data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'hank you for your inquiry!'
    project_name = 'lacoe'
    promo_link = 'bit.ly/3sbukvf'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)
