import re
from time import sleep

import bs4
import requests

from module import Spam


class ConcSpam(Spam):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_tokens(self, content: str):
        soup = bs4.BeautifulSoup(content, 'lxml')
        access_key = soup.find('input', {'type': 'hidden', 'value': '1'})['name']
        captcha_question_id = soup.find('input', {'type': 'text', 'required': 'required'})['id']
        captcha_text = soup.find('div', {'id': 'easycalccheckplus'}).text.replace('плюс', '+').replace('минус', '-')
        captcha_answer = eval(
            re.findall(r'(?<=ПРОВЕРКА на СПАМ: ).*(?= равно Protected by EasyCalcCheck Plus)', captcha_text)[0])
        another_token = [item for item in soup.find_all('input', dict(type="text", size="30")) if
                         'inputbox' in item['class']][0]['name']
        return access_key, captcha_question_id, captcha_text, captcha_answer, another_token

    def try_to_post(self, target: str, text: str) -> requests.Response:
        response = None
        while not response:
            s = requests.Session()
            proxy = self.proxy_pool.pop()
            proxies = {'http': proxy, 'https': proxy}
            try:
                get_resp = self.get(s, proxies)
                self.logger.debug(get_resp)
                cont = get_resp.content.decode()
                access_key, captcha_question_id, captcha_text, captcha_answer, another_token = self.get_tokens(cont)
            except Exception as e:
                self.logger.error(e)
                continue
            sleep(7)
            try:
                response = self.post(s, proxies, access_key, captcha_answer, captcha_question_id, another_token, target,
                                     text)
                self.logger.debug(response)
            except Exception as e:
                self.logger.error(e)
        return response

    def get(self, s: requests.Session, proxies: dict):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://modelstend.by/index.php/contact-us-page',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }
        response = s.get('http://modelstend.by/index.php/contact-us-page', headers=headers, proxies=proxies)
        return response

    def post(self, s: requests.Session,
             proxies: dict, access_key: str,
             captcha_answer: int, captcha_question_id: str, another_token: str,
             target: str, text: str) -> requests.Response:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Origin': 'http://modelstend.by',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://modelstend.by/index.php/contact-us-page',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }
        data = {
            'jform[contact_name]': text,
            another_token: '',
            'jform[contact_email]': target,
            'jform[contact_subject]': text,
            'jform[contact_message]': text,
            'jform[contact_email_copy]': '1',
            captcha_question_id: str(captcha_answer),
            'option': 'com_contact',
            'task': 'contact.submit',
            'return': '',
            'id': '1:name',
            access_key: '1',
        }
        response = s.post('http://modelstend.by/index.php/contact-us-page', headers=headers, data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    succ_message = 'Спасибо за ваше письмо!'
    project_name = 'modelstend'
    promo_link = 'bit.ly/3yiF4LO'
    spam = ConcSpam(promo_link=promo_link, project_name=project_name, success_message=succ_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)
