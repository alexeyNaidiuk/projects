import requests

from module import Spam

url = 'http://www.safestoragesolutions.com/wp-admin/admin-ajax.php'

cookies = {
    'PHPSESSID': 'dnrokmnhoi61j84k6sbel69bni',
    '_tccl_visitor': '9b9e7760-60c4-5610-a87c-2e1219b0f844',
    'mb-views': '[%221page27BshxeGBV%22%2C%226page27N7n_XhzE%22%2C%227page27Bi48oilK%22%2C%228page27hEz076md%22]',
    '_tccl_visit': 'e6decf82-e068-5908-8872-31cb21378ae7',
}
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://www.safestoragesolutions.com',
    'Referer': 'http://www.safestoragesolutions.com/request-a-quote/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
params = {
    'action': 'pwebcontact_sendEmail',
}
data = {
    'mid': '2',
    'format': 'json',
    'ignoreMessages': 'true',
    'fields[name]': 'name',
    'fields[phone]': '12121212',
    'fields[email]': 'softumwork@gmail.com',
    'fields[pickone]': '5x5',
    'fields[startdate]': '30-10-2022',
    'fields[message]': 'test',
    'copy': '1',
    '3b78e5b3d8': '1',
    'title': 'Request a Quote – Safe Storage Solutions',
    'url': 'http://www.safestoragesolutions.com/request-a-quote/',
    'screen_resolution': '1920x1080',
}


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        data['fields[email]'] = target
        data['fields[message]'] = text
        response = requests.post(url, params=params, cookies=cookies, headers=headers, data=data, verify=False,
                                 proxies=proxies)

        return response


if __name__ == '__main__':
    succ_msg = 'Thank you for your interest'
    project_name = 'safestoragesolutions'
    promo_link = 'bit.ly/3gtvVtK'
    spam = ConcreteSpam(promo_link, project_name, succ_msg)
    res = spam.send_post()
    if res:
        spam.run_concurrently(7)
