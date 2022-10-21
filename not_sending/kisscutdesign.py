import string
import requests

from module import Spam

cookies = {
    '__utmc': '59974199',
    '__utmt': '1',
    '__utma': '59974199.1254038755.1666361095.1666361095.1666361310.2',
    '__utmz': '59974199.1666361310.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '__utmb': '59974199.4.10.1666361310',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryXeho5A1OZfSiASo3',
    'Origin': 'http://kisscutdesign.com',
    'Referer': 'http://kisscutdesign.com/contact/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}
url = 'http://kisscutdesign.com/contact/'
DATA = '------WebKitFormBoundaryXeho5A1OZfSiASo3\r\nContent-Disposition: form-data; name="input_1"\r\n\r\n$text\r\n------WebKitFormBoundaryXeho5A1OZfSiASo3\r\nContent-Disposition: form-data; name="input_2"\r\n\r\n$target\r\n------WebKitFormBoundaryXeho5A1OZfSiASo3\r\nContent-Disposition: form-data; name="input_3"\r\n\r\n$text \r\n------WebKitFormBoundaryXeho5A1OZfSiASo3\r\nContent-Disposition: form-data; name="is_submit_1"\r\n\r\n1\r\n------WebKitFormBoundaryXeho5A1OZfSiASo3\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n1\r\n------WebKitFormBoundaryXeho5A1OZfSiASo3\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n\r\n------WebKitFormBoundaryXeho5A1OZfSiASo3\r\nContent-Disposition: form-data; name="state_1"\r\n\r\nWyJbXSIsIjVhOWQ5NjBjYjBiYzM4OWM3Zjc1MTc5NmFjYjNiNGJjIl0=\r\n------WebKitFormBoundaryXeho5A1OZfSiASo3\r\nContent-Disposition: form-data; name="gform_target_page_number_1"\r\n\r\n0\r\n------WebKitFormBoundaryXeho5A1OZfSiASo3\r\nContent-Disposition: form-data; name="gform_source_page_number_1"\r\n\r\n1\r\n------WebKitFormBoundaryXeho5A1OZfSiASo3\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundaryXeho5A1OZfSiASo3--\r\n'


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        data = string.Template(DATA).substitute({'target': target, 'text': text}).encode().decode('latin-1')
        response = requests.post(url, cookies=cookies, headers=headers, data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Thanks for the note'
    project_name = 'kisscutdesign'
    promo_link = 'bit.ly/3VLCdou'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
