import requests

import module

url = 'https://x1pphzxaa7.execute-api.ap-southeast-1.amazonaws.com/default/Zendesk-Website-Integration'

headers = {
    'origin': 'https://newcreation.org.sg',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = {
            'form_id': '360006685713',
            'name': self.get_text(),
            'email_address': target,
            'country': 'singapore',
            'contact_number': '2121211212',
            'type_en': 'volunteering_with_us',
            'zone_x': '',
            'order_no': '',
            'parent_name': '',
            'parent_contact': '',
            'mailing_address': '',
            'comment': self.get_text(),
            'pdpa_requester_en': 'on',
            'pdpa_related_en': 'on',
            'pdpa_third': 'on',
        }
        response = requests.post(url, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    project_name = 'newcreation'
    success_message = '"status":"new"'

    project = 'fortuneclock'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3EOzIu0'
    spam = ConcreteSpam(project_name, success_message, referal_project_name=project, promo_link=promo_link)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
