# -*- coding: utf-8 -*-
'''
Created on 2018年5月8日

@author: WSY
'''

ONLY_MSSP = 'ONLY_MSSP'

ONLY_MSSM = 'ONLY_MSSM'

ONLY_MSSG = 'ONLY_MSSG'

ONLY_MSSM_REASON = '仅运行云签章相关用例'

ONLY_MSSP_REASON = '仅运行云签名相关用例'

ONLY_MSSG_REASON = '仅运行网关相关用例'

runner_tags = []


def set_tags(tags):
    global runner_tags
    runner_tags = tags


def tags_check(tag):
    if tag.upper() in runner_tags:
        return True
    else:
        return False
