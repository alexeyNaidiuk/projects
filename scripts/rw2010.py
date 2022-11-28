import requests

import module

url = 'http://www.rw2010.pl/go.live.php/usr_default/-/-/Register.html?usr_login_rd=SaHR0cDovL3d3dy5ydzIwMTAucGwvZ28ubGl2ZS5waHA=&rd2=html,8,rejestracjaedycja'

headers = {
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary3unGxoACufNLQv8I',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

DATA = '------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="gonext"\r\n\r\nEditAccount_Save\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="login"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="pass1"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="pass2"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="mail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="phone"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="companyname"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="nip"\r\n\r\ntest http://www\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="name"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="street"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="postcode"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="city"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="region"\r\n\r\n2\r\n------WebKitFormBoundary3unGxoACufNLQv8I\r\nContent-Disposition: form-data; name="bankaccount"\r\n\r\ntest http://www.rw2010.pl/go.live.php/PL-H8/rejest\r\n------WebKitFormBoundary3unGxoACufNLQv8I--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('test http://www.rw2010.pl/go.live.php/PL-H8/rejest', self.get_text())
        data = data.replace('softumwork@gmail.com', target)

        response = requests.post(url, headers=headers, data=data.encode(), verify=False, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Dziękujemy'
    project_name = 'rw2010'
    # promo_link = 'bit.ly/3tPHsXt'
    target_pool_name = 'mixru'
    target_pool: module.Pool = module.TargetServerFactory.get_pool(factory_name=target_pool_name)
    proxy_pool_name = 'checked'
    proxy_pool: module.Pool = module.ProxyServerFactory.get_pool(factory_name=proxy_pool_name)
    target_lang = 'ru'
    text: module.Text = module.Text(text_lang=target_lang)

    project_controller: module.ProjectController = module.ProjectServerControllerCached(project_name=project_name)
    promo_link: str | None = project_controller.retrieve_attached_link()
    if not promo_link:
        promo_link = module.LinkShortner.get_link(target_pool_name)

    project_controller.prom_link = promo_link
    project_controller.get_status()

    spam = ConcreteSpam(project_controller, proxy_pool, target_pool, text, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
