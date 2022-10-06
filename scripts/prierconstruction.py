import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            'PHPSESSID': 'u6ool0i0d56hdaks1p0mm4p1f1',
            'session': 'e789b250712ce4a9b1428e2eee7fe80b.63356d95799c7',
        }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'PHPSESSID=u6ool0i0d56hdaks1p0mm4p1f1; session=e789b250712ce4a9b1428e2eee7fe80b.63356d95799c7',
            'Origin': 'http://prierconstruction.com',
            'Referer': 'http://prierconstruction.com/_forms/contact-footer.php',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }
        content = {
            'name': text,
            'email': target,
            'phone': text,
            'msg': text,
            'sbmtbtn': 'SUBMIT',
        }
        response = requests.post('http://prierconstruction.com/_forms/contact-footer.php', cookies=cookies,
                                 headers=headers, data=content, verify=False, proxies=proxies)
        return response


if __name__ == '__main__':
    spam = ConcreteSpam(promo_link='bit.ly/3CjqJB2', project_name='prierconstruction', success_message='Thank You')
    res = spam.send_post()  # False3
    # if res:
    #     spam.run_concurrently()
