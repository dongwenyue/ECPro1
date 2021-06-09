# -*- coding: utf-8 -*-
"""
Author:yuqi
"""
import unittest
import time
from BeautifulReport import BeautifulReport as bf
import requests, json


if __name__ == '__main__':
    start = time.perf_counter()
    print(start)
    from utils.configures.paths import SET_SYSCONFIG

    SET_SYSCONFIG('betaSysConfig.ini')  # 环境

    from cases.processes.product.createProduct import createProduct
    from cases.processes.product.createPeriod import createPeriod

    suite = unittest.TestSuite()
    # for j in range(2):

    # for i in range(10):
    #     suite.addTest(createProduct(i + 1, "createProduct"))
    # for i in range(117,127):
    #     suite.addTest(createProduct(i + 1, "createProduct"))
    for i in range(1):
        suite.addTest(createProduct(i + 1, "createProduct"))
    # for i in range(77, 110):
    #     suite.addTest(createProduct(i + 1, "createProduct"))

    # for i in range(0,10):
    #     suite.addTest(createProduct(i + 1, "createProduct"))


    # for i in range(170,190):
    #     suite.addTest(createProduct(i + 1, "createProduct"))
    #     print(i)
    # # suite.addTest(createProduct(121, "createProduct"))8888888

    # suite.addTest(createProduct(2, "createProduct"))


    run = bf(suite)
    run.report(filename='./result/test', description='testResult')


    wx_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=5071ba86-4d67-404b-807c-f751f57cafcf" # 企业微信机器人webhook地址
    # send_message = "女装前缀 = 'Ecprocsgril'，男装前缀 = '男装Ecprocsboy'，童装前缀 = '童装Ecprocschild'"


    def send_msg(self,content):
        """艾特全部，并发送指定信息"""
        data = json.dumps({"msgtype": "text", "text": {"content": content, "mentioned_list": ["@尹正茂"]}})
        r = requests.post(wx_url, data, auth=('Content-Type', 'application/json'),tp_ids = self.case['tp_ids'].split(','))
        print(r.json())


    # if __name__ == '__main__':
    #     send_msg(send_message)

    end = time.perf_counter()
    print(start)
    print(end)
    print('Running time: %s Seconds' % (end - start))
    seconds = end - start
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    print("%02d:%02d:%02d" % (h, m, s))
