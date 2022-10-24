import requests
from faker import Faker

from module import Spam

cookies = {
    'd858fadf5b143974390b9e90ca6f5489': 'ka1caml7n23ju2ngp2ttfn9um3',
    '31fba641e4a7784499947b16de7edb83': 'en-GB',
}


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        headers = {
            'User-Agent': Faker().chrome(),
        }
        data = {
            'jform[contact_name]': text,
            'jform[contact_email]': target,
            'jform[contact_subject]': text,
            'jform[contact_message]': text,
            'jform[contact_email_copy]': '1',
            'option': 'com_contact',
            'task': 'contact.submit',
            'return': '',
            'id': '2:contacts',
            'ddc3aeb61e9aac89326a4da864ed61d0': '1',
        }

        response = requests.post('http://www.lalumacadelcavaliere.com/en/contacts.html', cookies=cookies,
                                 headers=headers, data=data, verify=False, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = ''
    project_name = 'lalumacadelcavaliere'
    promo_link = 'bit.ly/3z8pbrM'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    if res := spam.send_post():
        spam.run_concurrently()
