# -*- coding: utf-8 -*-

from ..._importers import *


class createPeriod(TestCase):
    # @setup
    def __init__(self, caseid, methodName):
        TestCase.__init__(self, caseid, methodName)

    def createPeriod(self):
        period = self.case['period']
        period_describe = self.case['period_describe']

        res = ECPro.createPeriod(token, period, period_describe)
        print(res)
        self.assertEqual(self.case['expect'][0], res['code'], '获取导出记录')
