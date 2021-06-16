# -*- coding: utf-8 -*-

from ..._importers import *


class getMoreDetailsPage(TestCase):
    @setup
    def __init__(self, caseid, methodName):
        TestCase.__init__(self, caseid, methodName)

    def getOneDetailsPage(self):
        token = self.case['token']
        documen_id = self.case['documen_id']

        res = ECPro.getOneDetailsPage(token,documen_id)
        print(res)
        self.assertEqual(self.case['expect'][0], res['message'], '获取单条详情页')