import requests

from module.spam_abstraction import Spam

url = 'https://nlcultural.com/garden-at-sainte-adresse-by-claude-monet-the-met-150/'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = {
            'wp_iec_img': '51460',
            'wp_iec_post': '51459',
            'wp_iec_unique_id': '0',
            'wp_iec_ajax_validated': '1',
            'wp_iec_action': 'process_from',
            'wp_iec_name': 'te',
            'wp_iec_email': target,
            'wp_iec_femail': target,
            'wp_iec_more_recipient': '',
            'wp_iec_message': self.get_text(),
            'wp_iec_scopy': '1',
        }

        response = requests.post(url, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'thankyou_redirect'
    project_name = 'nlcultural'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3XTP5KD'
    spam = ConcreteSpam(project_name, success_message, referal_project_name=project, promo_link=promo_link)
    res = spam.send_post()  # True
    if res:
        spam.run_concurrently()
