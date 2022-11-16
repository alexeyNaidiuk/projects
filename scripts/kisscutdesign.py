import requests

from module.spam_abstraction import Spam

cookies = {
    '__utma': '59974199.288916262.1668081882.1668081882.1668081882.1',
    '__utmc': '59974199',
    '__utmz': '59974199.1668081882.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '__utmt': '1',
    '__utmb': '59974199.1.10.1668081882',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryq9o0nYSbuDyPPSh8',
    'Origin': 'http://kisscutdesign.com',
    'Referer': 'http://kisscutdesign.com/contact/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
url = 'http://kisscutdesign.com/contact/'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = '------WebKitFormBoundaryq9o0nYSbuDyPPSh8\r\nContent-Disposition: form-data; name="input_1"\r\n\r\ntest\r\n------WebKitFormBoundaryq9o0nYSbuDyPPSh8\r\nContent-Disposition: form-data; name="input_2"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryq9o0nYSbuDyPPSh8\r\nContent-Disposition: form-data; name="input_3"\r\n\r\ntest\r\n------WebKitFormBoundaryq9o0nYSbuDyPPSh8\r\nContent-Disposition: form-data; name="is_submit_1"\r\n\r\n1\r\n------WebKitFormBoundaryq9o0nYSbuDyPPSh8\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n1\r\n------WebKitFormBoundaryq9o0nYSbuDyPPSh8\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n\r\n------WebKitFormBoundaryq9o0nYSbuDyPPSh8\r\nContent-Disposition: form-data; name="state_1"\r\n\r\nWyJbXSIsIjVhOWQ5NjBjYjBiYzM4OWM3Zjc1MTc5NmFjYjNiNGJjIl0=\r\n------WebKitFormBoundaryq9o0nYSbuDyPPSh8\r\nContent-Disposition: form-data; name="gform_target_page_number_1"\r\n\r\n0\r\n------WebKitFormBoundaryq9o0nYSbuDyPPSh8\r\nContent-Disposition: form-data; name="gform_source_page_number_1"\r\n\r\n1\r\n------WebKitFormBoundaryq9o0nYSbuDyPPSh8\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundaryq9o0nYSbuDyPPSh8--\r\n'
        data = data.replace('softumwork@gmail.com', target)
        data = data.replace('test', self.get_text().encode().decode('latin-1'))
        response = requests.post(url, cookies=cookies, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Thanks for the note'
    project_name = 'kisscutdesign'
    promo_link = 'bit.ly/3tgPWGO'
    spam = ConcreteSpam(promo_link, project_name, success_message, with_stickers=False)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)
