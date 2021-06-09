# -*- coding: utf-8 -*-

import os
import time

CURRENTPATH = os.getcwd()

JVMPATH = None

CASEPATH = os.path.join(CURRENTPATH, 'cases', 'processes')

LOGCONFIG = os.path.join(CURRENTPATH, 'resource', 'configs', 'logger.ini')

SYSCONFIG = None

TEST_DATA_DIR = os.path.join(CURRENTPATH, 'resource', 'data')

PATHNAME = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
TEST_DATA_RESULT = os.path.join(CURRENTPATH, 'result')
# if not os.path.exists(TEST_DATA_RESULT): os.makedirs(TEST_DATA_RESULT)

RRSOURCE = os.path.join(CURRENTPATH, 'resource')

LOGPATH = os.path.join(CURRENTPATH, 'log', 'result.log')

CASES_DB_PATH = os.path.join(RRSOURCE, 'dbs', 'Case.db')


def SETDATAS(data):
    global DATACONFIG
    DATACONFIG = os.path.join(CURRENTPATH, 'resource', data)


def SET_SYSCONFIG(value='betaSysConfig.ini'):
    global SYSCONFIG
    SYSCONFIG = os.path.join(CURRENTPATH, 'resource', 'configs', value)