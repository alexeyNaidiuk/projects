from unittest import TestCase

from module.captcha_solvers import CapMonsterRecaptcha2Solver


class TestCapMonsterRecaptcha2solver(TestCase):

    def test_solving(self):
        solver = CapMonsterRecaptcha2Solver()

        googlesitekey = '6LdYakAUAAAAAI4ggmWblPh_VXde3pRfmlflPFb2'
        pageurl = 'https://www.enzolifesciences.com/email-to-friend/'
        result = solver.solve(googlekey=googlesitekey, pageurl=pageurl)

        self.assertNotEqual(result, None)
