# -*- coding: utf-8 -*-
"""
@time 2021-5-21
@author: yzm
"""
import datetime
import random
import sqlite3
import string
import time
import uuid

import requests
import MySQLdb
from collections import ChainMap

def select_mysql(type):
    # 打开数据库连接
    #db = MySQLdb.connect("rm-2zeb07rt531eym8of1o.mysql.rds.aliyuncs.com", "qa_v2", "lyp82nLF", "qa_v2_merchant", charset='utf8' )
    PERIOD_MAPPING = {}
    try:
        db = MySQLdb.connect(
            host='rm-2zeb07rt531eym8of1o.mysql.rds.aliyuncs.com',
            port=3306,
            user='qa_v2',
            passwd='lyp82nLF',
            db='qa_v2_design',
            charset='utf8',
            compress=1,
            connect_timeout=1
        )
    except BaseException:
        print("Could not connect to MySQL server.")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # qa_v2_catalog 谨慎操作这张表，仅此一份
    sql = "SELECT * FROM `qa_v2_catalog`.`category` WHERE `is_leaf` <> '0' AND `path` LIKE '%s' AND `status` = 'enabled' ORDER BY `is_leaf` DESC " % ("%" + type + '%')
    print(sql)
   # 执行SQL查询语句
    try:
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print(len(results))
        for row in results:
            id = row[0]
            path = row[9]
            # 打印结果
            # print("mc_period_id=%s,cms_period_id=%s" % (mc_period_id, cms_period_id))
            PERIOD_MAPPING[id] = path
    except:
        print('查询失败')
    print(PERIOD_MAPPING)
    print(len(PERIOD_MAPPING))
    db.close()
    return PERIOD_MAPPING


def MakeDbfile(mysql_name):
    # 连接数据库(如果不存在则创建)
    conn = sqlite3.connect(mysql_name)

    cursor = conn.cursor()

    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS createPeriod")
    cursor.execute("DROP TABLE IF EXISTS createProduct")
    # 创建表
    sql = 'CREATE TABLE "createPeriod" ("id"  TEXT,"description"  TEXT,"period"  TEXT,"period_describe"  TEXT,"expect"  TEXT);'
    cursor.execute(sql)
    sql = 'CREATE TABLE "createProduct" ("id"  INT PRIMARY KEY     NOT NULL,"description"  TEXT,"period"  TEXT,"category_id"  TEXT,"period_id"  TEXT,"category_path"  TEXT,"filename"  TEXT,"codes"  TEXT,"tp_ids"  TEXT,"template_id"  TEXT,"model_id"  TEXT,"expect"  TEXT)'
    print ("Table created successfully")
    cursor.execute(sql)

    # 关闭游标
    cursor.close()
    # 提交事物
    conn.commit()
    # 关闭连接
    conn.close()


def select_insert(mysql_name, d, code, tp_id, template_list, model_list):
    # 写入文件数据库
    conn = sqlite3.connect(mysql_name)
    c = conn.cursor()
    print("Opened database successfully")
    sql = 'INSERT INTO "createPeriod"("id", "description", "period", "period_describe", "expect") VALUES ("1", "【创建商品期数】", "2020-12-30", "123456", "0");'
    print(sql)
    c.execute(sql)
    count = 0
    for key, value in d.items():
        template_id = str(random.choice(template_list))
        model_id = str(random.choice(model_list))
        count = count + 1
        if '女' in value:
            des = "【创建商品】普通商品上货流程（女装）"
            file = 'testZip.zip'
            sql = 'INSERT INTO "createProduct"("id", "description", "period", "category_id", "period_id", "category_path", "filename", "codes", "tp_ids", "template_id", "model_id", "expect") VALUES ("%s", "%s", "2020-12-30", "%s", "13102", "%s", "%s", "%s", "%s", "%s", "%s", "0");' % (
            count, des, key, value, file, code, tp_id, template_id, model_id)
            print(sql)
        if '男' in value:
            des = "【创建商品】普通商品上货流程（男装）"
            file = 'boy.zip'
            sql = 'INSERT INTO "createProduct"("id", "description", "period", "category_id", "period_id", "category_path", "filename", "codes", "tp_ids", "template_id", "model_id", "expect") VALUES ("%s", "%s", "2020-12-30", "%s", "13102", "%s", "%s", "%s", "%s", "%s", "%s", "0");' % (
            count, des, key, value, file, code, tp_id, template_id, model_id)
            print(sql)
        if '童' in value:
            des = "【创建商品】普通商品上货流程（童装）"
            file = 'testZip.zip'
            sql = 'INSERT INTO "createProduct"("id", "description", "period", "category_id", "period_id", "category_path", "filename", "codes", "tp_ids", "template_id", "model_id", "expect") VALUES ("%s", "%s", "2020-12-30", "%s", "13102", "%s", "%s", "%s", "%s", "%s", "%s", "0");' % (
            count, des, key, value, file, code, tp_id, template_id, model_id)
            print(sql)
        c.execute(sql)
    conn.commit()
    print("Records created successfully")
    print(count)
    conn.close()

def cms_account(CMS_HOST, cms_number, cms_password):
    """查找账号下的token
    """
    # 获取access_token和account_id
    login_url = CMS_HOST + '/auth/login'
    login_body = {"mobile":str(cms_number),"password":str(cms_password),"login_way":"mobile"}
    print(login_body)
    response = requests.post(login_url,json=login_body)
    # print(response.json()['data']['access_token'],response.json()['data']['last_login_account'])
    print(response.json()['data']['last_login_account'])

    # 获取token
    account_url = CMS_HOST + '/user/account/login'
    account_body = {"account_id": response.json()['data']['last_login_account']}
    headers = {}
    headers['authorization'] = 'Bearer '+ response.json()['data']['access_token']
    res = requests.post(account_url, json=account_body, headers=headers)
    # print(res.json()['data']['access_token'])
    token = res.json()['data']['access_token']
    cms_account_id = response.json()['data']['last_login_account']
    print(token)
    return token, cms_account_id


template_list = []
def get_template_id(page=1, per_page=14):
    # 返回所有详情页模板id
    url = CMS_HOST + '/design-studio/template/user_template?preview=true&page=%s&total=1&per_page=%s' % (page, per_page)
    res = requests.get(url=url, headers=headers_cms)
    for template in res.json()['data']['template']:
        template_list.append(str(template['id']))
    if (page * per_page) - res.json()["data"]["total"] < 0:
        get_template_id(page + 1, per_page)
    return template_list


model_list = []
def get_model_id(page=1, per_page=14):
    # 返回所有模特id
    url = CMS_HOST + '/merchant/config/fashion_model?page=%s&per_page=%s' % (page, per_page)
    res = requests.get(url=url, headers=headers_cms)
    for results in res.json()['data']['results']:
        model_list.append(str(results['id']))
    if (page * per_page) - res.json()["data"]["total"] < 0:
        get_model_id(page + 1, per_page)
    return model_list
if __name__ == '__main__':
    tp_id = "1001"
    HOST = 'qa'
    mysql_name = 'Case.db'

    if HOST == 'qa':
        cms_number = 18617847474
        cms_password = 'lf18617847474'
        CMS_HOST = 'https://cms-qa-api.ecpro.com'
    elif HOST == 'dev':
        cms_number = 18617847474
        cms_password = '18617847474'
        CMS_HOST = 'https://cms-dev-api.ecpro.com'
    elif HOST == 'on':
        cms_number = 18612210007
        cms_password = '18612210007'
        CMS_HOST = 'https://cms-api.ecpro.com'


    CMS_token, CMS_account_id = cms_account(CMS_HOST, cms_number, cms_password)
    headers_cms = {}
    headers_cms['authorization'] = 'Bearer ' + CMS_token

    template_list = get_template_id()
    print(template_list)
    model_list = get_model_id()
    print(model_list)

    girl = select_mysql('女')
    boy = select_mysql('男')
    children = select_mysql('童')
    MakeDbfile(mysql_name)
    d = dict(ChainMap(children, boy, girl))
    # Python生成2位的英文大写的随机数
    random_str = ''.join([random.choice(string.ascii_uppercase) for i in range(2)])
    code = time.strftime("%m%d", time.localtime()) + random_str
    select_insert(mysql_name, d, code, tp_id, template_list, model_list)






