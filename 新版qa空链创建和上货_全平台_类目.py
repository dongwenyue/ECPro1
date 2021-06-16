# -*- coding: utf-8 -*-
"""
@time 2020-1-22
@author: yzm
"""
import xlrd
import os
import time
import requests
import hashlib
import datetime
import re
import sys
import argparse
import json
import xlwt
import random


def get_time():
    """获取当前时间戳"""
    # now_time = (datetime.datetime.now() + datetime.timedelta(hours=-0)).strftime("T%H:%M:%S:%f")
    #now_time = datetime.datetime.now().strftime('T%H:%M:%S.%f')
    now_time = datetime.datetime.now().strftime('T%H%M%S%f')
    # 取到毫秒（毫秒第一位数字）的日期  # 转换成str后切片
    now_time = str(now_time)[:-5]
    return now_time


def read_url_get(code_url):
    response_2 = requests.get(url=code_url, headers=headers).json()
    response_str = str(response_2)
    return response_str


def read_url_post(code_url, data):
    response_2 = requests.post(url=code_url, headers=headers, data=data).json()
    response_str = str(response_2)
    return response_str


def read_url_post_json(code_url, data):
    response2 = requests.post(url=code_url, headers=headers, json=data).json()
    response_str = str(response2)
    return response_str


def create_null_link(prefix, category_id, category_path, tp_ids):
    """创建空链接商品
     :return: 商品的product_id
    """
    merchant_url = CMS_HOST + "/merchant/v2/products"
    now_time = get_time()
    data1 = {"category_id": category_id, "category_path": category_path, "period_id": 14854,
             #"codes": [prefix + category_path.split('>> ')[-1] + str(now_time)],
             "codes": [prefix  + str(now_time)],
             "tp_ids": [tp_ids]}
    print('创建商品的报文:', data1)
    print("1.访问接口,创建商品:" + merchant_url)
    response = read_url_post_json(merchant_url, data1)
    response = eval(response)
    print("商品ID值:", response["data"]["id"])
    return response["data"]["id"]


def water_mark(tp_id):
    """查找随机一个水印
     :return: 水印的id
    """
    water_mark_url = CMS_HOST + '/merchant/config/water-mark?page=1&per_page=10&tp_id=%s' % tp_id
    response = read_url_get(water_mark_url)
    response = eval(response)
    water_mark_data = random.choice(response["data"]["results"])
    print('随机取到的水印name：', water_mark_data["name"])
    print('随机取到的水印id：', water_mark_data["id"])
    return water_mark_data["id"]


def shops(tp_name, shop_name, brand_name):
    """查找店铺和品牌和tp_id
     :return: 店铺id和品牌id：shop["id"], shop["shop_id"] 和tp_id
    """
    shop_url = CMS_HOST + '/merchant/shop/personal-center'
    response = read_url_get(shop_url)
    response = eval(response)
    # 取到店铺ID和品牌ID （shop_id 和 brand_id）
    for shop_data in response["data"]:
        if shop_data["name"] == tp_name:
            shop_data_id = shop_data["id"]
            for shop in shop_data["shops"]:
                if shop['name'] == shop_name:
                    for brand in shop["brands"]:
                        if brand['name'] == brand_name:
                            print(tp_name, '品牌id：', brand["id"])
                            print(tp_name, '品牌名称：', brand["name"])
                            print(tp_name, '店铺id：', brand["shop_id"])
                            return brand["id"], brand["shop_id"], shop_data_id


def batch_info(brand_id, tp_id):
    """查找随机的物流与售后，需要传店铺id
     :return: 随机的物流与售后id：batch_id
    """
    batch_info_url = CMS_HOST + '/merchant/config/batch_info?tp_id=%s&page=1&per_page=40' % tp_id
    response = read_url_get(batch_info_url)
    response = eval(response)
    batch_list = {}
    for batch in response["data"]["results"]:
        if batch["shop_id"] == brand_id:
            batch_list[batch["id"]] = batch["name"]
    batch_id = random.choice(list(batch_list))
    print('随机的物流与售后id', batch_id)
    print('随机的物流与售后name', batch_list[batch_id])
    return batch_id


def category(brand_id):
    """查找随机的店铺分类，需要传店铺id，随机找到5个
    :return: 随机的店铺分类id字典
    """
    batch_info_url = CMS_HOST + '/merchant/shop/%s/category' % brand_id
    response = read_url_get(batch_info_url)
    response = eval(response)
    category_list = {}
    category_id_key_list = []
    for category_data in response["data"]:
        # 遍历店铺的子类
        for children_key, children_value in category_data.items():
            if children_key == 'children':
                for children in category_data[children_key]:
                    category_list[children["cid"]] = children["name"]
            elif category_data['parent_cid'] is not 0:
                category_list[category_data["cid"]] = category_data["name"]
    category_id = random.sample(list(category_list), 5)
    for category_id_key in category_id:
        print('随机的店铺分类id和name', category_id_key, category_list[category_id_key])
        category_id_key_list.append(category_id_key)
    print(category_id_key_list)
    return category_id_key_list


def mappings_tp_ids(person, tp_name):
    code_url = CMS_HOST + "/catalog/categories"
    create_product = {}
    product_category = {}
    response = requests.get(code_url, headers=headers).json()
    for product in response['data']['categories']:
        first_url = CMS_HOST + "/catalog/categories?parent_id" + str(product['id'])
        code_first_url = first_url
        response_first_url = requests.get(code_first_url, headers=headers).json()
        for product_first_url in response_first_url['data']['categories']:
            if product_first_url['is_leaf'] == True:
                # print(product_first_url['id'], product_first_url['path'])
                create_product[product_first_url['id']] = product_first_url['path']
            if product_first_url['is_leaf'] == False:
                product_second_url_id = CMS_HOST + "/catalog/categories?parent_id=" + str(
                    product_first_url['id'])
                response_second_url_id = requests.get(product_second_url_id, headers=headers).json()
                for product_second_url_id_name in response_second_url_id['data']['categories']:
                    if product_second_url_id_name['is_leaf'] == True:
                        # print(product_second_url_id_name['id'], product_second_url_id_name['path'])
                        create_product[product_second_url_id_name['id']] = product_second_url_id_name['path']
                    if product_second_url_id_name['is_leaf'] == False:
                        product_three_url_id = CMS_HOST + "/catalog/categories?parent_id=" + str(
                            product_second_url_id_name['id'])
                        response_three_url_id_name = requests.get(product_three_url_id, headers=headers).json()
                        for response_three_url_id_name_data in response_three_url_id_name['data']['categories']:
                            # print(response_three_url_id_name_data['id'], response_three_url_id_name_data['path'])
                            create_product[response_three_url_id_name_data['id']] = response_three_url_id_name_data[
                                'path']
    # print(create_product)
    for category_ids, path in create_product.items():
        if path[0] == person:
            code_url = CMS_HOST + "/catalog/categories/%s/mappings?tp_ids=1001,1000,1003,1004,1005,1006,1008,1009,1010,1011" % category_ids
            response = requests.get(code_url, headers=headers).json()
            for product in response['data']['mappings']:
                if product['tp_name'] == tp_name and product['tp_category']:
                    # print(category_ids, path)
                    product_category[category_ids] = path
    return product_category


def merchant_publishs(product_ids, shop_id, brand_id, water_mark, batch_info_id, tp_id):
    """空链上货和生成上货的链接
     :return: 查看上货的链接
    """
    merchant_url = CMS_HOST + "/merchant/publish"
    data = []
    for product_id in product_ids:
        print(product_id)
        # [{"tp_id":1003,"shop_id":2007054,"brand_id":2394,"product_id":2117029,"document_ids":["0"],"batch_info_id":1279,"water_mark_id":183,"shop_categories":[15839581,4047568,2871365,15535783,15480214]}]
        data_singular = {"tp_id": tp_id, "shop_id": brand_id, "brand_id": shop_id,
                         "product_id": product_id, "document_ids": ["0"], "batch_info_id": batch_info_id,
                         "water_mark_id": water_mark}
        data.append(data_singular)
    print('访问上货接口的报文:', data)
    print("2.访问接口,上货:" + merchant_url)
    response = read_url_post_json(merchant_url, data)
    print(response)
    response = eval(response)
    print(response["data"]["publish_ids"])
    publish_id = list(map(str, response["data"]["publish_ids"]))
    publish_id = ','.join(publish_id)
    merchant_check_url = CMS_PUB_HOST + '/publish/publish-results?pids=%s&sid=%s&t=publish' % (
        publish_id, brand_id)
    print(merchant_check_url)


def merchant_publishs_jd(product_ids, shop_id, brand_id, water_mark, batch_info_id, tp_id, category_id):
    """京东空链上货和生成上货的链接
     :return: 查看上货的链接
    """
    merchant_url = CMS_HOST + "/merchant/publish"
    data = []
    for product_id in product_ids:
        print(product_id)
        data_singular = {"tp_id": tp_id, "shop_id": brand_id, "brand_id": shop_id,
                         "product_id": product_id, "document_ids": ["0"], "batch_info_id": batch_info_id,
                         "water_mark_id": water_mark, "shop_categories": category_id}
        data.append(data_singular)
    print('访问上货接口的报文:', data)
    print("2.访问接口,上货:" + merchant_url)
    response = read_url_post_json(merchant_url, data)
    print(response)
    response = eval(response)
    print(response["data"]["publish_ids"])
    publish_id = list(map(str, response["data"]["publish_ids"]))
    publish_id = ','.join(publish_id)
    merchant_check_url = CMS_PUB_HOST + '/publish/publish-results?pids=%s&sid=%s&t=publish' % (
        publish_id, brand_id)
    print(merchant_check_url)


def merchant_publishs_tm(product_ids, shop_id, brand_id, water_mark, batch_info_id, tp_id, category_id,
                         shipping_template_id):
    """天猫和淘宝的空链上货和生成上货的链接
     :return: 查看上货的链接
    """
    merchant_url = CMS_HOST + "/merchant/publish"
    data = []
    # [{"tp_id":1001,"shop_id":2007044,"brand_id":2372,"product_id":2117077,"document_ids":["0"],"batch_info_id":1278,"shipping_template_id":788,"water_mark_id":175,"shop_categories":[1556797630,1556889354,1556880975]}]
    # [{"tp_id":1001,"shop_id":2007044,"brand_id":2372,"product_id":2117078,"document_ids":["0"],"batch_info_id":1278,"main_video_id":"290558942376","shipping_template_id":788,"water_mark_id":175,"shop_categories":[1556889354,1556797630,1556880975]}]
    for product_id in product_ids:
        print(product_id)
        data_singular = {"tp_id": tp_id, "shop_id": brand_id, "brand_id": shop_id,
                         "product_id": product_id, "document_ids": ["0"], "batch_info_id": batch_info_id,
                         "shipping_template_id": shipping_template_id,
                         "water_mark_id": water_mark, "shop_categories": category_id}
        data.append(data_singular)
    print('访问上货接口的报文:', data)
    print("2.访问接口,上货:" + merchant_url)
    response = read_url_post_json(merchant_url, data)
    print(response)
    response = eval(response)
    print(response["data"]["publish_ids"])
    print('共计多少商品：', len(response["data"]["publish_ids"]))
    publish_id = list(map(str, response["data"]["publish_ids"]))
    publish_ids = ','.join(publish_id)
    merchant_check_url = CMS_PUB_HOST + '/publish/publish-results?pids=%s&sid=%s&t=publish' % (
        publish_ids, brand_id)
    print(merchant_check_url)

    time.sleep(10)
    publish_product_id_list = []
    print("发布之后的接口")
    publish_ids_data = '%2C'.join(publish_id)
    merchant_check_api_url = 'https://cms-qa-api.ecpro.com/merchant/publish?publish_ids=%s&page=1&per_page=%s' % (
        publish_ids_data, len(response["data"]["publish_ids"]))
    print(merchant_check_api_url)
    response = requests.get(merchant_check_api_url, headers=headers).json()
    print(response['data']['results'])
    for publish_results in response['data']['results']:
        if publish_results['pub_description'] == '发布成功':
            publish_product_id = publish_results['product_id']
            # 删除发布成功的商品
            delete_url = 'https://cms-qa-api.ecpro.com/merchant/v2/products'
            data_delete = {"source": "overview", "product_ids": [publish_product_id]}
            requests.delete(delete_url, headers=headers, json=data_delete).json()
        else:
            publish_product_id = publish_results['id']
            publish_product_id_list.append(publish_product_id)
    print("删除发布成功的商品，之后的接口")
    publish_end_id = list(map(str, publish_product_id_list))
    publish_product_end_ids = ','.join(publish_end_id)
    merchant_end_api_url = CMS_PUB_HOST + '/publish/publish-results?pids=%s&sid=%s&t=publish' % (publish_product_end_ids, brand_id)
    print(merchant_end_api_url)

#https://cms-qa.ecpro.com/publish/publish-results?pids=31325,31326,31327,31328,31329,31330,31331,31332,31333,31334,31335,31336,31337,31338,31339,31340,31341,31342,31343,31344,31345,31346,31347,31348,31349,31350,31351,31352,31353,31354,31355,31356,31357,31358,31359,31360,31361&sid=2007057&t=publish
#https://cms-qa.ecpro.com/publish/publish-results?pids=2122032,2122035,2122036,2122037,2122038,2122039,2122040,2122016,2122017,2122019,2122020,2122021&sid=2007057&t=publish

if __name__ == '__main__':
    '''
    淘宝  上货需要 水印选择 品牌选择 物流与售后 运费模板 店铺分类
    天猫  上货需要 水印选择 品牌选择 物流与售后 3:4视频主图 运费模板 店铺分类  
    京东  上货需要 水印选择 品牌选择 物流与售后 店铺分类   
    拼多多上货需要 水印选择 品牌选择 物流与售后
    唯品会上货需要 水印选择 品牌选择 物流与售后
    有赞  上货需要 水印选择 品牌选择 物流与售后 店铺分类
    快手  上货需要 水印选择 品牌选择 物流与售后
    抖音  上货需要 水印选择 品牌选择 物流与售后
    '''
    # 运费模板id和期数id，需要传
    # 淘宝  other  天猫 LANDI 京东 LANDI 拼多多  test 唯品会 LANDI 有赞 test 快手 tttt 抖音 采唯
    # 天猫  伊木子  京东 bosie 抖音 bosie
    tp_name = '京东'  # 平台
    shop_name = 'LANDI女装旗舰店'
    brand_name = 'LANDI'  # 品牌
    prefix = 'JDD'  # 空链接商品的前缀
    person = '女'
    HOST = 'qa'
    if HOST == 'qa':
        CMS_HOST = 'https://cms-qa-api.ecpro.com'
    elif HOST == 'on':
        CMS_HOST = 'https://cms-api.ecpro.com'
    if 'qa-api' in CMS_HOST:
        CMS_PUB_HOST = 'https://cms-qa.ecpro.com'
        headers = {
            "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMDAwMTczLCJ1c2VyX3N0YXR1cyI6ImVuYWJsZWQiLCJhY2NvdW50cyI6WzEwMDAxODldLCJpc3MiOiJ1MTlkaUVnVjdMVURiejF5dlFlaTZ2c2NieWRpeXBQQyIsImlhdCI6MTYyMjUzMTgwNCwiZXhwIjoxNjIyNjE4MjA0LCJhY2NvdW50X2lkIjoxMDAwMTg5LCJhY2NvdW50X3N0YXR1cyI6ImVuYWJsZWQiLCJyb2xlcyI6WyJcdTdiYTFcdTc0MDZcdTU0NTgiLCJyb290Il0sInBlcm1zIjpbXX0.CEGetpmgkhewWojtydRbwro78NacmqFx07jmbR2Mkp8",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }
    elif 'cms-api' in CMS_HOST:
        CMS_PUB_HOST = 'https://cms.ecpro.com'
        headers = {
            "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo2LCJ1c2VyX3N0YXR1cyI6ImVuYWJsZWQiLCJpc3MiOiJhNlprcE1kNHViZ0llSEtsTkxNdmFXVUVOcmZvbHVqdyIsImlhdCI6MTYxMTc0NTk0MSwiZXhwIjoxNjExODMyMzQxfQ.UoetVZQPG1iUYug5NVE4_leAW19I8ZrF5Y3y9BlM7lk",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }

    shop_id, brand_id, tp_id = shops(tp_name, shop_name, brand_name)
    water_mark = water_mark(tp_id)
    batch_info_id = batch_info(brand_id, tp_id)
    product_category = mappings_tp_ids(person, tp_name)
    TP_dicts = {1000: "淘宝", 1001: "天猫", 1003: "京东", 1004: "拼多多", 1005: "唯品会", 1006: "有赞", 1008: "快手", 1009: "抖音", 1010: "京东自营", 1011: "爱库存"}
    for tp_ids, tp_names in TP_dicts.items():
        if tp_names == tp_name:
            categorg_tp_id = tp_ids

    product_ids = []
    for category_id, categorg_path in product_category.items():
        print(category_id, categorg_path)
        product_id = create_null_link(prefix, category_id, categorg_path, categorg_tp_id)
        product_ids.append(product_id)
    print(product_ids)

    if tp_name == '京东':
        category_id = category(brand_id)
        merchant_publishs_jd(product_ids, shop_id, brand_id, water_mark, batch_info_id, tp_id, category_id)
    elif tp_name == '天猫':
        # 上传了3:4主图视频，必须上传3:4商品图片
        # 只加了运费模板
        category_id = category(brand_id)
        merchant_publishs_tm(product_ids, shop_id, brand_id, water_mark, batch_info_id, tp_id, category_id, 1704)
    elif tp_name == '淘宝':
        # 只加了运费模板
        category_id = category(brand_id)
        merchant_publishs_tm(product_ids, shop_id, brand_id, water_mark, batch_info_id, tp_id, category_id, 785)
    else:
        pass
        #merchant_publishs(product_ids, shop_id, brand_id, water_mark, batch_info_id, tp_id)
