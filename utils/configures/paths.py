# -*- coding: utf-8 -*-

import os
import time

CURRENTPATH = os.getcwd()

JVMPATH = None

CLASSPATH = os.path.join(CURRENTPATH, 'resource', 'lib')

CASEPATH = os.path.join(CURRENTPATH, 'cases', 'processes')

LOGCONFIG = os.path.join(CURRENTPATH, 'resource', 'configs', 'logger.ini')

SYSCONFIG = None

DATACONFIG = os.path.join(CURRENTPATH, 'resource', 'datas.ini')

TEST_DATA_DIR = os.path.join(CURRENTPATH, 'resource', 'data')

TEST_DATA_RESULT = os.path.join(CURRENTPATH, 'result', time.strftime('%Y-%m-%d-%H', time.localtime(time.time())))
if not os.path.exists(TEST_DATA_RESULT): os.makedirs(TEST_DATA_RESULT)

RRSOURCE = os.path.join(CURRENTPATH, 'resource')

LOGPATH = os.path.join(CURRENTPATH, 'log', 'result.log')

CASES_DB_PATH = os.path.join(RRSOURCE, 'dbs', 'Cases.db')


def SET_JVMPATH(value):
    global JVMPATH
    JVMPATH = value


def SETDATAS(data):
    global DATACONFIG
    DATACONFIG = os.path.join(CURRENTPATH, 'resource', data)


def SET_SYSCONFIG(value='betaSysConfig.ini'):
    global SYSCONFIG
    SYSCONFIG = os.path.join(CURRENTPATH, 'resource', 'configs', value)
