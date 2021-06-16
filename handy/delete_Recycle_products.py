# -*- coding: utf-8 -*-
"""
@time 2021-06-09
@author: yzm
@删除回收站所有的商品
"""
import requests


products_list =  []
def dele_data(page=1, per_page=40):
    '''遍历回收站所有的商品，返回所有products_id'''
    url = CMS_HOST + '/merchant/v2/products/restore?page=%s&per_page=%s&codes=' % (page, per_page)
    res = requests.get(url,  headers=headers_cms)
    for product_data in res.json()['data']['product_overview']:
        # print(product_data['id'])
        products_list.append(product_data['id'])
        #if product_data['id'] == 2124741:
        #    print(page , per_page, product_data['code'])
    if (page * per_page) - res.json()["data"]["total"] < 0:
        dele_data(page + 1, per_page)
    return products_list

def dele_product(id):
    '''批量永久删除'''
    url = CMS_HOST + '/merchant/v2/products'
    body = {"product_ids":id ,"source":"restore"}
    print(body)
    res = requests.delete(url,  headers=headers_cms, json = body)
    print(res.json())
    if res.json()['message'] == "Success":
        print('删除成功')
    else:
        print('删除失败')

def cms_account(CMS_HOST, cms_number, cms_password):
    """查找账号下的token"""
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

if __name__ == '__main__':
    HOST = 'qa'

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

    products_list = dele_data()
    print(len(products_list))

    # 去重，只显示重复一次的数据
    a = {}
    for i in products_list:
        if products_list.count(i) == 1:
            a[i] = products_list.count(i)
    print(products_list)
    print(a)

    data_list = []
    for k, v in a.items():
        data_list.append(k)

    dele_product(products_list)

