# -*- coding: utf-8 -*-
"""
Author:yuqi
"""
import unittest

from BeautifulReport import BeautifulReport as bf
from utils.testutils.runner.testRunner import lens

if __name__ == '__main__':
    from utils.configures.paths import SET_SYSCONFIG

    SET_SYSCONFIG('betaSysConfig.ini')
    # SET_SYSCONFIG('abTestSysConfig.ini')
    # SET_SYSCONFIG('proSysConfig.ini')


    from cases.processes.level1.verify.verifyAttr import verifyAttr
    from cases.processes.level1.verify.verifyAttrVal import verifyAttrVal
    from cases.processes.level1.verify.verifyMergeAttr import verifyMergeAttr
    from cases.processes.level1.verify.verifyEmptyAttr import verifyEmptyAttr

    suite = unittest.TestSuite()
    #
    # for i in range(lens):
    #     suite.addTest(verifyAttr(1, "verifyAttr",int(i)))
    for i in range(lens):
        suite.addTest(verifyAttrVal(1, "verifyAttrVal", int(i)))

    # 属性值合并
    # for i in range(lens):
    #     suite.addTest(verifyMergeAttr(1, "verifyMergeAttr", int(i)))
    #
    # for i in range(lens):
    #     suite.addTest(verifyEmptyAttr(1, "verifyEmptyAttr",int(i)))

    run = bf(suite)
    run.report(filename='./result/test', description='testResult')
