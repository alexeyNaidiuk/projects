import requests

from module.spam_abstraction import Spam

url = 'http://www.rw2010.pl/go.live.php/usr_default/-/-/Register.html?usr_login_rd=SaHR0cDovL3d3dy5ydzIwMTAucGwvZ28ubGl2ZS5waHA=&rd2=html,8,rejestracjaedycja'

cookies = {
    'PHPSESSID': '38a8ba7ddeef22b26334ab592a123e74',
    'wwwrw2010pldsafeaktea_LANG_': 'SMg%253D%253D',
    '__utma': '24514105.1633723080.1668425641.1668425641.1668425641.1',
    '__utmc': '24514105',
    '__utmz': '24514105.1668425641.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '__utmt': '1',
    'kkdjjahnenmflkkasjjreb': 'VVRGT1EwMUdjRmxVYWtKS1VqSm5kMXBGYUVKT2EzZzFUMVJPYTAweVRqRlpNalZxWlZVeFJWSllaRTFpYTBwNlZFUkthMlJyZUhSbFNFSnJZbFpXTVZrd1pHOWtNSGQ0VVdzeFRWWlhZekJVUkU1TFlrZEdkRlpVTUQwPQ%3D%3D',
    'ppqoolemmvcnbbahrejjto': 'VVRGT1EwMUdjRmxVYWtKS1VqSm5kMXBGYUVKT2EzZzFUMVJPYTAweVRqRlpNalZxWlZVeFJWSllaRTFpYTBwNlZFUkthMlJyZUhSbFNFSnJZbFpXTVZrd1pHOWtNSGQ0VVdzeFRWWlhZekJVUkU1TFlrZEdkRlp1Y0d0VFJYQnZWMVJLZDJGR2NGaFZhbFphVFc1Q2IxUkVSa3RpUm05NVlraHdhMUl4V2pWVVJ6RnZUVWRLV0dSNU9XdFhSVFUxVjBSS05HUnNiM2xpU0ZaWlRUQndjbFZHV2s5aFJrNUhVMWhrV2sxR1NqSmFSM1F6Wld4d1JWUnRkR3hXUmxreFYydG9kMU50VVhkTlZsWlNWMFphY1ZWcVRtdE5iR1J4VTFSU2ExWXdjRWxaYTFKTFdWWldObFpxVGxwV1YyaERVMnhTVDFKUlBUMD0%3D',
    '__utmb': '24514105.4.10.1668425641',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary3unGxoACufNLQv8I',
    'Origin': 'http://www.rw2010.pl',
    'Referer': 'http://www.rw2010.pl/go.live.php/PL-H8/rejestracjaedycja/Register.html?usr_login_rd=SaHR0cDovL3d3dy5ydzIwMTAucGwvZ28ubGl2ZS5waHA%3D',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

DATA = '------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="gonext"\r\n\r\nEditAccount_Save\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="login"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="pass1"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="pass2"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="mail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="phone"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="companyname"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="nip"\r\n\r\ntest http://www\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="name"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="street"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="postcode"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="city"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="region"\r\n\r\n2\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="bankaccount"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I--\r\n'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('test http://www.rw2010.pl/go.live.php/PL-H8/rejest', self.get_text().encode().decode('latin-1'))
        data = data.replace('softumwork@gmail.com', target)

        response = requests.post(url, cookies=cookies, headers=headers, data=data, verify=False,
                                 proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Dziękujemy'
    project_name = 'rw2010'
    promo_link = 'bit.ly/3O5ndyD'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)
