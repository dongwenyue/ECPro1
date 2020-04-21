# -*- coding: utf-8 -*-
'''
Created on 2016年8月16日
@author: zhengkeyan
'''
import random
import time

ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')


def gen_idcard():
    u"""随机生成18为身份证"""
    t = time.localtime()[0]  # 年份
    k = '%02d%02d%02d%04d%02d%02d%03d' % (random.randint(10, 99),
                                          random.randint(10, 99),
                                          random.randint(10, 99),
                                          random.randint(t - 80, t - 18),
                                          random.randint(1, 12),
                                          random.randint(1, 28),
                                          random.randint(1, 999))
    y = 0
    for i in range(17):
        y += int(k[i]) * ARR[i]
    return '%s%s' % (k, LAST[y % 11])
