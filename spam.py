import requests

from module.link_shortner import LinkShortner
from module.pools import TargetServerFactory, ProxyServerFactory, Pool
from module.project_controller import ProjectController, ProjectServerControllerCached
from module.spam_abstraction import Spam
from module.texts import Text


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        ...


if __name__ == '__main__':
    project_name = 'newproject2'

    target_pool_name = 'mixru'
    proxy_pool_name = 'checked'
    target_lang = 'ru'
    success_message = ''

    project_controller: ProjectController = ProjectServerControllerCached(project_name=project_name)
    promo_link: str | None = project_controller.retrieve_attached_link()
    if not promo_link:
        link = f'https://referencemen.live/ktVmDV?c=0097xLek_pT9MBb54378f54e94879e&utm_campaign={target_pool_name}'
        shortened_link = LinkShortner.get_link(link)
        project_controller.prom_link = shortened_link
    project_controller.get_status()

    target_pool: Pool = TargetServerFactory.get_pool(factory_name=target_pool_name)
    proxy_pool: Pool = ProxyServerFactory.get_pool(factory_name=proxy_pool_name)
    text: Text = Text(text_lang=target_lang)

    spam = ConcreteSpam(project_controller, proxy_pool, target_pool, text, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
