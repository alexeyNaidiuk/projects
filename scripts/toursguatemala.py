import requests

from module.spam_abstraction import Spam

url = 'https://www.toursguatemala.com/index.php/packages/short-breaks/242-escape-to-nature'

cookies = {
    '_gid': 'GA1.2.1929494318.1668605286',
    'd5e3c24b6379010083a67d3015576e03': 'd944a50ebb28cefaf6f0784c77d4df98',
    '_gat_gtag_UA_216532762_1': '1',
    '_ga_WTNMETJBE4': 'GS1.1.1668605285.1.1.1668606916.0.0.0',
    '_ga': 'GA1.1.169033319.1668605285',
}

headers = {
    'authority': 'www.toursguatemala.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_gid=GA1.2.1929494318.1668605286; d5e3c24b6379010083a67d3015576e03=d944a50ebb28cefaf6f0784c77d4df98; _gat_gtag_UA_216532762_1=1; _ga_WTNMETJBE4=GS1.1.1668605285.1.1.1668606916.0.0.0; _ga=GA1.1.169033319.1668605285',
    'origin': 'https://www.toursguatemala.com',
    'referer': 'https://www.toursguatemala.com/index.php/packages/short-breaks/242-escape-to-nature',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = {
            'formSent': '1',
            'jform[name]': target,
            'jform[Phone]': target,
            'jform[email]': target,
            'jform[Adults Child]': '1',
            'jform[Child]': '1',
            'jform[Arrival]': '2022-11-25',
            'jform[Departure]': '2022-11-30',
            'jform[Total budget (estimate):]': '5000',
            'jform[Additional Comments]': self.get_text(),
            'jform[sendcopy]': '1',
            'moduleId': '91',
        }

        response = requests.post(url, cookies=cookies, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Thank you!'
    project_name = 'toursguatemala'
    promo_link = 'bit.ly/3EBsUkv'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)
