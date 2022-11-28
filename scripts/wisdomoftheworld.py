import requests

import module

headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarylsfZtEABELdUhlPi',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
url = 'https://www.wisdomoftheworld.com/offerings/wisdomcards/'
DATA = '------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n8392\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n7615\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\ntest\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_more_recipient"\r\n\r\ntest\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundarylsfZtEABELdUhlPi--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('softumwork@gmail.com', target).replace('test', self.get_text())
        response = requests.post(url, headers=headers, data=data.encode(), proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'successfully'
    project_name = 'wisdomoftheworld'
    # promo_link = 'bit.ly/3gvybRu'

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
