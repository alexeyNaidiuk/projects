import logging
from time import sleep

import requests

from module.data import get_turk_spinned_text, TurkeyTargetPool, ProjectController, Pool, \
    func_mapped_to_pool_concurrently, DeutcheProxyPool

PROM_LINK = 'bit.ly/3LIutyZ'
PROJECT_NAME = 'firenzesaude'
target_pool: Pool = TurkeyTargetPool()
PROXY_POOL: Pool = DeutcheProxyPool()
project: ProjectController = ProjectController(PROJECT_NAME, PROM_LINK)
logger = logging.getLogger(PROJECT_NAME)
logging.basicConfig(format=f'%(name)s {PROM_LINK} %(asctime)s: %(message)s')
logger.setLevel(logging.INFO)


class Spam:
    success_message = 'sucesso'

    def post(self, proxies, target, text):
        cookies = {
            '_ga': 'GA1.3.1233387358.1664182734',
            '_gid': 'GA1.3.534309537.1664182734',
            '_gat_gtag_UA_114453131_1': '1',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Origin': 'http://firenzesaude.com.br',
            'Referer': 'http://firenzesaude.com.br/contato.php',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }

        data = {
            'nomeremetente': text,
            'emailremetente': target,
            'telefone': '1212',
            'assunto2': text,
            'mensagem': text,
        }

        response = requests.post('http://firenzesaude.com.br/envia-contato.php', cookies=cookies, headers=headers,
                                 data=data, verify=False, proxies=proxies)
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
