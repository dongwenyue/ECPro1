# -*- coding: utf-8 -*-

import unittest

from BeautifulReport import BeautifulReport as bf

if __name__ == '__main__':
    from utils.configures.paths import SET_SYSCONFIG

    SET_SYSCONFIG('betaSysConfig.ini')
    # SET_SYSCONFIG('devSysConfig.ini')
    # SET_SYSCONFIG('proSysConfig.ini')

    from cases.processes.level1.updateRolesInfo import updateRolesInfo
    from cases.processes.level1.deleteRoles import deleteRoles

    suite = unittest.TestSuite()
    suite.addTest(updateRolesInfo(1, "updateRolesInfo"))
    suite.addTest(deleteRoles(1, "deleteRoles"))

    run = bf(suite)
    run.report(filename='./result/test', description='testResult')
