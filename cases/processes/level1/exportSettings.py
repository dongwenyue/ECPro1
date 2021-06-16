# -*- coding: utf-8 -*-

from ..._importers import *


class exportSettings(TestCase):
    @setup
    def __init__(self, caseid, methodName):
        TestCase.__init__(self, caseid, methodName)

    def exportSettings(self):
        token = self.case['token']
        name = 'test_%s'%(time.time())
        imgFormat = self.case['imgFormat']
        width = self.case['width']
        sliceType = self.case['sliceType']
        height = self.case['height']
        maxHeight = self.case['maxHeight']
        isLimitCount = self.case['isLimitCount']
        isLimitMaxHeight = self.case['isLimitMaxHeight']
        count = self.case['count']
        isCompress = self.case['isCompress']
        compressSize = self.case['compressSize']
        default = self.case['default']

        res = ECPro.exportSettings(name, token, imgFormat, width, sliceType, isLimitMaxHeight, maxHeight, height,
                          isLimitCount, count, isCompress, compressSize,default)
        print(res)
        self.assertEqual(self.case['expect'][0], res['message'], '导出详情页')
        id = res['data']['id']
        INFO('新建的导出规则id是：%s'%id)
        INFO('-----------------------------------调用新建详情页接口----------------------------------------')
        image_package_id = self.case['image_package_id']
        template_id = self.case['template_id']
        model_id = self.case['model_id']
        product_id = self.case['product_id']
        note = self.case['note']

        res = ECPro.createDetailsPage(token, image_package_id, template_id, model_id, product_id, note)
        print(res)
        self.assertEqual(self.case['expect'][0], res['message'], '获取导出记录')
        document_id = res['data']['id'][0]
        INFO('新建的详情页面id是：%s'%document_id)

        INFO('-----------------------------------调用获取单条页接口----------------------------------------')

        res = ECPro.getOneDetailsPage(token, document_id)
        print(res)
        self.assertEqual(self.case['expect'][0], res['message'], '获取单条详情页')

        INFO('-----------------------------------调用导出详情页接口----------------------------------------')
        res = ECPro.exportDetailsPage(token, document_id, imgFormat, width, sliceType, isLimitMaxHeight, maxHeight,
                                      height,
                                      isLimitCount, count, isCompress, compressSize)
        print(res)
        self.assertEqual(self.case['expect'][0], res['message'], '导出详情页')