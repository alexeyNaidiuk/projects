import requests

import module

url = 'http://www.rw2010.pl/go.live.php/usr_default/-/-/Register.html?usr_login_rd=SaHR0cDovL3d3dy5ydzIwMTAucGwvZ28ubGl2ZS5waHA=&rd2=html,8,rejestracjaedycja'

headers = {
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary3unGxoACufNLQv8I',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

DATA = '------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="gonext"\r\n\r\nEditAccount_Save\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="login"\r\n\r\ntest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="pass1"\r\n\r\ntest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="pass2"\r\n\r\ntest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="mail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="phone"\r\n\r\ntest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="companyname"\r\n\r\ntest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="nip"\r\n\r\ntest http://www\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="name"\r\n\r\ntest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="street"\r\n\r\ntest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="postcode"\r\n\r\ntest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="city"\r\n\r\ntest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="region"\r\n\r\n2\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="bankaccount"\r\n\r\ntest\r\n------WebKitFormBoundary3unGxoACufNLQv8I--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('test', self.get_text())
        data = data.replace('softumwork@gmail.com', target)

        response = requests.post(url, headers=headers, data=data.encode(), verify=False,
                                 # proxies=self.get_proxies(),
                                 # timeout=10
                                 )
        return response


if __name__ == '__main__':
    success_message = 'Dziękujemy'
    project_name = 'rw2010'

    link = 'bit.ly/3Y99ECC'
    project = 'allright'
    spam = ConcreteSpam(
        project_name, success_message, referal_project_name=project,
        promo_link=link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
