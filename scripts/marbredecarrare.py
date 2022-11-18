import requests

from module.spam_abstraction import Spam

URL = 'https://marbredecarrare.fr/wp-admin/admin-ajax.php'

cookies = {
    'mailchimp_landing_site': 'https%3A%2F%2Fmarbredecarrare.fr%2Fru%2F%25D0%25BF%25D1%2580%25D0%25BE%25D0%25B4%25D1%2583%25D0%25BA%25D1%2582%25D1%258B%2F',
    'pll_language': 'ru',
    '_gcl_au': '1.1.1620023896.1668784016',
    '_gid': 'GA1.2.1467870679.1668784016',
    'nitroCachedPage': '1',
    '__atuvc': '3%7C46',
    '__atuvs': '63779f8fc0e1f872002',
    '__atssc': 'google%3B3',
    '_ga_DM6XL6MM3S': 'GS1.1.1668784016.1.1.1668785620.0.0.0',
    '_ga': 'GA1.1.828290488.1668784016',
}

headers = {
    'authority': 'marbredecarrare.fr',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryCL5xTYVshmS7Kw5s',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fmarbredecarrare.fr%2Fru%2F%25D0%25BF%25D1%2580%25D0%25BE%25D0%25B4%25D1%2583%25D0%25BA%25D1%2582%25D1%258B%2F; pll_language=ru; _gcl_au=1.1.1620023896.1668784016; _gid=GA1.2.1467870679.1668784016; nitroCachedPage=1; __atuvc=3%7C46; __atuvs=63779f8fc0e1f872002; __atssc=google%3B3; _ga_DM6XL6MM3S=GS1.1.1668784016.1.1.1668785620.0.0.0; _ga=GA1.1.828290488.1668784016',
    'origin': 'https://marbredecarrare.fr',
    'referer': 'https://marbredecarrare.fr/ru/%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D1%8B/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = '------WebKitFormBoundaryCL5xTYVshmS7Kw5s\r\nContent-Disposition: form-data; name="contact-name"\r\n\r\ntest https://marbredecarrare.fr/ru/%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D1%8B/\r\n------WebKitFormBoundaryCL5xTYVshmS7Kw5s\r\nContent-Disposition: form-data; name="contact-email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryCL5xTYVshmS7Kw5s\r\nContent-Disposition: form-data; name="contact-message"\r\n\r\ntest https://marbredecarrare.fr/ru/%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D1%8B/\r\n------WebKitFormBoundaryCL5xTYVshmS7Kw5s\r\nContent-Disposition: form-data; name="contact-sendcopy"\r\n\r\n1\r\n------WebKitFormBoundaryCL5xTYVshmS7Kw5s\r\nContent-Disposition: form-data; name="gdpr"\r\n\r\n1\r\n------WebKitFormBoundaryCL5xTYVshmS7Kw5s\r\nContent-Disposition: form-data; name="action"\r\n\r\nbuilder_contact_send\r\n------WebKitFormBoundaryCL5xTYVshmS7Kw5s\r\nContent-Disposition: form-data; name="post_id"\r\n\r\n3310\r\n------WebKitFormBoundaryCL5xTYVshmS7Kw5s\r\nContent-Disposition: form-data; name="orig_id"\r\n\r\n929\r\n------WebKitFormBoundaryCL5xTYVshmS7Kw5s\r\nContent-Disposition: form-data; name="element_id"\r\n\r\n32ri603\r\n------WebKitFormBoundaryCL5xTYVshmS7Kw5s--\r\n'
        data = data.replace('softumwork@gmail.com', target)
        data = data.replace('test', self.get_text().encode().decode('latin-1'))
        response = requests.post(URL, cookies=cookies, headers=headers,
                                 data=data, proxies=self.get_proxies())

        return response


if __name__ == '__main__':
    success_message = 'Message sent.'
    project_name = 'marbredecarrare'
    promo_link = 'bit.ly/3hVyup5'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
