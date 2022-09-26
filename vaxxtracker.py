import logging
from time import sleep

import requests

from module.data import get_turk_spinned_text, TurkeyTargetPool, ProjectController, Pool, \
    func_mapped_to_pool_concurrently, DeutcheProxyPool

PROM_LINK = 'bit.ly/3C4dsfx'
PROJECT_NAME = 'vaxxtracker'
target_pool: Pool = TurkeyTargetPool()
PROXY_POOL: Pool = DeutcheProxyPool()
project: ProjectController = ProjectController(PROJECT_NAME, PROM_LINK)
logger = logging.getLogger(PROJECT_NAME)
logging.basicConfig(format=f'%(name)s {PROM_LINK} %(asctime)s: %(message)s')
logger.setLevel(logging.INFO)


class Spam:

    def __call__(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def post(self, target: str, text: str, proxies: dict | None = None) -> requests.Response:
        headers = {
            'authority': 'vaxxtracker.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'origin': 'https://vaxxtracker.com',
            'referer': 'https://vaxxtracker.com/vaxContactUs.aspx?t=1',
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
        params = {
            't': '1',
        }
        data = {
            '__VIEWSTATE': '/wEPDwULLTIwMzI1Njc0NjEPZBYCAgMPZBYKAgEPDxYCHgdWaXNpYmxlaGRkAgMPDxYCHwBnZGQCBQ8PFgIfAGhkZAIHDw8WAh8AaGRkAhUPFgIeBFRleHRlZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUEY2tiMZxCchf8JfhkSlFLWKMMr31+0MuyiQYjETl4pl5egMDD',
            '__VIEWSTATEGENERATOR': 'C9A25C30',
            '__EVENTVALIDATION': '/wEdAAhNPW1UY8p/bLAYSnFFniZGozoJZpuXxkpOVJKRbHyuHkMHZh9ZuPBRie2vA/HfoRL57krzdrowy1YqiaDEjlkHEVY5u54TgWwyd97xcy3QirEfxNUtl86PXruMcj2GUlMYMEzNwxRA5nXVZ+7dFzCrPOaW1pQztoQA36D1w/+bXbC32883XWBVL4UFhGfCtlLa6lRRkexgCcMrpm0F3nB4',
            'txtName': text,
            'txtEmail': target,
            'txtPhone': text,
            'txtMessage': text,
            'txtHuman': '12',
            'ckb1': 'on',
            'btnSubmit': 'Send Email',
        }
        response = requests.post('https://vaxxtracker.com/vaxContactUs.aspx', params=params,
                                 headers=headers, data=data, proxies=proxies, timeout=10)
        return response


def try_to_post(text, target) -> str:
    content = None
    while not content:
        proxy = PROXY_POOL.get_unique()
        proxy = {'http': proxy, 'https': proxy}
        try:
            spam = Spam()
            response = spam(text=text, target=target, proxies=proxy)
            content = response.content.decode()
        except Exception as e:
            logger.error(e)
    return content


def main(target='softumwork1@gmail.com', success_statement='Thank You, your message has been sent.'):
    if not project.status():
        logger.debug('sleeping')
        sleep(120)
        return False
    target: str = target.encode().decode('latin-1')
    text: str = get_turk_spinned_text(PROM_LINK, with_stickers=True, decoded=False)
    content: str = try_to_post(text=text, target=target)
    result = success_statement in content
    logger.info(f'{result} {target}')
    if result:
        project.send_good_status()
        project.send_count(1)
    else:
        project.send_bad_status()


if __name__ == '__main__':
    main()
    func_mapped_to_pool_concurrently(main, pool=target_pool, threads_amount=1)
