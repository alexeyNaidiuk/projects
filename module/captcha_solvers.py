import logging
from time import sleep

import requests

from module.config import CAPMONSTER_HOST


class Solver:

    def solve(self, *args, **kwargs) -> str:
        ...


class CapMonsterSolver(Solver):

    def solve(self, googlekey: str, pageurl: str, tine_for_solving: int = 20) -> str:
        ...


class CapMonsterRecaptcha3Solver(CapMonsterSolver):

    def solve(self, googlekey: str, pageurl: str, tine_for_solving: int = 20) -> str:
        ...


class CapMonsterRecaptcha2Solver(CapMonsterSolver):

    def _check_request(self, request_id: str) -> requests.Response:
        params = {
            'action': 'get',
            'id': request_id
        }
        response = requests.get(f'http://{CAPMONSTER_HOST}/res.php', params=params)
        return response

    def _send_request(self, googlekey: str, pageurl: str) -> requests.Response:
        params = {
            'method': 'userrecaptcha',
            'soft_id': '19',
            'version': 'v2',
            'pageurl': pageurl,
            'googlekey': googlekey
        }
        response = requests.get(f'http://{CAPMONSTER_HOST}/in.php', params=params)
        logging.debug(f'_send_request {response.text}')
        return response

    def _await_for_result(self, request_id: str, time_limit: int) -> str | None:
        result = None
        for _ in range(time_limit):
            result = self._check_request(request_id).text
            logging.debug(result)
            if result in ['CAPCHA_NOT_READY']:
                sleep(1)
                continue
        logging.debug(result)
        return result

    def solve(self, googlekey: str, pageurl: str, time_limit: int = 60) -> str | None:
        status, request_id = self._send_request(googlekey=googlekey, pageurl=pageurl).text.split('|')
        if 'OK' not in status:
            logging.error(f'{status} {request_id}')
            return None
        result = self._await_for_result(request_id, time_limit=time_limit)
        return result
