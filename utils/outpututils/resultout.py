# -*- coding: utf-8 -*-
'''
@author: wsy
'''
import os

from ..configures.paths import TEST_DATA_RESULT, TEST_DATA_DIR


# 设备信息

def OUT_PDF(methodName):
    return OUT(methodName, 'pdf')


def OUT(methodName, suffix=None):
    if suffix == None:
        return os.path.join(TEST_DATA_RESULT, methodName.replace('@Description:', '').replace(':', '_'))
    else:
        return os.path.join(TEST_DATA_RESULT,
                            '%s.%s' % (methodName.replace('@Description:', '').replace(':', '_'), suffix))


def GETIMAGE(img):
    return os.path.join(TEST_DATA_RESULT, img)


def GETPDF(pdf):
    return os.path.join(TEST_DATA_RESULT, pdf)


def GET_DATAS(datas):
    datas = datas.split(';')
    path = ''.join([str(r'%s%s' % (TEST_DATA_DIR, data) + ';') for data in datas])
    return path[:-1]
