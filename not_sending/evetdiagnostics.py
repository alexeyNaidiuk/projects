import requests

from module.spam_abstraction import Spam

url = 'https://www.evetdiagnostics.com/(S(llmafrtlcy5ligkdsw4zo0de))/ContactUs.aspx'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'https://www.evetdiagnostics.com',
    'Referer': 'https://www.evetdiagnostics.com/(S(llmafrtlcy5ligkdsw4zo0de))/ContactUs.aspx',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
data = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': '',
    '__SCROLLPOSITIONX': '0',
    '__SCROLLPOSITIONY': '562',
    '__EVENTVALIDATION': '/wEdAAuvVXD1oYELeveMr0vHCmYP4ccGDk8cSgecUAAd4hqIktytASaofmdjlGHNGq/Wd8WWPQcRppNZvP2H5AXkJ0fd8/qPVmPBZCfHN4paGyZas/q+20//TnXTMh87xZFncc/3M3DJnDZ/tpLzEwm/bmI70YFe+cCuBAwFxroShnsdIlGA0QCmplLsNfU3yRTKv1lFJyI109haYg0KuKnXCrDTJ3GmwqyZeBMOHbeQn1sN4X6/6ef0T7XE8oTeXLbmf8sUzGEgx3PYvWvxqsVPYjY3',
    'tbName': 'test',
    'tbEmailAddress': 'softumwork@gmail.com',
    'tbSubject': 'test',
    'textAreaMessage': 'test',
    'tbCaptcha': '8506506',
    'checkBoxSendCopyToSender': 'on',
    'btnSendEmail': 'Send Email',
}


class ConcreteSpam(Spam):

    def post(self, text, target) -> requests.Response:
        data['tbEmailAddress'] = target
        data['tbName'] = text
        data['tbSubject'] = text
        data['textAreaMessage'] = text
        response = requests.post(url, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Your message has been sent!'
    project_name = 'evetdiagnostics'
    promo_link = 'bit.ly/3DhUjHA'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently(15)
