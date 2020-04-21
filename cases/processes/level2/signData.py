# -*- coding: utf-8 -*-
'''
Created on 2017年3月1日

@author: wangsiyu
'''
from ..._importers import *


class signData_lvl2(TestCase):
    @setup
    def __init__(self, caseid, methodName):
        TestCase.__init__(self, caseid, methodName)

    def signData(self):
        if not self.get_datas('name'):
            name = fullname()
        else:
            name = self.get_datas('name')

        if not self.get_datas('idcard'):
            idCardNumber = idnum()
        else:
            idCardNumber = self.get_datas('idcard')

        plain = self.get_datas('plain')
        if 'txt' in plain:
            plain = base64.b64encode(open('%s/%s' % (TEST_DATA_DIR, plain), 'r').read())

        if not self.get_datas('bussinessId'):
            bussinessId = 'bussinessId_' + str(self.caseid)
        else:
            bussinessId = self.get_datas('bussinessId')

        idCardType = self.get_datas('idtype')

        algo = self.get_datas('algo')

        keyLength = self.get_datas('keyLength')

        dataType = self.get_datas('dataType')

        extItems = self.get_datas('extItems')

        res = anySign.signData(bussinessId, algo, keyLength, name, idCardType, idCardNumber, extItems, plain, dataType)
        INFO('status:' + '       ' + str(res['status']))
        INFO('transId:' + '      ' + str(res['data']['transId']))
        INFO('bussinessId:' + '  ' + str(res['data']['bussinessId']))

        self.assertEqual(self.get_datas('errMsg'), res['message'], '事件证书签名返回')
        self.assertEqual(self.get_datas('errCode'), str(res['status']), '事件证书签名返回')
