import requests

from module import Spam

request_json = {
    "url": None,
    "method": "post",
    "cookies": None,
    "headers": None,
    "data": None
}


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        response = requests.request(
            method=request_json['method'].upper(),
            url=request_json.get('url'),
            cookies=request_json.get('cookies'),
            headers=request_json.get('headers'),
            data=request_json.get('data'),
            proxies=proxies
        )
        return response


if __name__ == '__main__':
    success_message = ''
    project_name = 'project_name'
    promo_link = 'bit.ly/3CEv81r'
    spam = ConcreteSpam(promo_link, project_name, success_message, logging_level='debug')
    res = spam.send_post()
    if res:
        spam.run_concurrently()
