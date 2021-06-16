# -*- coding: utf-8 -*-

from ..._importers import *


class exportDetailsPage(TestCase):
    @setup
    def __init__(self, caseid, methodName):
        TestCase.__init__(self, caseid, methodName)

    def exportDetailsPage(self):
        token = self.case['token']
        document_ids = self.case['document_ids']
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

        res = ECPro.exportDetailsPage(token, document_ids, imgFormat, width, sliceType, isLimitMaxHeight, maxHeight, height,
                          isLimitCount, count, isCompress, compressSize)
        print(res)
        self.assertEqual(self.case['expect'][0], res['message'], '导出详情页')