import requests
from requests_toolbelt import MultipartEncoder

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            '_ga': 'GA1.2.1334825578.1664455057',
            '_gid': 'GA1.2.1079586821.1664455057',
            '_gali': 'wpcf7-f141-p17-o1',
        }
        headers = {
            'authority': 'kiddosride.com',
            'accept': 'application/json, */*;q=0.1',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryPym58NBuD4EIY51x',
            'origin': 'https://kiddosride.com',
            'referer': 'https://kiddosride.com/contact-us/',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }
        fields = [
            {
                "name": "_wpcf7",
                "value": "141"
            },
            {
                "name": "_wpcf7_version",
                "value": "5.6.3"
            },
            {
                "name": "_wpcf7_locale",
                "value": "en_US"
            },
            {
                "name": "_wpcf7_unit_tag",
                "value": "wpcf7-f141-p17-o1"
            },
            {
                "name": "_wpcf7_container_post",
                "value": "17"
            },
            {
                "name": "_wpcf7_posted_data_hash",
                "value": ""
            },
            {
                "name": "your-name",
                "value": "test"
            },
            {
                "name": "your-email",
                "value": "softumwork@gmail.com"
            },
            {
                "name": "your-subject",
                "value": "test"
            },
            {
                "name": "your-message",
                "value": "test"
            }
        ]
        fields = {item['name']: item['value'] for item in fields}
        fields['your-name'] = text
        fields['your-message'] = text
        fields['your-subject'] = text
        fields['your-email'] = target
        content = MultipartEncoder(fields=fields)
        headers['content-type'] = content.content_type
        response = requests.post('https://kiddosride.com/wp-json/contact-form-7/v1/contact-forms/141/feedback',
                                 cookies=cookies, headers=headers, data=content, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Thank you for your message'
    project_name = 'kiddosride'
    promo_link = 'bit.ly/3BXywmu'
    spam = ConcreteSpam(promo_link, project_name, success_message=success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)
