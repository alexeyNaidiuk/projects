import logging
from time import sleep

import requests

from module.data import get_turk_spinned_text, TurkeyTargetPool, ProjectController, Pool, \
    func_mapped_to_pool_concurrently, DeutcheProxyPool

PROM_LINK = 'bit.ly/3dQgx9A'
PROJECT_NAME = 'happytsuuhan'
target_pool: Pool = TurkeyTargetPool()
PROXY_POOL: Pool = DeutcheProxyPool()
project: ProjectController = ProjectController(PROJECT_NAME, PROM_LINK)
logger = logging.getLogger(PROJECT_NAME)
logging.basicConfig(format=f'%(name)s {PROM_LINK} %(asctime)s: %(message)s')
logger.setLevel(logging.INFO)


class Spam:
    success_message = 'mail_sent'

    def post(self, proxies, target, text):
        cookies = {
            '_ga': 'GA1.2.1976763022.1664182405',
            '_gid': 'GA1.2.206760749.1664182405',
            '_gat_gtag_UA_66439696_1': '1',
        }

        headers = {
            'authority': 'happytsuuhan.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryONlDU1Lq8mWTEx8U',
            # Requests sorts cookies= alphabetically
            # 'cookie': '_ga=GA1.2.1976763022.1664182405; _gid=GA1.2.206760749.1664182405; _gat_gtag_UA_66439696_1=1',
            'origin': 'https://happytsuuhan.com',
            'referer': 'https://happytsuuhan.com/contact/',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = '------WebKitFormBoundaryONlDU1Lq8mWTEx8U\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n14\r\n------WebKitFormBoundaryONlDU1Lq8mWTEx8U\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.3.2\r\n------WebKitFormBoundaryONlDU1Lq8mWTEx8U\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nja\r\n------WebKitFormBoundaryONlDU1Lq8mWTEx8U\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f14-p12-o1\r\n------WebKitFormBoundaryONlDU1Lq8mWTEx8U\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n12\r\n------WebKitFormBoundaryONlDU1Lq8mWTEx8U\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundaryONlDU1Lq8mWTEx8U\r\nContent-Disposition: form-data; name="your-name"\r\n\r\n%(name)s\r\n------WebKitFormBoundaryONlDU1Lq8mWTEx8U\r\nContent-Disposition: form-data; name="your-email"\r\n\r\n%(target)s\r\n------WebKitFormBoundaryONlDU1Lq8mWTEx8U\r\nContent-Disposition: form-data; name="tel"\r\n\r\n1212\r\n------WebKitFormBoundaryONlDU1Lq8mWTEx8U\r\nContent-Disposition: form-data; name="your-message"\r\n\r\n%(text)s\r\n------WebKitFormBoundaryONlDU1Lq8mWTEx8U--\r\n' % {
            'target': target, 'text': text, 'name': 'text'}

        response = requests.post('https://happytsuuhan.com/wp-json/contact-form-7/v1/contact-forms/14/feedback',
                                 cookies=cookies, headers=headers, data=data, proxies=proxies)
        return response

    def try_to_post(self, text, target) -> str:
        content = None
        while not content:
            proxy = PROXY_POOL.get_unique()
            proxy = {'http': proxy, 'https': proxy}
            try:
                response = self.post(text=text, target=target, proxies=proxy)
                content = response.content.decode()
            except Exception as e:
                logger.error(e)
        return content

    def main(self, target='softumwork1@gmail.com'):
        if not project.status():
            logger.info('sleeping')
            sleep(120)
            return False
        target: str = target.encode().decode('latin-1')
        text: str = get_turk_spinned_text(PROM_LINK, with_stickers=True, decoded=True)
        content: str = self.try_to_post(text=text, target=target)
        result = self.success_message in content
        logger.info(f'{result} {target}')
        if result:
            project.send_good_status()
            project.send_count(1)
        else:
            project.send_bad_status()


if __name__ == '__main__':
    Spam().main()
    func_mapped_to_pool_concurrently(Spam().main, pool=target_pool, threads_amount=50)
