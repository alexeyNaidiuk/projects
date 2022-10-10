import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            'humans_21909': '1',
            'f3921aef6a5c0fe9e9ce2ebcf0adbfba': 'ogcripo0q3te24glit76hnqmp7',
            '_ga': 'GA1.2.721577742.1664896902',
            '_gid': 'GA1.2.1387303750.1664896902',
            '_gat': '1',
        }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Origin': 'http://sunway-network.com',
            'Referer': 'http://sunway-network.com/contact-us',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
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
            'id': '1:contact',
            'e25a0a8f9d3369d70c862acc5d0f9e58': '1',
        }
        response = requests.post('http://sunway-network.com/contact-us', cookies=cookies, headers=headers, data=data,
                                 verify=False, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Thank you for your email.'
    project_name = 'sunway'
    promo_link = 'bit.ly/3fG6rcf'
    spam = ConcreteSpam(promo_link, project_name, success_message=success_message)
    result = spam.send_post()  # False
    # if result:
    #     spam.run_concurrently()
