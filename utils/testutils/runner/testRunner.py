# -*- coding: utf-8 -*-

import platform, sys
from ...dbutils.sqlite_dao import CasesSqliteDao
from ...stringIO.logger.testlogger import *
from ...converter.encoding import isUnicode
from ...outpututils.resultout import OUT_PDF, OUT
from .. import unittest

separator = '--------------------------------------------------------------------------------'


class TestCase(unittest.TestCase):
    _class_cleanups = []

    def __init__(self, caseid, method_name, lvl='1'):
        unittest.TestCase.__init__(self, method_name)
        self.case_id = caseid
        self.case_name = method_name
        self.case_db = CasesSqliteDao()
        self.lvl = lvl

    @classmethod
    def doClassCleanups(cls):
        """Execute all class cleanup functions. Normally called for you after
        tearDownClass."""
        cls.tearDown_exceptions = []
        while cls._class_cleanups:
            function, args, kwargs = cls._class_cleanups.pop()
            try:
                function(*args, **kwargs)
            except Exception as exc:
                cls.tearDown_exceptions.append(sys.exc_info())

    def setUp(self):
        self.case = self.case_db.get_data_by_id(self.case_name, self.case_id, self.lvl)
        self.case_decription = self.case['description']
        INFO(separator)
        INFO('接口名称:    %s' % self.case_name)
        INFO('用例编号:    %s' % self.case_id)
        INFO('用例描述:    %s' % self.case_decription)
        INFO(separator)

    def tearDown(self):
        INFO(separator + '\n')
        self._testMethodDoc = self.case_decription

    def get_pdf_path(self):
        return OUT_PDF('%s-cases-%s' % (self.case_name, self.case_id))

    def get_out_path(self, suffix=None):
        return OUT('%s-cases-%s' % (self.case_name, self.case_id), suffix)

    def assertEqual(self, first, second, msg=None):
        try:
            if len(str(second)) > 100:
                msgerror = '用例 %s case:%s  在进行【 %s】 操作时失败\n EXPECT = %s\n ACTUAL = %s\n用例描述: %s' % \
                           (self.case_name, self.case_id, msg, str(first)[:90], str(second)[:90], self.case_decription)
            else:
                msgerror = '用例 %s case:%s  在进行【 %s】 操作时失败\n EXPECT = %s\n ACTUAL = %s\n用例描述: %s' % \
                           (self.case_name, self.case_id, msg, str(first), str(second), self.case_decription)
            self.fail(msgerror)
        except:
            if len(str(second)) > 100:
                msgerror = '进行【 %s】 操作时失败\n EXPECT = %s\n ACTUAL = %s\n用例描述: %s' % \
                           (msg, str(first)[:90], str(second)[:90], self.case_decription)
            else:
                msgerror = '进行【 %s】 操作时失败\n EXPECT = %s\n ACTUAL = %s\n用例描述: %s' % \
                           (msg, str(first), str(second), self.case_decription)
        try:
            unittest.TestCase.assertEqual(self, first, second)
            if msg:
                if len(str(second)) > 100:
                    INFO('%s EXPECT = %s ..... %s' % (msg, str(first)[:90], str(first)[-10:]))
                    INFO('%s ACTUAL = %s ..... %s' % (msg, str(second)[:90], str(first)[-10:]))
                else:
                    INFO('%s EXPECT = %s ' % (msg, str(first)))
                    INFO('%s ACTUAL = %s ' % (msg, str(second)))
            else:
                if len(str(second)) > 100:
                    INFO('EXPECT = %s ..... %s' % (str(first)[:90], str(first)[-10:]))
                    INFO('ACTUAL = %s ..... %s' % (str(second)[:90], str(first)[-10:]))
                else:
                    INFO('EXPECT = %s ' % (str(first)))
                    INFO('ACTUAL = %s ' % (str(second)))
        except:
            self.fail(msgerror)

    def fail(self, msg):
        if not isUnicode(msg): msg = msg.decode()
        unittest.TestCase.fail(self, msg=msg)
