import requests

import module

url = 'https://workersrights.com/me-plus-three/'

headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryCj1CmkB9HeoczPXR',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
data = '------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_1.3"\r\n\r\ntest https://workersrights.com/me-plus-three/\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_1.6"\r\n\r\ntest https://workersrights.com/me-plus-three/\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_2"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_4.3"\r\n\r\ntest https://workersrights.com/me-plus-three/\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_5"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_8.3"\r\n\r\ntest https://workersrights.com/me-plus-three/\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_10"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_9.3"\r\n\r\ntest https://workersrights.com/me-plus-three/\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_11"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="is_submit_1"\r\n\r\n1\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n1\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="state_1"\r\n\r\nWyJbXSIsIjgxYWUzZTY0NmE4YjFiY2UyMWZlZjI2ZWZjNDVmMTM2Il0=\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="gform_target_page_number_1"\r\n\r\n0\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="gform_source_page_number_1"\r\n\r\n1\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        post_data = data.replace('softumwork@gmail.com', target).replace('test', self.get_text())
        response = requests.post(url, headers=headers, data=post_data.encode(),
                                 proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'THANK YOU'
    project_name = 'workersrights'
    # promo_link = 'bit.ly/3AQL7bo'

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
