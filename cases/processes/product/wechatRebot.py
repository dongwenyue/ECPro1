# -*- coding: utf-8 -*-
from utils.dbutils.sqlite_dao import CasesSqliteDao
import requests


class wechatRebot:
    def __init__(self):
        pass
    def Rebot(self):
        self.case_db = CasesSqliteDao()
        self.case = self.case_db.get_data_by_id("createProduct", 1, 'lvl')
        tp_ids = self.case['tp_ids'].split(',')
        prefix = self.case['codes']
        # print(tp_ids, prefix)
        return tp_ids, prefix

class wechatRebot_send:
    def __init__(self,message):
        self.message = message
    def test_robot(self):
        headers = {"CContent-Type": "text/plain"}
        data = {"msgtype": "text","text": {"content":self.message,}}
        wxurl = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=24692f61-7f4f-41f4-a4df-57b9b4660a57'
        r = requests.post(url=wxurl, headers=headers, json=data)
        print(r.text)
        return (r.text)
