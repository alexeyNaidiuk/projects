from unittest import TestCase

from module.captcha_solvers import CapMonsterRecaptcha2Solver


class TestCapMonsterRecaptcha2solver(TestCase):

    def test_solving(self):
        solver = CapMonsterRecaptcha2Solver()

        googlesitekey = ' 6LfCnhwTAAAAAONEzvCPHkac-biXc_1zUPqxsrX3'
        pageurl = 'https://mountainexcursion.is/contact-us.html'
        result = solver.solve(googlekey=googlesitekey, pageurl=pageurl)  # error recaptcha timeout

        self.assertNotEqual(result, None)
