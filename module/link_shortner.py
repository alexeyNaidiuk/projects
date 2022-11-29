import requests

from module.config import ZENNO_KEY


class LinkShortner:
    __url = 'https://zennotasks.com/automation/api.php'
    __key = ZENNO_KEY
    __referals = {
        'supercat': 'https://referencemen.live/ktVmDV?c=0098xLek_pT9MBd059d7cb95430c53',
        'luckybird': 'https://referencemen.live/ktVmDV?c=0097xLek_pT9MB5b4d7a1cbb052b1b',
        'allright': 'https://referencemen.live/ktVmDV?c=0114xLek_pT9MBc578b8a2b8d59856',
        'fortuneclock': 'https://referencemen.live/ktVmDV?c=0133xLek_pT9MB5ea167c052b0c66a'
    }

    @classmethod
    def get_link(cls, target_pool_name: str, referal_to_project: str) -> str:
        '''https://zennotasks.com/automation/api.php?key=softumXasHq1!&shurl=https://referencemen.live/ktVmDV?c=0097xLek_pT9MBb54378f54e94879e&utm_campaign=mixru'''
        project_link = cls.__referals[referal_to_project]

        if not referal_to_project:
            utm_campaign = target_pool_name
        else:
            utm_campaign = f'{target_pool_name}_{referal_to_project}'

        url = f'{project_link}&utm_campaign={utm_campaign}'
        params = {'key': cls.__key, 'shurl': url}
        response = requests.get(cls.__url, params=params)
        content = response.text
        return content
