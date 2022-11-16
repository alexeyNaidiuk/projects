import requests

from module.spam_abstraction import Spam

cookies = {
    '131301c35f639b38185fdb9890d1259c': '3cb610d423bf045914221785ee26f6fc',
    'sj_preschool_tpl': 'sj_preschool',
    '_gcl_au': '1.1.213421845.1664892531',
    '__ctmid': '633c3e5e000617db1d790e68',
    '_ga': 'GA1.1.1677966572.1664892532',
    '_clck': '1rud6ab|1|f5g|0',
    'b72dd514516a6f8ec6e9ac444173b904': 'en-GB',
    '_ga_B1W209WL75': 'GS1.1.1664959629.4.1.1664959811.41.0.0',
    '_uetsid': '1338f31043ee11edbc3323a2b43d3515',
    '_uetvid': '13391b9043ee11edbf187b0e9c8730ff',
    '_clsk': 'w2q7um|1664959811489|4|1|h.clarity.ms/collect',
}
headers = {
    'authority': 'lilvillage.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://lilvillage.com',
    'referer': 'https://lilvillage.com/index.php/contact-lilvillage',
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
    'contact_ajax': '2493461664959789',
    'ctajax_modid': '639',
}
url = 'https://lilvillage.com/index.php/contact-lilvillage'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = {
            'name': 'text',
            'email': target,
            'message': self.get_text(),
            'subject': 'text',
            'date': '06/10/2022',
            'send_copy': '1',
            'task': 'sendmail',
            'ctajax_modid': '639',
        }
        response = requests.post(url, params=params, cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = '{"status":1,"message":"Your email has been sent."}'
    project_name = 'lilvillagee'
    promo_link = 'bit.ly/3NV9een'
    spam = ConcreteSpam(promo_link=promo_link, project_name=project_name, success_message=success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently(1)
