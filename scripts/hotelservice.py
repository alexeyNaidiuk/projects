import requests

import module

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
url = 'https://hotelservice.spb.ru/contact-us/'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        text = self.get_text()
        data = {
            'zn_form_field_1_0': 'consult',
            'zn_form_field_1_1': text,
            'zn_form_field_1_2': '+7965965965',
            'zn_form_field_email1_3': target,
            'zn_form_field_1_4': target,
            'zn_form_field_1_5': target,
            'zn_form_field_1_6': target,
            'zn_form_field_1_7': target,
            'zn_form_field__152_1_8': 'true',
            'zn_pb_form_submit_1': '1',
            'send_me_copy_eluidb2441ab1': 'true',
        }
        response = requests.post(url, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    project_name = 'hotelservice'
    success_message = 'Спасибо'

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
