import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            'nrid': '4e0dee3253be8858',
            'd5e3c24b6379010083a67d3015576e03': 'c41d913c448830304e67d479e789418d',
            '_gid': 'GA1.2.1751152354.1665142087',
            '_ga_WTNMETJBE4': 'GS1.1.1665142086.3.1.1665142189.0.0.0',
            '_ga': 'GA1.2.1865995636.1663161567',
            '_gat_gtag_UA_216532762_1': '1',
        }

        headers = {
            'authority': 'www.toursguatemala.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'nrid=4e0dee3253be8858; d5e3c24b6379010083a67d3015576e03=c41d913c448830304e67d479e789418d; _gid=GA1.2.1751152354.1665142087; _ga_WTNMETJBE4=GS1.1.1665142086.3.1.1665142189.0.0.0; _ga=GA1.2.1865995636.1663161567; _gat_gtag_UA_216532762_1=1',
            'origin': 'https://www.toursguatemala.com',
            'referer': 'https://www.toursguatemala.com/index.php/day-tour/from-flores/133-tikal-sunset',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }

        data = {
            'formSent': '1',
            'jform[name]': text,
            'jform[Phone]': text,
            'jform[email]': target,
            'jform[Adults Child]': '0',
            'jform[Child]': '',
            'jform[Arrival]': '2022-10-08',
            'jform[Departure]': '2022-10-15',
            'jform[Total budget (estimate):]': '2500',
            'jform[Additional Comments]': text,
            'jform[sendcopy]': '1',
            'moduleId': '91',
        }

        response = requests.post('https://www.toursguatemala.com/index.php/day-tour/from-flores/133-tikal-sunset',
                                 cookies=cookies, headers=headers, data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Thank you!'
    project_name = 'toursguatemala'
    promo_link = 'bit.ly/3RKfki3'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
