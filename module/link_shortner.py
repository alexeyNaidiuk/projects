import requests

from module.config import ZENNO_KEY


class LinkShortner:
    __url = 'https://zennotasks.com/automation/api.php'
    __key = ZENNO_KEY

    @classmethod
    def get_link(cls, target_pool_name: str) -> str:

        '''https://zennotasks.com/automation/api.php?key=softumXasHq1!&shurl=https://referencemen.live/ktVmDV?c=0097xLek_pT9MBb54378f54e94879e&utm_campaign=mixru'''

        url = f'https://referencemen.live/ktVmDV?c=0097xLek_pT9MBb54378f54e94879e&utm_campaign={target_pool_name}'
        params = {'key': cls.__key, 'shurl': url}
        response = requests.get(cls.__url, params=params)
        content = response.text
        return content
