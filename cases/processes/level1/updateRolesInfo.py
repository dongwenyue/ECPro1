# -*- coding: utf-8 -*-

from ..._importers import *


class updateRolesInfo(TestCase):
    @setup
    def __init__(self, caseid, methodName):
        TestCase.__init__(self, caseid, methodName)

    def updateRolesInfo(self):
        role_id = self.case['role_id']

        name = self.case['name']

        res = ECPro.updateRolesInfo(name, role_id)
        INFO(res)
        self.assertEqual('SUCCESS', res['message'], '修改角色信息')
