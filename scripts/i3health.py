import requests

import module

url = 'https://www.i3health.com/index.php'
cookies = {
    'e79021f9fc55873d8ea51109cedd972e': '3aac7e8384cf71fb9e8ae0eda45c780d',
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
params = {
    'option': 'com_inviterefer',
    'view': 'inviterefer',
    'Itemid': '3737',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        text = self.get_text()
        data = [
            ('5ba6dcc476a4ebc76e33faa22f2d383c', '1'),
            ('option', 'com_inviterefer'),
            ('task', 'send'),
            ('recommend_from_name', text),
            ('recommend_from_email', target),
            ('recommend_to_name0', text),
            ('recommend_to_email0', target),
            ('recommend_to_name1', text),
            ('recommend_to_email1', target),
            ('recommend_to_name2', text),
            ('recommend_to_email2', target),
            ('recommend_to_name3', text),
            ('recommend_to_email3', target),
            ('recommend_text', text),
            ('Submit', 'Send Invitation'),
            ('recommend_option', 'send'),
            ('scode', 'dm5mamg='),
            ('scode2', ''),
            ('5ba6dcc476a4ebc76e33faa22f2d383c', '1'),
        ]

        response = requests.post(url, params=params, cookies=cookies, headers=headers,
                                 data=data)
        return response


if __name__ == '__main__':
    project_name = 'i3health'
    s = 'Thank you for Inviting'

    project = 'supercat'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3uIR7j3'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
