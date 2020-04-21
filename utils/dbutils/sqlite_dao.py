# -*- coding: utf-8 -*-
'''
Created on 2019年2月27日

@author: wsy
'''
import os

from utils.configures.paths import TEST_DATA_DIR
from utils.dbutils.sqlite_driver import CasesSqliteDriver


class CasesSqliteDao(object):

    def __init__(self):
        global sqlite
        sqlite = CasesSqliteDriver()

    def get_case_tables(self):
        return sqlite.get_all_tables()

    def get_data_by_id(self, test_method, case_id, case_lvl):
        datas = sqlite.get_datas_by_id(test_method, case_id)
        for key in list(datas.keys()):
            if key == 'extInfo':
                if datas[key] != None:
                    datas[key] = sqlite.get_ext_infos(datas[key])['extInfo']
                    if '.txt' in datas[key]:
                        datas[key] = open(os.path.join(TEST_DATA_DIR, datas[key]), 'r').read()
            #             elif key == 'extDn':
            #                 if datas[key] != None:
            #                     datas[key] = sqlite.get_ext_dns(datas[key])
            #                     if '.txt' in datas[key]:
            #                         datas[key] = open(os.path.join(TEST_DATA_DIR, datas[key]), 'r').read()
            #                 else:
            #                     datas[key] = None
            elif key == 'extItems':
                if datas[key] != None:
                    datas['seal'] = sqlite.get_ext_items(datas[key])
                    if '.txt' in datas[key]:
                        datas[key] = open(os.path.join(TEST_DATA_DIR, datas[key]), 'r').read()
                else:
                    datas['seal'] = None
            elif key == 'expect':
                if datas[key] != None:
                    datas[key] = datas[key].split(';')
                else:
                    datas[key] = ['SUCCESS']
            else:
                continue
        return datas

    def update_desc(self, test_method, case_id, desc):
        sqlite.update_desc(test_method, case_id, desc)

    def get_cases_num(self, test_method):
        return sqlite.get_cases_num(test_method)

    def get_cases_ids(self, test_method):
        return sqlite.get_cases_ids(test_method)
