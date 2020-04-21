#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ..._importers import *


class noEncCert_lvl2(TestCase):
    def __init__(self, caseid, methodName):
        TestCase.__init__(self, caseid, methodName, '2')

    def noEncCert(self):
        name = self.case['name']

        if not self.case['idcard']:
            idCard = idnum()
        else:
            idCard = self.case['idcard']

        bussinessId = 'noEncCert_lvl2_%s' % str(int(round(time.time() * 1000)))

        idCardType = self.case['idcard_type']

        mobile = self.case['mobile']

        algo = self.case['algo']

        if not self.case['extDn']:
            extDn = 'c=cn, cn=%(name)s' % {'name': name}
        else:
            extDn = self.case['extDn']

        version = '1.0'

        extInfo = self.case['extInfo']

        p10 = self.case['p10']

        length = self.case['length']

        expDate = self.case['expdate']

        if not p10:
            try:
                p10res = genKeyPairAndP10(algo, length, extDn)
                self.assertEqual('SUCCESS', p10res['message'], '申请 p10 信息')
                p10 = (p10res['data'])['p10']
            except:
                self.assertEqual(self.case['expect'][0], p10res['message'], '申请 p10 信息')
                return

        res = anySign.noEncCert(bussinessId, algo, p10, name, idCardType, idCard, mobile, extDn,
                                extInfo, version, expDate)

        self.assertEqual(self.case['expect'][0], res['message'], '非加密包证书申请')

        if res['status'] == 200:
            noEncCert_cert = '%s非加密包证书_lvl2_case%s.cer' % (TEST_DATA_RESULT, str(self.case_id))

            open(noEncCert_cert, 'w').write(res['data']['certInfo'])

            INFO('非加密包证书保存至: %s' % noEncCert_cert)
