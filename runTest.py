# -*- coding: utf-8 -*-
"""
Author:yuqi
"""
import unittest
import time
from BeautifulReport import BeautifulReport as bf

if __name__ == '__main__':
    start = time.perf_counter()
    print(start)
    from utils.configures.paths import SET_SYSCONFIG

    SET_SYSCONFIG('betaSysConfig.ini')  # 环境

    from cases.processes.product.createProduct import createProduct

    suite = unittest.TestSuite()

    for i in range(16, 35):
          suite.addTest(createProduct(i + 1, "createProduct"))
    for i in range(88, 92):
          suite.addTest(createProduct(i + 1, "createProduct"))
    #
    # for i in range(119,129):
    #     suite.addTest(createProduct(i + 1, "createProduct"))


    run = bf(suite)
    run.report(filename='./result/test', description='testResult')

    end = time.perf_counter()
    seconds = end - start
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    create_time = "%02d:%02d:%02d" % (h, m, s)
    print(create_time)


    from cases.processes.product.wechatRebot import wechatRebot, wechatRebot_send
    mess = wechatRebot()
    tp_ids, prefix = mess.Rebot()
    tp_ids = ','.join(tp_ids)
    print(tp_ids, prefix)
    message = '勇敢的大老牛创建的平台:%s  商品前缀:%s  创建用时:%s' % (tp_ids, prefix, create_time)
    print(message)
    mess = wechatRebot_send(message).test_robot()
    print(mess)
