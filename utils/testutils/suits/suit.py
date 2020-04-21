# -*- coding: utf-8 -*-

from .. import unittest
from ...configures.paths import *
from ...dbutils.sqlite_dao import CasesSqliteDao
from ...stringIO.logger.testlogger import *


class BjcaSuits(unittest.TestSuite):

    def __init__(self, tests=()):

        unittest.TestSuite.__init__(self, tests)

        self._suits_dic = {}

        self._sqlite_cases = CasesSqliteDao()

        self._get_suits_from_dir()

    def loader_all(self):
        for class_name in self._suits_dic.keys():
            suite = self._suits_dic[class_name]
            for caseid in suite['cases']:
                self.addTest(suite['class'](int(caseid), class_name))

    def loader_by_id(self, caseid):
        class_name = caseid[0: caseid.find('_')]
        if class_name in self._suits_dic.keys():
            suite = self._suits_dic[class_name]
        else:
            raise BaseException('case id: %s not found' % caseid)

        if not int(caseid[caseid.find('_case') + 5:]) in suite['cases']:
            ERROR('【case id %s 】not found in suite %s, skip' % (caseid[caseid.find('_case') + 5:], class_name))

        self.addTest(suite['class'](int(caseid[caseid.find('_case') + 5:]), class_name))

    def _get_suits_from_model(self, class_path):
        try:
            suit = {}
            # 其他产品请修改 processes
            class_name = class_path[len(CURRENTPATH) + 1:].replace('\\', '.')
            # 通过 __import__ 动态加载 models, 类似于 from cases.processes.mssm.cloudSealPdfSign import cloudSealPdfSign
            __import__(class_name)
            # 通过  eval 获取 目标类实例
            suit['class'] = eval('%s.%s' % (class_name, class_name[class_name.rfind('.') + 1:]))
            # 返回 目标类下 所有测试用例
            suit['cases'] = self._sqlite_cases.get_cases_ids(class_name[class_name.rfind('.') + 1:])

            return suit
        except Exception as e:
            ERROR('[SUIT] get suits from model :%s error: \n %s' % (
            class_path[len(CURRENTPATH) + 1:].replace('\\', '.'), e))
            raise BaseException('[SUIT] get suits from model :%s error: \n %s' % (
            class_path[len(CURRENTPATH) + 1:].replace('\\', '.'), e))

    def _get_suits_from_dir(self, path=CASEPATH):
        DEBUG('[SUIT] loading cases from dir : %s' % path)
        if not os.path.exists(path):
            ERROR('[SUIT] %s not exists' % path)
            raise BaseException('%s not exists' % path)
        objs = os.listdir(path)
        for _str_class in objs:
            if os.path.isdir(os.path.join(path, _str_class)): self._get_suits_from_dir(os.path.join(path, _str_class))
            if not _str_class.endswith('.py'): continue
            if _str_class.startswith('_'): continue
            suite = self._get_suits_from_model(os.path.join(path, _str_class.replace('.py', '')))
            self._suits_dic[_str_class.replace('.py', '')] = suite
