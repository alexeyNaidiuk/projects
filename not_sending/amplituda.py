import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            'pll_language': 'ru',
        }
        headers = {
            'authority': 'amplituda.hr',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryofX66zwQeaJQ1f1n',
            # 'cookie': 'pll_language=ru',
            'origin': 'https://amplituda.hr',
            'referer': 'https://amplituda.hr/ru/kontakt-ru/',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        content = '------WebKitFormBoundaryofX66zwQeaJQ1f1n\r\nContent-Disposition: form-data; name="post_id"\r\n\r\n1370\r\n------WebKitFormBoundaryofX66zwQeaJQ1f1n\r\nContent-Disposition: form-data; name="form_id"\r\n\r\ncc14e2d\r\n------WebKitFormBoundaryofX66zwQeaJQ1f1n\r\nContent-Disposition: form-data; name="queried_id"\r\n\r\n1370\r\n------WebKitFormBoundaryofX66zwQeaJQ1f1n\r\nContent-Disposition: form-data; name="form_fields[name]"\r\n\r\n%(text)s\r\n------WebKitFormBoundaryofX66zwQeaJQ1f1n\r\nContent-Disposition: form-data; name="form_fields[email]"\r\n\r\n%(target)s\r\n------WebKitFormBoundaryofX66zwQeaJQ1f1n\r\nContent-Disposition: form-data; name="form_fields[field_b176409]"\r\n\r\n%(text)s\r\n------WebKitFormBoundaryofX66zwQeaJQ1f1n\r\nContent-Disposition: form-data; name="form_fields[message]"\r\n\r\n%(text)s\r\n------WebKitFormBoundaryofX66zwQeaJQ1f1n\r\nContent-Disposition: form-data; name="form_fields[field_e156a2a]"\r\n\r\non\r\n------WebKitFormBoundaryofX66zwQeaJQ1f1n\r\nContent-Disposition: form-data; name="form_fields[field_ea06525]"\r\n\r\nSend copy to yourself (optional)\r\n------WebKitFormBoundaryofX66zwQeaJQ1f1n\r\nContent-Disposition: form-data; name="action"\r\n\r\nelementor_pro_forms_send_form\r\n------WebKitFormBoundaryofX66zwQeaJQ1f1n\r\nContent-Disposition: form-data; name="referrer"\r\n\r\nhttps://amplituda.hr/ru/kontakt-ru/\r\n------WebKitFormBoundaryofX66zwQeaJQ1f1n--\r\n' % {
            'text': text, 'target': target}

        response = requests.post('https://amplituda.hr/wp-admin/admin-ajax.php', cookies=cookies, headers=headers,
                                 data=content, proxies=proxies)
        return response


if __name__ == '__main__':
    # not working
    success_message = '{"success":true,"data":{"message":"Message sent.","data":[]}}'
    promo_link = 'bit.ly/3Cw0s2r'
    project_name = 'amplituda'
    spam = ConcreteSpam(promo_link=promo_link, project_name=project_name,
                        success_message=success_message, text_encoding='latin-1')
    result = spam.send_post()
    # if result:
    #     spam.run_concurrently()
