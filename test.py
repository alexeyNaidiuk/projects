import logging
from time import sleep

import requests

from module.data import get_turk_spinned_text, TurkeyTargetPool, WwmixProxyPool, ProjectController, SpamInterface, \
    ProxyPool, TargetPool

PROM_LINK = 'shortin.us/kCLjH'
PROJECT_NAME = 'test'

target_pool: TargetPool = TurkeyTargetPool()
proxy_pool: ProxyPool = WwmixProxyPool()

project: ProjectController = ProjectController(PROJECT_NAME, PROM_LINK)

logger = logging.getLogger(PROJECT_NAME)
logging.basicConfig(format=f'%(name)s {PROM_LINK} %(asctime)s: %(message)s')
logger.setLevel(logging.INFO)


class Spam(SpamInterface):
    ...


class SpamRunnerInterface:

    def __init__(self):
        self.target: str = target_pool.get_unique().encode().decode('latin-1')
        self.text: str = get_turk_spinned_text(PROM_LINK, with_stickers=True, decoded=False)

    def try_to_post(self):
        ...


def try_to_post(text, target) -> str:
    content: str = ''
    while not content:
        spam: SpamInterface = Spam(proxy_pool=proxy_pool)
        try:
            response: requests.Response = spam.post(text=text, target=target)
            content: str = response.content.decode()
        except Exception as e:
            logger.error(e)
    return content


def main(spamrunner: SpamRunnerInterface, success_message: str = ''):
    if not project.status():
        sleep(120)
        return

    result_content = spamrunner.try_to_post()
    if success_message in result_content:
        project.send_good_status()
        project.send_count(1)
    else:
        project.send_bad_status()


if __name__ == '__main__':
    main(SpamRunnerInterface(), 'success')
