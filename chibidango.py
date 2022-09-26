import logging
from time import sleep

import requests

from module.data import get_turk_spinned_text, TurkeyTargetPool, ProjectController, Pool, \
    func_mapped_to_pool_concurrently, DeutcheProxyPool

PROM_LINK = 'bit.ly/3ygaQZV'
PROJECT_NAME = 'chibidango'
target_pool: Pool = TurkeyTargetPool()
PROXY_POOL: Pool = DeutcheProxyPool()
project: ProjectController = ProjectController(PROJECT_NAME, PROM_LINK)
logger = logging.getLogger(PROJECT_NAME)
logging.basicConfig(format=f'%(name)s {PROM_LINK} %(asctime)s: %(message)s')
logger.setLevel(logging.INFO)


class Spam:
    success_message = 'ขอบคุณที่ติดต่อกับเรา'

    def post(self, proxies, target, text):

        cookies = {
            '_ga': 'GA1.2.1395900819.1664182151',
            '_gid': 'GA1.2.473635944.1664182151',
            '_gat': '1',
            '_gat_gtag_UA_139948818_1': '1',
            '__gads': 'ID=f519b9bbbf37773a-2261f3282bce00b9:T=1664182129:RT=1664182129:S=ALNI_Mayup35gwyuMtkHMlE98FbrZWENig',
            '__gpi': 'UID=00000b4f05412bce:T=1664182129:RT=1664182129:S=ALNI_MbqxdjTerIvltxMXIYxkcCH3LRUSQ',
        }

        headers = {
            'authority': 'chibidango.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'origin': 'https://chibidango.com',
            'referer': 'https://chibidango.com/contact-us/',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }

        data = {
            'contactName': text,
            'email': target,
            'comments': text,
            'submitted': 'true',
        }

        response = requests.post('https://chibidango.com/contact-us/', cookies=cookies, headers=headers, data=data
                                 , proxies=proxies)
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
        text: str = get_turk_spinned_text(PROM_LINK, with_stickers=False, decoded=False)
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
