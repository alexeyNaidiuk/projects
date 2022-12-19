from unittest import TestCase

from module.captcha_solvers import CapMonsterRecaptcha2Solver


class TestCapMonsterRecaptcha2solver(TestCase):

    def test_solving(self):
        solver = CapMonsterRecaptcha2Solver()

        googlesitekey = '6Lf42XIaAAAAAEMuMBvgiHJYfEzMOBIR792J26zd'
        pageurl = 'http://flamel.eu/contact/'
        result = solver.solve(googlekey=googlesitekey, pageurl=pageurl)

        self.assertNotEqual(result, None)
