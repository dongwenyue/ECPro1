# -*- coding: utf-8 -*-
'''
@author: wsy
'''
import sqlite3

from utils.stringIO.logger.testlogger import ERROR
from ..configures.paths import CASES_DB_PATH


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class CasesSqliteDriver():
    def __init__(self):
        try:
            global conn
            conn = sqlite3.connect(CASES_DB_PATH)
            conn.row_factory = dict_factory

            global cur
            cur = conn.cursor()

        except Exception as e:
            ERROR('init sqlite driver %s error :%s' % (CASES_DB_PATH, e))
            raise BaseException('init sqlite driver %s error :%s' % (CASES_DB_PATH, e))
        self._table_names = [table['name'] for table in self.get_all_tables()]

    def t2d(self, table):
        '''
            make table to arry of dictionary 
        '''
        cursor = cur.execute('SELECT * FROM %s' % table)
        rows = cursor.fetchall()
        return rows

    def get_ext_infos(self, id):  # @ReservedAssignment
        cursor = cur.execute("SELECT * FROM extInfos WHERE id = '%s'" % id)
        return (cursor.fetchall())[0]

    def get_ext_items(self, id):  # @ReservedAssignment
        cursor = cur.execute("SELECT * FROM extItems WHERE id = %s" % id)
        return (cursor.fetchall())[0]

    def get_ext_dns(self, id):  # @ReservedAssignment
        cursor = cur.execute("SELECT * FROM extDn WHERE id = %s" % id)
        return (cursor.fetchall())[0]

    def get_datas_by_id(self, table, dataID):
        try:
            cursor = cur.execute("SELECT * FROM %s WHERE id = %s" % (self._get_table_by_name(table), dataID))
            return (cursor.fetchall())[0]
        except:
            ERROR('get datas from table %s by id %s failed, no datas found' % (self._get_table_by_name(table), dataID))
            raise BaseException(
                'get datas from table %s by id %s failed, no datas found' % (self._get_table_by_name(table), dataID))

    def update_desc(self, table, dataID, desc):
        cur.execute(
            "UPDATE %s set description =  '%s' WHERE id = '%s'" % (self._get_table_by_name(table), desc, dataID))
        conn.commit()

    def get_all_tables(self):
        '''
            make table to arry of dictionary 
        '''
        cursor = cur.execute('SELECT name FROM sqlite_master WHERE type=\'table\' order by name')
        return cursor.fetchall()

    def _get_table_by_name(self, name):
        try:
            return [_table_name for _table_name in self._table_names if _table_name.endswith(name)][0]
        except:
            ERROR('match table by %s failed' % name)
            raise BaseException('match table by %s failed' % name)

    def get_cases_num(self, table):
        try:
            cursor = cur.execute("SELECT COUNT(*) FROM %s" % self._get_table_by_name(table))
            return int((cursor.fetchall())[0])
        except:
            ERROR('get datas\'s num from table %s  failed, no datas found' % self._get_table_by_name(table))
            raise BaseException(
                'get datas\'s num from table %s  failed, no datas found' % self._get_table_by_name(table))

    def get_cases_ids(self, table):
        try:
            cursor = cur.execute("SELECT id FROM %s" % self._get_table_by_name(table))
            return [ids['id'] for ids in cursor.fetchall()]
        except:
            ERROR('get datas\'s id from table %s  failed, no datas found' % self._get_table_by_name(table))
            raise BaseException(
                'get datas\'s id from table %s  failed, no datas found' % self._get_table_by_name(table))
