import logging
from concurrent.futures import ThreadPoolExecutor

import bs4
import requests

from module.data import TurkeyTargetPool, WwmixProxyPool, Pool, \
    SpamInterface, get_turk_spinned_text, ProjectController

PROM_LINK = 'shortin.us/r7DXe'
PROJECT_NAME = 'gersophile'
project: ProjectController = ProjectController(PROJECT_NAME, PROM_LINK)
target_pool: Pool = TurkeyTargetPool()
PROXY_POOL: Pool = WwmixProxyPool()
use_proxy: bool = False
logger = logging.getLogger('logger')
logging.basicConfig(format=f'%(name)s {PROM_LINK} %(asctime)s: %(message)s')
logger.setLevel(logging.INFO)


class Spam(SpamInterface):

    def get(self, *args, **kwargs) -> requests.Response:
        cookies = {
            'pwg_id': 'ju3celg03jdllcadu0t0raamt3',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Referer': 'https://gersophile.piwigo.com/index?/contact/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        response = requests.get('https://gersophile.piwigo.com/index?/contact/', cookies=cookies, headers=headers,
                                proxies=self.proxies)
        return response

    def post(self, token, target, text) -> requests.Response:  # fixme
        cookies = {
            'pwg_id': 'ju3celg03jdllcadu0t0raamt3',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': 'pwg_id=ju3celg03jdllcadu0t0raamt3',
            'Origin': 'https://gersophile.piwigo.com',
            'Referer': 'https://gersophile.piwigo.com/index?/contact/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'author': text,
            'email': target,
            'subject': 'test',
            'content': text,
            'send_mail': 'Send',
            'key': token,
        }

        response = requests.post('https://gersophile.piwigo.com/index?/contact/', cookies=cookies, headers=headers,
                                 data=data, proxies=self.proxies)
        return response


def spam(target) -> bool:  # fixme
    target: str = target.encode().decode('latin-1')
    text: str = get_turk_spinned_text(PROM_LINK, with_stickers=True, decoded=False)
    result: str = try_to_post(text=text, target=target)
    return 'E-mail sent successfully' in result


def try_to_post(text, target) -> str:  # fixme
    content = None
    spam: SpamInterface = Spam()
    while not content:
        if use_proxy:
            proxy = next(PROXY_POOL)
            proxy = {'http': proxy, 'https': proxy}
        else:
            proxy = None
        spam.proxies = proxy
        get_resp = spam.get()
        soup = bs4.BeautifulSoup(get_resp.content.decode(), 'lxml')
        token = soup.find('form', {'action': 'https://gersophile.piwigo.com/index?/contact/'})
        token = token.find('input', {'type': 'hidden'})['value']
        post_resp = spam.post(token, text=text, target=target)
        content = post_resp.content.decode()
    return content


def main(target: str = 'softumwork@gmail.com'):
    # if not project.status():
    #     logger.debug('sleeping')
    #     sleep(120)
    #     return False
    result: bool = spam(target=target)
    logger.info(f'{result} {target}')
    # if result:
    #     project.send_good_status()
    #     project.send_count(1)
    # else:
    #     logger.error(f'{result} {target}')
    #     project.send_bad_status()


def threaded_main():
    with ThreadPoolExecutor(50) as executor:
        executor.map(main, [target for target in target_pool])


if __name__ == '__main__':
    main()
