import requests

import module

headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryAse2uhCm5tDf76Nz',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
url = 'https://kiddosride.com/wp-json/contact-form-7/v1/contact-forms/141/feedback'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = '------WebKitFormBoundaryAse2uhCm5tDf76Nz\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n141\r\n------WebKitFormBoundaryAse2uhCm5tDf76Nz\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.6.4\r\n------WebKitFormBoundaryAse2uhCm5tDf76Nz\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nen_US\r\n------WebKitFormBoundaryAse2uhCm5tDf76Nz\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f141-p17-o1\r\n------WebKitFormBoundaryAse2uhCm5tDf76Nz\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n17\r\n------WebKitFormBoundaryAse2uhCm5tDf76Nz\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundaryAse2uhCm5tDf76Nz\r\nContent-Disposition: form-data; name="your-name"\r\n\r\ntest\r\n------WebKitFormBoundaryAse2uhCm5tDf76Nz\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryAse2uhCm5tDf76Nz\r\nContent-Disposition: form-data; name="your-subject"\r\n\r\ntest\r\n------WebKitFormBoundaryAse2uhCm5tDf76Nz\r\nContent-Disposition: form-data; name="your-message"\r\n\r\ntest\r\n------WebKitFormBoundaryAse2uhCm5tDf76Nz--\r\n'
        data = data.replace('test', self.get_text().encode().decode('latin-1'))
        data = data.replace('softumwork@gmail.com', target)

        proxies = self.get_proxies()
        response = requests.post(url, headers=headers, data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Thank you for your message'
    project_name = 'kiddosride'

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
