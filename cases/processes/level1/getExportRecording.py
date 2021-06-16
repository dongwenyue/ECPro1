# -*- coding: utf-8 -*-

from ..._importers import *


class getExportRecording(TestCase):
    # @setup
    def __init__(self, caseid, methodName):
        TestCase.__init__(self, caseid, methodName)

    def getExportRecording(self):
        token = self.case['token']

        res = ECPro.getExportRecording(token)
        print(res)
        self.assertEqual(self.case['expect'][0], res['message'], '获取导出记录')