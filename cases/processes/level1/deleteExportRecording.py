# -*- coding: utf-8 -*-

from ..._importers import *


class deleteExportRecording(TestCase):
    @setup
    def __init__(self, caseid, methodName):
        TestCase.__init__(self, caseid, methodName)

    def deleteExportRecording(self):
        record_id = self.case['record_id']
        token = self.case['token']

        res = ECPro.deleteExportRecording(record_id,token)
        print(res)
        # self.assertEqual('SUCCESS', res['message'], '删除角色')
