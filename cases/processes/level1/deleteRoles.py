# -*- coding: utf-8 -*-

from ..._importers import *


class deleteRoles(TestCase):
    @setup
    def __init__(self, caseid, methodName):
        TestCase.__init__(self, caseid, methodName)

    def deleteRoles(self):
        role_id = self.case['role_id']

        res = ECPro.deleteRoles(role_id)
        print(res)
        self.assertEqual('SUCCESS', res['message'], '删除角色')
