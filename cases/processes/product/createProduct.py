# -*- coding: utf-8 -*-
from . import wechatRebot
from .. import product
from ..._importers import *
import sys
from cases.processes.product.wechatRebot import *
# prefix = 'Ecprocs'
# class mess():
#     def me(self):
#         tp_ids1 = self.case['tp_ids']
#         prefix1 = prefix
class createProduct(TestCase):
    # @setup
    def __init__(self, caseid, methodName):
        TestCase.__init__(self, caseid, methodName)

    def createProduct(self):
        codes = []
        period = self.case['period']
        filename = self.case['filename']
        period_describe = 'test_%s' % str(uuid.uuid1())[0:15]
        # period_describe = self.case['period_describe']
        category_id = self.case['category_id']
        category_path = self.case['category_path']
        tp_ids = self.case['tp_ids'].split(',')
        # codes.append(self.case['codes'])

        # prefix = 'Ecprocs'
        prefix = 'TbCg'
        # 前缀
        if '女装' in category_path:
            code = ((prefix + 'girl%s') % (time.strftime('%H%M%S', time.localtime(time.time()))))
        elif '男装' in category_path:
            code = ((prefix + 'boy%s') % (time.strftime('%H%M%S', time.localtime(time.time()))))
        elif '童装' in category_path:
            code = ((prefix + 'child%s') % (time.strftime('%H%M%S', time.localtime(time.time()))))
        codes.append(code)

        INFO('-------------------------新增期数------------------------------------')
        period_res = ECPro.createPeriod(token, period, period_describe)
        print(period_res)
        if period_res['data']['id']:
            group_id = period_res['data']['id']

            INFO('-------------------------检测类目平台-----------------------------------')
            tp_ids = ECPro.checkTpid(category_id, tp_ids, token)

            INFO('-------------------------创建商品-----------------------------------')
            product_res = ECPro.createProduct(token, category_id, category_path, codes, tp_ids,
                                              period_res['data']['id'])
            print(product_res)
            if product_res['data']['id']:
                product_id = product_res['data']['id']
                attr_res = ECPro.getAttr(token, tp_ids, category_id)
                INFO('-------------------------提交商品-----------------------------------')
                jsonres = ECPro.setJosn(codes, attr_res, category_id, tp_ids, period_res['data']['id'],
                                        period, period_describe, token, category_path, filename)
                res = ECPro.submitProduct(token, jsonres, product_res['data']['id'])
                # print(json.dumps(res))
                if res['code'] != 0:
                    jsonres['created_type'] = 'staging'
                    ECPro.submitProduct(token, jsonres, product_res['data']['id'])
                INFO('-------------------------上传图片包-----------------------------------')
                status, image_package_id, cover_image = ECPro.uploadFile(token, filename, product_id, group_id,
                                                                         serverurl)
                print(status)
                INFO('-------------------------关联图片包-----------------------------------')
                ECPro.relation(token, product_id, image_package_id, cover_image)


                #time.sleep(1)
                INFO('-------------------------制作详情页-----------------------------------')
                ECPro.createDetailsPage(token, image_package_id, self.case['template_id'], self.case['model_id'],
                                              product_id)

                #time.sleep(1)
                INFO('-------------------------提交资源图-----------------------------------')
                ECPro.setresources(token, product_id)

                # INFO('-------------------------发送平台id-----------------------------------')
                # s = '平台 %s %s' %(tp_ids, prefix)
                # print(s)
                # #print(ECPro.test_robot(s))
