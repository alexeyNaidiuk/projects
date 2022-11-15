import requests

from module.spam_abstraction import Spam


url = 'https://www.gerritsmainterieur.nl/customer/account/createpost/'

cookies = {
    '_ga': 'GA1.2.602278255.1668510414',
    '_gid': 'GA1.2.2088987538.1668510414',
    '_fbp': 'fb.1.1668510414430.1380717368',
    'mage-cache-storage': '%7B%7D',
    'mage-cache-storage-section-invalidation': '%7B%7D',
    'mage-cache-sessid': 'true',
    '_pin_unauth': 'dWlkPU0ySTFPREUxWVRJdE16SXdaQzAwTUdWaExXSTFabVF0T0RVek9UWmhZelV6TVdNMw',
    'mage-messages': '',
    'recently_viewed_product': '%7B%7D',
    'recently_viewed_product_previous': '%7B%7D',
    'recently_compared_product': '%7B%7D',
    'recently_compared_product_previous': '%7B%7D',
    'product_data_storage': '%7B%7D',
    'PHPSESSID': '0muu480lakedrft84bbnmnnlgp',
    'form_key': 'nINzn5P2aCu5OGdi',
    'private_content_version': '32ae99996068c3080601222d13659fcf',
    'mst_related_session_id': '16685104148466547',
    'mst-cache-warmer-track': '1668510441926',
    '_gali': 'form-validate',
    'section_data_ids': '%7B%22messages%22%3A1668511416%2C%22customer%22%3Anull%2C%22compare-products%22%3Anull%2C%22last-ordered-items%22%3Anull%2C%22cart%22%3Anull%2C%22directory-data%22%3Anull%2C%22captcha%22%3Anull%2C%22loggedAsCustomer%22%3Anull%2C%22persistent%22%3Anull%2C%22review%22%3Anull%2C%22wishlist%22%3Anull%2C%22guest_wishlist%22%3Anull%2C%22recently_viewed_product%22%3Anull%2C%22recently_compared_product%22%3Anull%2C%22product_data_storage%22%3Anull%7D',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryJwFC8pDmaLpJl5gS',
    'Origin': 'https://www.gerritsmainterieur.nl',
    'Referer': 'https://www.gerritsmainterieur.nl/customer/account/create/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}


class Foo(Spam):
    def post(self, text: str, target: str) -> requests.Response:
        data = '------WebKitFormBoundaryJwFC8pDmaLpJl5gS\r\nContent-Disposition: form-data; name="success_url"\r\n\r\n\r\n------WebKitFormBoundaryJwFC8pDmaLpJl5gS\r\nContent-Disposition: form-data; name="form_key"\r\n\r\nnINzn5P2aCu5OGdi\r\n------WebKitFormBoundaryJwFC8pDmaLpJl5gS\r\nContent-Disposition: form-data; name="error_url"\r\n\r\n\r\n------WebKitFormBoundaryJwFC8pDmaLpJl5gS\r\nContent-Disposition: form-data; name="firstname"\r\n\r\ntest gerritsmainterieur.nl/customer/account/create/\r\n------WebKitFormBoundaryJwFC8pDmaLpJl5gS\r\nContent-Disposition: form-data; name="lastname"\r\n\r\ntest gerritsmainterieur.nl/customer/account/create/\r\n------WebKitFormBoundaryJwFC8pDmaLpJl5gS\r\nContent-Disposition: form-data; name="is_subscribed"\r\n\r\n1\r\n------WebKitFormBoundaryJwFC8pDmaLpJl5gS\r\nContent-Disposition: form-data; name="email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryJwFC8pDmaLpJl5gS\r\nContent-Disposition: form-data; name="password"\r\n\r\nZxcasdqwe123\r\n------WebKitFormBoundaryJwFC8pDmaLpJl5gS\r\nContent-Disposition: form-data; name="password_confirmation"\r\n\r\nZxcasdqwe123\r\n------WebKitFormBoundaryJwFC8pDmaLpJl5gS--\r\n'
        data = data.replace('softumwork@gmail.com', target)
        data = data.replace('test', text.encode().decode('latin-1'))
        response = requests.post(url, cookies=cookies, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'success'
    project_name = 'gerritsmainterieur'
    promo_link = 'bit.ly/3GgbgUC'
    spam = Foo(promo_link, project_name, success_message, with_stickers=False)
    res = spam.send_post('softumwork+2@gmail.com')
    if res:
        spam.run_concurrently(5)
