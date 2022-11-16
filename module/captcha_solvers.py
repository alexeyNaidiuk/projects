import requests

from config import CAPMONSTER_HOST


class Solver:

    def solve(self, *args, **kwargs) -> str:
        ...


class CapMonsterSolver(Solver):
    __url = CAPMONSTER_HOST

    def solve(self, sitekey: str, url: str, tine_for_solving: int = 20) -> str:
        ...


class CapMonsterRecaptcha2Solver(CapMonsterSolver):

    def solve(self, sitekey: str, url: str, tine_for_solving: int = 20) -> str:
        ...


class CapMonsterRecaptcha3Solver(CapMonsterSolver):

    def solve(self, sitekey: str, url: str, tine_for_solving: int = 20) -> str:
        ...
