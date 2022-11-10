import requests

from module.spam_abstraction import Spam

url = 'https://www.coala-travel.com/wp-admin/admin-ajax.php'

cookies = {
    'PHPSESSID': '165277c1aa1cd384346cc026371dc5ca',
    'PH_HPXY_CHECK': 's1',
    'wassup_screen_resc535371f2ba126540b25902ff70ede42': '1920%20x%201080',
    'wassupc535371f2ba126540b25902ff70ede42': 'MGJfNjkzMGM4YjAxMzFhMDFmMDY4ZTg3YzJjOGI1MDQ3NTQjIzE2NjYyNjc3NDEjIzE5MjAgeCAxMDgwIyMxOTQuMTgzLjE2OC4yIyMxOTQuMTgzLjE2OC4yIyM%253D',
}
headers = {
    'authority': 'www.coala-travel.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.coala-travel.com',
    'referer': 'https://www.coala-travel.com/mirjana1/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
params = {
    'action': 'pwebcontact_sendEmail',
}


class ConcreteSpam(Spam):

    def post(self, text, target) -> requests.Response:
        data = {
            'mid': '1',
            'format': 'json',
            'ignoreMessages': 'true',
            'fields[name]': text,
            'fields[email]': target,
            'fields[field_6]': '21-10-2022',
            'fields[field_7]': '23-10-2022',
            'fields[numberofadultpersons]': '1',
            'fields[mobilephone]': '21212',
            'fields[message]': text,
            'fields[agreetotermsconditions]': '1',
            'fields[igivemyconsentforcoalatraveltousemypersonaldata]': '1',
            'copy': '1',
            '87fcf9596c': '1',
            'title': '# Apartments Okrug Donji free wireless internet air condition |',
            'url': 'https://www.coala-travel.com/mirjana1/',
            'screen_resolution': '1920x1080',
        }
        response = requests.post(url, params=params, cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Thanks'
    project_name = 'coala'
    promo_link = 'bit.ly/3WN3O9s'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)
