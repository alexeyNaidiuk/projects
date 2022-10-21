import string

import requests

from module import Spam

URL = 'https://access.dnmx.org/src/compose.php'
COOKIES = {
    'SQMSESSID': 'knpfgrk0v89otnj944acuoakib',
    'key': 'VJgewu5Z1Vceu33J',
    'squirrelmail_language': 'deleted',
}
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarySlfCyO6Fpan0rSM2',
    'Origin': 'https://access.dnmx.org',
    'Referer': 'https://access.dnmx.org/src/compose.php?mailbox=INBOX&startMessage=1',
    'Sec-Fetch-Dest': 'frame',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
DATA = '------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="smtoken"\r\n\r\nqdqPqaUefN04\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="startMessage"\r\n\r\n1\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="session"\r\n\r\n1\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="passEed_id"\r\n\r\n\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="send_to"\r\n\r\n$target\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="send_to_cc"\r\n\r\n$target\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="send_to_bcc"\r\n\r\n$target\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="subject"\r\n\r\n$text\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="mailprio"\r\n\r\n3\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="body"\r\n\r\n$text\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="MAX_FILE_SIZE"\r\n\r\n2097152\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="attachfile"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="username"\r\n\r\nqwzxasqw@dnmx.org\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="smaction"\r\n\r\n\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="mailbox"\r\n\r\nINBOX\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="composesession"\r\n\r\n1\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="querystring"\r\n\r\nmailbox=INBOX&amp;startMessage=1\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="captcha"\r\n\r\nJSFg\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2\r\nContent-Disposition: form-data; name="send"\r\n\r\nsend\r\n------WebKitFormBoundarySlfCyO6Fpan0rSM2--\r\n'


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        data = string.Template(DATA).substitute({'text': text, 'target': target}).encode().decode('latin-1')
        response = requests.post(URL, cookies=COOKIES, headers=HEADERS, data=data, proxies=proxies, timeout=10)
        return response


if __name__ == '__main__':
    success_message = '@dnmx.org'
    project_name = 'dnmx'
    promo_link = 'bit.ly/3MJXmLG'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
