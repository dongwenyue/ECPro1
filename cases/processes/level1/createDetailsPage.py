# -*- coding: utf-8 -*-

from ..._importers import *


class createDetailsPage(TestCase):
    # @setup
    def __init__(self, caseid, methodName):
        TestCase.__init__(self, caseid, methodName)

    def createDetailsPage(self):
        token = self.case['token']
        image_package_id = self.case['image_package_id']
        template_id = self.case['template_id']
        model_id = self.case['model_id']
        product_id = self.case['product_id']
        note = self.case['note']

        res = ECPro.createDetailsPage(token,image_package_id,template_id,model_id,product_id,note)
        print(res)
        self.assertEqual(self.case['expect'][0], res['message'], '获取导出记录')