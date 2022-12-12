import requests

import module

url = 'https://oncdata.com/index.php'

cookies = {
    '9f69769e418e585696a4d80ea8b29492': '24df0ae1e00f1dbcdaa04c30c149a05e',
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

params = {
    'option': 'com_inviterefer',
    'view': 'inviterefer',
    'Itemid': '2943',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        text = self.get_text()
        data = [
            ('d94642a9312febcef2e6aa1a51523727', '1'),
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
            ('scode', 'eHJzMng='),
            ('scode2', ''),
            ('d94642a9312febcef2e6aa1a51523727', '1'),
        ]
        response = requests.post(url, params=params, cookies=cookies, headers=headers, data=data)
        return response


if __name__ == '__main__':
    project_name = 'oncdata'
    s = 'Thank you for Inviting'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3UQp383'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
