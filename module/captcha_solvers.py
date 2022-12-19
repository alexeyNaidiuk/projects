from time import sleep

import requests

from module.config import CAPMONSTER_HOST


class Solver:

    def solve(self, *args, **kwargs) -> str:
        ...


class CapMonsterSolver(Solver):

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
        return response

    def _await_for_result(self, request_id: str, time_limit: int) -> str:
        result = None
        c = 0
        while result is None and c < time_limit * 2:
            result = self._check_request(request_id).text

            c += 1
            sleep(.5)
        return result

    def solve(self, googlekey: str, pageurl: str, time_limit: int = 30) -> str | None:
        result = None
        status, request_id = self._send_request(googlekey=googlekey, pageurl=pageurl).text.split('|')
        if 'OK' not in status:
            raise Exception(status)
        result = self._await_for_result(request_id, time_limit=time_limit)

        return result


class CapMonsterRecaptcha3Solver(CapMonsterSolver):

    def solve(self, googlekey: str, pageurl: str, tine_for_solving: int = 20) -> str:
        ...
