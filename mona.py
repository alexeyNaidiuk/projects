import logging
from time import sleep

import requests

from module.data import get_turk_spinned_text, TurkeyTargetPool, ProjectController, Pool, \
    func_mapped_to_pool_concurrently, DeutcheProxyPool

PROM_LINK = 'bit.ly/3dLfCr8'
PROJECT_NAME = 'mona'
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
            '_ga': 'GA1.1.1925452155.1664180452',
            'quads_browser_width': '1920',
            '__gads': 'ID=b49fcf28c88f8331-22f240a22fce00ad:T=1664180429:RT=1664180429:S=ALNI_MYe0KdUmHUWmmYna7euIgjZ12sSWw',
            '__gpi': 'UID=00000b4ef51e0223:T=1664180429:RT=1664180429:S=ALNI_MYU1Ub4pwyg8nmvqUuQGtzxqm9QuA',
            '_ga_T8NDS45D95': 'GS1.1.1664180452.1.1.1664180526.0.0.0',
            'FCNEC': '%5B%5B%22AKsRol8dtA667mSxa__HaOZS0GfKPrhOSHvL1-vO-5Cj24RMjHfJ9q-nWFtwCA-Lpt-W2V_qmpxdTg8eWnB2jaHiSypgzl_pv7SSU8oXuuuSXdLb1FPnN5gr2udr4pZaIln8uR7FBA40Ud7RgvpBXHjXyxTfwkUmUA%3D%3D%22%5D%2Cnull%2C%5B%5D%5D',
        }

        headers = {
            'authority': 'www.dd-mona.com',
            'accept': 'application/json, */*;q=0.1',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarypEJKHlgHACfpHwFg',
            'origin': 'https://www.dd-mona.com',
            'referer': 'https://www.dd-mona.com/contact/',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }

        data = '------WebKitFormBoundarypEJKHlgHACfpHwFg\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n25\r\n------WebKitFormBoundarypEJKHlgHACfpHwFg\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.6.3\r\n------WebKitFormBoundarypEJKHlgHACfpHwFg\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nja\r\n------WebKitFormBoundarypEJKHlgHACfpHwFg\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f25-p26-o1\r\n------WebKitFormBoundarypEJKHlgHACfpHwFg\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n26\r\n------WebKitFormBoundarypEJKHlgHACfpHwFg\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n2bbba9d2187ae01400c245cf40436b53\r\n------WebKitFormBoundarypEJKHlgHACfpHwFg\r\nContent-Disposition: form-data; name="your-name"\r\n\r\n%(name)s\r\n------WebKitFormBoundarypEJKHlgHACfpHwFg\r\nContent-Disposition: form-data; name="your-email"\r\n\r\n%(target)s\r\n------WebKitFormBoundarypEJKHlgHACfpHwFg\r\nContent-Disposition: form-data; name="your-subject"\r\n\r\n%(subject)s\r\n------WebKitFormBoundarypEJKHlgHACfpHwFg\r\nContent-Disposition: form-data; name="your-message"\r\n\r\n%(body)s\r\n------WebKitFormBoundarypEJKHlgHACfpHwFg\r\nContent-Disposition: form-data; name="_wpcf7_ak_hp_textarea"\r\n\r\n\r\n------WebKitFormBoundarypEJKHlgHACfpHwFg\r\nContent-Disposition: form-data; name="_wpcf7_ak_js"\r\n\r\n1664180526731\r\n------WebKitFormBoundarypEJKHlgHACfpHwFg--\r\n' % {
            'subject': text, 'body': text, 'name': 'test', 'target': target}

        response = requests.post('https://www.dd-mona.com/wp-json/contact-form-7/v1/contact-forms/25/feedback',
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
    func_mapped_to_pool_concurrently(Spam.main, pool=target_pool, threads_amount=50)
