# -*- coding: utf-8 -*-

'''
Created on 2018年6月7日

@author: wangsiyu
'''
import sys
from unittest.result import failfast

from utils.runner.BSTestRunner import _TestResult
from utils.runner.xmlrunner.result import _XMLTestResult


class BJCATestResult(_XMLTestResult, _TestResult):
    """
    A test result class that can express test results in a XML report.

    Used by XMLTestRunner.
    """

    def __init__(self, stream=sys.stderr, descriptions=1, verbosity=1,
                 elapsed_times=True, properties=None, infoclass=None):
        _TestResult.__init__(self, 0)
        _XMLTestResult.__init__(self, stream, descriptions, verbosity, elapsed_times, properties, infoclass)

    def startTest(self, test):
        _XMLTestResult.startTest(self, test)

    #         _TestResult.startTest(self, test)

    def stopTest(self, test):
        _XMLTestResult.stopTest(self, test)
        _TestResult.stopTest(self, test)

    def addSuccess(self, test):
        _XMLTestResult.addSuccess(self, test)
        _TestResult.addSuccess(self, test)

    @failfast
    def addFailure(self, test, err):
        _XMLTestResult.addFailure(self, test, err)
        _TestResult.addFailure(self, test, err)

    @failfast
    def addError(self, test, err):
        _XMLTestResult.addError(self, test, err)
        _TestResult.addError(self, test, err)
