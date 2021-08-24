# -*- coding: utf-8 -*-
from initdrivers.global_importers import *
from utils.configures.paths import TEST_DATA_DIR
from utils.outpututils.resultout import *
import zipfile
import json
color_list = [{'乳白色': '1'}, {'白色': '2'}, {'米白色': '3'}, {'浅灰色': '4'}, {'深灰色': '5'}, {'灰色': '6'}, {'银色': '7'},
              {'黑色': '8'}, {'桔红色': '9'},
              {'玫红色': '10'}, {'粉红色': '11'}, {'红色': '12'}, {'藕色': '13'}, {'西瓜红': '14'}, {'酒红色': '15'}, {'卡其色': '16'},
              {'姜黄色': '17'}, {'明黄色': '18'}, {'杏色': '19'}, {'柠檬黄': '20'}, {'桔色': '21'}, {'浅黄色': '22'},
              {'金色': '24'}, {'香槟色': '25'}, {'黄色': '26'}, {'军绿色': '27'}, {'墨绿色': '28'}, {'浅绿色': '29'}, {'绿色': '30'},
              {'翠绿色': '31'}, {'青色': '33'}, {'天蓝色': '34'}, {'宝蓝色': '36'}, {'浅蓝色': '37'},
              {'深蓝色': '38'}, {'湖蓝色': '39'}, {'蓝色': '40'}, {'藏青色': '41'}, {'浅紫色': '42'}, {'深紫色': '43'}, {'紫红色': '44'},
              {'紫色': '46'}, {'咖啡色': '47'}, {'巧克力色': '48'}, {'栗色': '49'}, {'浅棕色': '50'}, {'深卡其布色': '51'},
              {'深棕色': '52'}, {'褐色': '53'}, {'驼色': '54'}, {'花色': '55'}, {'咖色': '57'}, {'米色': '58'},
              {'裸色': '59'},
              {'粉色': '60'}, {'橙色': '61'}, {'彩色': '62'}, {'肤色': '63'}, {'其他颜色': '64'}, {'炫色': '65'},
              {'自定义颜色1': f"{uuid.uuid4()}"}
    , {'自定义颜色2': f"{uuid.uuid4()}"}, {'自定义颜色3': f"{uuid.uuid4()}"}, {'自定义颜色4': f"{uuid.uuid4()}"},
              {'自定义颜色5': f"{uuid.uuid4()}"}
    , {'自定义颜色6': f"{uuid.uuid4()}"}, {'自定义颜色7': f"{uuid.uuid4()}"}, {'自定义颜色8': f"{uuid.uuid4()}"},
              {'自定义颜色9': f"{uuid.uuid4()}"}
    , {'自定义颜色10': f"{uuid.uuid4()}"}, {'自定义颜色11': f"{uuid.uuid4()}"}, {'自定义颜色12': f"{uuid.uuid4()}"},
              {'自定义颜色13': f"{uuid.uuid4()}"}
    , {'自定义颜色14': f"{uuid.uuid4()}"}, {'自定义颜色15': f"{uuid.uuid4()}"}, {'自定义颜色16': f"{uuid.uuid4()}"},
              {'自定义颜色17': f"{uuid.uuid4()}"}, {'自定义颜色18': f"{uuid.uuid4()}"}, {'自定义颜色19': f"{uuid.uuid4()}"},
              {'自定义颜色20': f"{uuid.uuid4()}"}
    , {'自定义颜色21': f"{uuid.uuid4()}"}, {'自定义颜色22': f"{uuid.uuid4()}"}, {'自定义颜色23': f"{uuid.uuid4()}"},
              {'自定义颜色24': f"{uuid.uuid4()}"}, {'自定义颜色25': f"{uuid.uuid4()}"}, {'自定义颜色26': f"{uuid.uuid4()}"}
    , {'自定义颜色27': f"{uuid.uuid4()}"}, {'自定义颜色28': f"{uuid.uuid4()}"}, {'自定义颜色29': f"{uuid.uuid4()}"},
              {'自定义颜色30': f"{uuid.uuid4()}"}
    , {'自定义颜色31': f"{uuid.uuid4()}"}, {'自定义颜色32': f"{uuid.uuid4()}"}, {'自定义颜色33': f"{uuid.uuid4()}"},
              {'自定义颜色34': f"{uuid.uuid4()}"}
    , {'自定义颜色35': f"{uuid.uuid4()}"}, {'自定义颜色36': f"{uuid.uuid4()}"}, {'自定义颜色37': f"{uuid.uuid4()}"},
              {'自定义颜色38': f"{uuid.uuid4()}"}]


def get_color(num):
    if num > len(color_list):
        for i in range(len(color_list), num):
            color_list.append({f'自定义颜色{i}': f"{uuid.uuid4()}"})
    return random.sample(color_list, num)


def is_number(s):
    try:
        if '.' in s:
            return float(s)
        else:
            return int(s)
    except ValueError:
        return s


class ECProServer(object):
    def __init__(self, httpUtil):
        global http
        http = httpUtil

    def _init_data(self):
        pass

    def getExportRecording(self, token):
        INFO('调用 获取导出记录 接口')
        from utils.globals import SECRET
        murl = '%s/%s' % (SECRET, 'slice_export')

        res = http.get(murl, token)
        try:
            return json.loads(res)
        except:
            print('getExportRecording return:%s' % res)

    def deleteExportRecording(self, record_id, token):
        INFO('调用 删除导出记录 接口')
        from utils.globals import SECRET
        murl = '%s/%s' % (SECRET, 'slice_export')
        body = {}
        body['record_ids'] = record_id
        res = http.delete(murl, token, json.dumps(body))
        try:
            return json.loads(res)
        except:
            self.fail('deleteExportRecording return:%s' % res)


    def createDetailsPage(self, token, image_package_id, template_ids, model_ids, product_id):
        INFO('调用 生成详情页 接口')
        from utils.globals import PAGE
        murl = '%s/%s' % (PAGE, 'create')
        body = {}
        alist = []
        body['product_id'] = product_id
        body['image_package_id'] = image_package_id
        body['template_ids'] = template_ids
        body['model_ids'] = model_ids
        body['note'] = 'mao_auto_create'
        alist.append(body)
        print(json.dumps(alist))
        res = http.request(murl, token, json.dumps(alist))
        try:
            return json.loads(res)
        except:
            self.fail('createDetailsPage return:%s' % res)

    def getOneDetailsPage(self, token, document_id):
        INFO('调用 获取单条详情页详情 接口')
        from utils.globals import SECRET
        murl = '%s/%s' % (SECRET, document_id)
        res = http.get(murl, token)
        try:
            return json.loads(res)
        except:
            self.fail('getOneDetailsPage return:%s' % res)

    def getMoreDetailsPage(self):
        pass

    def exportDetailsPage(self, token, document_ids, imgFormat, width, sliceType, isLimitMaxHeight, maxHeight, height,
                          isLimitCount, count, isCompress, compressSize):
        INFO('调用 倒出详情页 接口')
        from utils.globals import SECRET
        murl = '%s/%s' % (SECRET, 'slice_export')
        body = {}
        export_data = {}
        document_List = []
        document_ids = is_number(document_ids)
        isLimitMaxHeight = is_number(isLimitMaxHeight)
        maxHeight = is_number(maxHeight)
        height = is_number(height)
        count = is_number(count)
        compressSize = is_number(compressSize)

        document_List.append(document_ids)
        body['document_ids'] = document_List
        export_data['imgFormat'] = imgFormat
        export_data['width'] = width
        export_data['sliceType'] = sliceType
        export_data['isLimitMaxHeight'] = isLimitMaxHeight
        export_data['maxHeight'] = maxHeight
        export_data['height'] = height
        export_data['isLimitCount'] = isLimitCount
        export_data['count'] = count
        export_data['isCompress'] = isCompress
        export_data['compressSize'] = compressSize

        body['export_data'] = json.dumps(export_data)
        print(json.dumps(body))
        res = http.request(murl, token, json.dumps(body))
        try:
            return json.loads(res)
        except:
            self.fail('exportDetailsPage return:%s' % res)

    def exportSettings(self, name, token, imgFormat, width, sliceType, isLimitMaxHeight, maxHeight, height,
                       isLimitCount, count, isCompress, compressSize, default):
        INFO('调用 添加导出规则 接口')
        from utils.globals import EXPORT
        murl = '%s/%s' % (EXPORT, 'export_settings')
        body = {}
        data = {}
        isLimitMaxHeight = is_number(isLimitMaxHeight)
        maxHeight = is_number(maxHeight)
        height = is_number(height)
        count = is_number(count)
        compressSize = is_number(compressSize)
        default = is_number(default)

        body['name'] = name
        data['imgFormat'] = imgFormat
        data['width'] = width
        data['sliceType'] = sliceType
        data['isLimitMaxHeight'] = isLimitMaxHeight
        data['maxHeight'] = maxHeight
        data['height'] = height
        data['isLimitCount'] = isLimitCount
        data['count'] = count
        data['isCompress'] = isCompress
        data['compressSize'] = compressSize

        body['data'] = json.dumps(data)
        body['default'] = default
        print(json.dumps(body))
        res = http.request(murl, token, json.dumps(body))
        try:
            return json.loads(res)
        except:
            self.fail('exportSettings return:%s' % res)

    def createPeriod(self, token, period, period_describe):
        INFO('调用 创建期数 接口')
        from utils.globals import SECRET
        murl = '%s%s' % (SECRET, '/v2/period')
        body = {}
        body['period'] = period
        body['period_describe'] = period_describe
        print(body)
        res = http.request(murl, token, json.dumps(body))
        try:
            return json.loads(res)
        except:
            self.fail('createPeriod return:%s' % res)

    def relation(self, token, product_id, package_id, cover_image):
        INFO('调用 关联图片包 接口')
        from utils.globals import SECRET
        murl = '/merchant/picture-packages/products/associate'
        body = {}
        body_list = []
        body['product_id'] = product_id
        body['package_id'] = package_id
        body['cover_image'] = cover_image
        body_list.append(body)
        bodys = {}
        bodys['products'] = body_list
        print('guanlian', bodys)
        res = http.request(murl, token, json.dumps(bodys))
        print('fnahui', res)
        try:
            return json.loads(res)
        except:
            self.fail('relation return:%s' % res)

    def setresources(self, token, product_id):
        INFO('调用 提交资源图 接口')
        mmurl = '/merchant/products/%s' % product_id
        seturl = '/merchant/products/%s/media' % product_id
        print('lianjie', mmurl, seturl)
        res = http.get(mmurl, token)
        print('ziyuantu', res)
        res = json.loads(res)
        if res['message'] == 'Success':
            data = res['data']['media']
            media = data['data']
        media_data = list(media)
        media_data.insert(0, '{"product_media":')
        media_data.append(',"created_type":"save"}')
        media_data = ''.join(media_data)  # 转化回来
        bodys = media_data
        print('bodys', bodys)
        res = http.request_put(seturl, token, json.dumps(bodys))
        try:
            return json.loads(res)
        except:
            self.fail('relation return:%s' % res)

    def createProduct(self, token, category_id, category_path, codes, tp_ids, period_id):
        INFO('调用 批量创建商品 接口')
        from utils.globals import SECRET
        murl = '%s%s' % (SECRET, '/v2/products')
        body = {}
        body['category_id'] = int(category_id)
        body['category_path'] = category_path
        body['period_id'] = period_id
        body['codes'] = codes
        body['tp_ids'] = tp_ids
        print(json.dumps(body))
        res = http.request(murl, token, json.dumps(body))
        try:
            return json.loads(res)
        except:
            self.fail('createProduct return:%s' % res)

    def getAttr(self, token, tp_ids, category_id):
        INFO('调用 获取商品属性 接口')
        from utils.globals import ATTR
        murl = '%s/%s/props_form?tp_ids=%s' % (ATTR, category_id, ','.join(tp_ids))
        res = http.get(murl, token)
        try:
            return json.loads(res)
        except:
            return res

    def setJosn(self, codes, res, category_id, tp_ids, periodId, period, period_describe, token, category_path,
                filename):
        if res['message'] == 'Success':
            body = {}
            info = []
            att = {}
            options_data = {}
            att_grandchild = {}
            att_children = {}
            att_children_no = {}
            att_data_grandchild_data = {}
            size_table = []
            specs = []
            body['created_type'] = 'save'
            body['period_describe'] = '%s %s' % (period, period_describe)
            body['price'] = 1111
            body['category_id'] = int(category_id)
            body['tp_ids'] = [int(tp_id) for tp_id in tp_ids]
            body['whole_sale_info'] = {
                "quoteType": "1",
                "saleType": "normal",
                "minOrderQuantity": 2
            }
            sku_table_list = []
            for field in res['data']:
                if field['name'] == 'basic':
                    body['title'] = '测试类目:%s' % category_path.split('>>')[-1]
                    name = category_path.split('>>')[0].strip()
                    #if '/' in name:
                    #    name = name.split('/')[0]
                    # body['code'] = '扩展2-2期%s%s' % (name, str(codes[0]))
                    # body['code'] = codes[0]
                    # body['code'] = 'nv1211en%s' % (time.strftime('%H%M%S', time.localtime(time.time())))
                    body['code'] = codes[0]
                    body['period_id'] = periodId

                elif field['name'] == 'sales':
                    res_size = []
                    res_color = get_color(2)
                    file_path = os.path.join(TEST_DATA_DIR, filename.split('.')[0], '资源图')
                    filelist = os.listdir(file_path)
                    change_clolr_list = []
                    for color in res_color:
                        for key, value in color.items():
                            change_clolr_list.append(key)
                    colour_prefix_list = ['y','bm','xj','dc']
                    for colour_prefix in colour_prefix_list:
                        times = 0
                        for pic in filelist:
                            if pic.startswith(colour_prefix):
                                try:
                                    os.chdir(file_path)
                                    print('---///',pic, '%s%s.jpg' % (colour_prefix, change_clolr_list[times]))
                                    os.rename(pic, '%s%s.jpg' % (colour_prefix, change_clolr_list[times]))
                                    times += 1
                                except:
                                    pass

                    for num in range(1, 6):
                        times = 0
                        for pic in filelist:
                            suffix = "(%s).jpg" % num
                            if pic.endswith(suffix) and pic.startswith("vipd"):
                                try:
                                    os.chdir(file_path)
                                    print('--->>',pic, 'vipd%s(%s).jpg' % (change_clolr_list[times], num))
                                    os.rename(pic, 'vipd%s(%s).jpg' % (change_clolr_list[times], num))
                                    times += 1
                                except:
                                    pass

                    os.chdir(TEST_DATA_DIR)
                    with zipfile.ZipFile(filename, 'w') as f:
                        for d in os.listdir(file_path):
                            f.write(file_path + os.sep + d, '资源图' + os.sep + d)
                    f.close()

                    for fields in field['fields']:
                        if fields['label'] == '颜色':
                            specs_color_dict = {}
                            specs_color_dict['prop_id'] = str(fields['prop_id'])
                            specs_color_dict['prop_name'] = fields['label']
                            specs_color_dict['spec_type'] = 'color'
                            specs_color_dict['position'] = 1
                            spec_color_values = []
                            count = 0
                            for color in res_color:
                                for key, value in color.items():
                                    count += 1
                                    spec_values_color_dict = {}
                                    spec_values_color_dict['prop_value_id'] = str(value)
                                    spec_values_color_dict['prop_value_name'] = str(key)
                                    spec_values_color_dict['remark'] = ''
                                    spec_values_color_dict['ext'] = ''
                                    spec_values_color_dict['image_url'] = ''
                                    spec_values_color_dict['position'] = count
                                    spec_values_color_dict['number'] = f"{uuid.uuid4()}"
                                    spec_color_values.append(spec_values_color_dict)
                            specs_color_dict['spec_values'] = spec_color_values
                            specs.append(specs_color_dict)
                        if fields['label'] == '尺码':
                            res_size = self.getSize(category_id, fields['id'], tp_ids, token, 5)
                            specs_size_dict = {}
                            specs_size_dict['prop_id'] = str(fields['prop_id'])
                            specs_size_dict['sizePropId'] = fields['id']
                            specs_size_dict['spec_type'] = 'size'
                            specs_size_dict['prop_name'] = fields['label']
                            specs_size_dict['position'] = 2
                            spec_size_values = []
                            count = 0
                            for size in res_size:
                                for key, value in size.items():
                                    count += 1
                                    spec_values_size_dict = {}
                                    spec_values_size_dict['group_name'] = '中国码'
                                    spec_values_size_dict['prop_value_id'] = str(value)
                                    spec_values_size_dict['prop_value_name'] = str(key)
                                    spec_values_size_dict['remark'] = ''
                                    spec_values_size_dict['ext'] = ''
                                    spec_values_size_dict['image_url'] = ''
                                    spec_values_size_dict['position'] = count
                                    spec_size_values.append(spec_values_size_dict)
                                specs_size_dict['spec_values'] = spec_size_values
                            specs.append(specs_size_dict)

                        if fields['label'] == '参考身高':
                            res_size = self.getSize(category_id, fields['id'], tp_ids, token, 2)
                            specs_size_dict = {}
                            specs_size_dict['prop_id'] = str(fields['prop_id'])
                            specs_size_dict['sizePropId'] = fields['id']
                            specs_size_dict['spec_type'] = 'height'
                            specs_size_dict['prop_name'] = fields['label']
                            specs_size_dict['position'] = 2
                            spec_size_values = []
                            count = 0
                            for size in res_size:
                                for key, value in size.items():
                                    count += 1
                                    spec_values_size_dict = {}
                                    spec_values_size_dict['group_name'] = '中国码'
                                    spec_values_size_dict['prop_value_id'] = str(value)
                                    spec_values_size_dict['prop_value_name'] = str(key)
                                    spec_values_size_dict['remark'] = ''
                                    spec_values_size_dict['ext'] = ''
                                    spec_values_size_dict['image_url'] = ''
                                    spec_values_size_dict['position'] = count
                                    spec_size_values.append(spec_values_size_dict)
                                specs_size_dict['spec_values'] = spec_size_values
                            specs.append(specs_size_dict)

                        if fields['label'] == 'SKU表':
                            position = 0
                            for color in res_color:
                                for color_key, color_values in color.items():
                                    for size in res_size:
                                        for size_key, size_values in size.items():
                                            sku_table_dict = {}
                                            sku_table_info = []
                                            position += 1
                                            sku_table_dict['position'] = position
                                            sku_table_dict['spec_value_first_id'] = str(color_values)
                                            sku_table_dict['spec_value_second_id'] = str(size_values)
                                            for field in fields['sub_props']:
                                                sku_table_info_dict = {}
                                                sku_table_info_dict['id'] = field['id']
                                                sku_table_info_dict['field_set'] = field['field_set']
                                                sku_table_info_dict['uuid'] = f"{uuid.uuid4()}"
                                                sku_table_info_dict['prop_id'] = field['prop_id']

                                                if field['label'] == '天猫上市时间':
                                                    sku_table_info_dict['text'] = '2021-02-25T03:17:40.918Z'
                                                elif field['label'] == '唯品会条码':
                                                    sku_table_info_dict['text'] = f"{uuid.uuid4()}"
                                                elif field['label'] == '拼多多单买价':
                                                    sku_table_info_dict['text'] = '900'
                                                elif field['label'] == '拼多多团购价':
                                                    sku_table_info_dict['text'] = '800'
                                                elif field['label'] == '京东自营市场价':
                                                    sku_table_info_dict['text'] = '1112'
                                                elif field['label'] == '采购价':
                                                    sku_table_info_dict['text'] = '1110'
                                                elif field['label'] == '京东自营货号':
                                                    #sku_table_info_dict['text'] = codes[0]
                                                    sku_table_info_dict['text'] = 'ECPRO123'
                                                elif field['label'] == '商家编码':
                                                    sku_table_info_dict['text'] = ''
                                                elif field['label'] == '商品条形码':
                                                    if '1011' in tp_ids:
                                                        sku_table_info_dict['text'] = f"{uuid.uuid4().hex}"[:32]
                                                    else:
                                                        sku_table_info_dict['text'] = ''
                                                    # 爱库存平台，有商品条形码，校验
                                                    # sku_table_info_dict['text'] = f"{uuid.uuid4()}".replace('-', '')[0:32]
                                                    # sku_table_info_dict['text'] = f"{uuid.uuid4().hex}"[:32]
                                                    # sku_table_info_dict['text'] = ''
                                                elif field['label'] == '划线价说明':
                                                    sku_table_info_dict['text'] = '吊牌价'
                                                else:
                                                    sku_table_info_dict['text'] = '1111'

                                                sku_table_info.append(sku_table_info_dict)
                                            sku_table_dict['info'] = json.dumps(sku_table_info)
                                            sku_table_list.append(sku_table_dict)
                    body['sku_table'] = sku_table_list
                    body['specs'] = specs

                elif field['name'] == 'size':
                    for fields in field['fields']:
                        prop_values = []
                        size = {}
                        sub_props = fields['sub_props']
                        size['id'] = fields['id']
                        size['label'] = fields['label']
                        size['require'] = True
                        size['field_set'] = 'size'
                        size['uuid'] = f"{uuid.uuid4()}"
                        for item in res_size:
                            for key, value in item.items():
                                prop_values_dict = {}
                                sub = []
                                prop_values_dict['firstColProps'] = key
                                for sub_prop in sub_props:
                                    sub_dict = {}
                                    sub_dict['id'] = sub_prop['id']
                                    sub_dict['field_set'] = sub_prop['field_set']
                                    sub_dict['require'] = sub_prop['required']
                                    sub_dict['uuid'] = f"{uuid.uuid4()}"
                                    if sub_prop['label'] == '号型':
                                        sub_dict['prop_values'] = [{"text": "170/65A"}]
                                    else:
                                        sub_dict['prop_values'] = [{"text": "60"}]
                                    sub_dict['uuid'] = f"{uuid.uuid4()}"
                                    sub.append(sub_dict)
                                prop_values_dict['sub_props'] = sub
                                prop_values.append(prop_values_dict)
                                size['prop_values'] = prop_values
                        size_table.append(size)
                    body['size_table'] = json.dumps(size_table)

                elif field['name'] == 'properties':
                    label_list = ['淘宝标题', '天猫标题', '京东标题', '拼多多标题', '唯品会标题', '有赞标题', '快手标题', '抖音标题', '京东自营标题', '爱库存标题']
                    for fields in field['fields']:
                        info_dict = {}
                        info_dict_son = {}
                        info_dict_grand = {}
                        if fields['field_type'] == 'input':
                            info_dict['id'] = fields['id']
                            info_dict['field_set'] = 'properties'
                            info_dict['uuid'] = f"{uuid.uuid4()}"
                            info_dict['value_type'] = fields['value_type']
                            info_dict['tp_id'] = fields['tp_id']
                            info_dict['_options_display'] = True
                            for label in label_list:
                                if fields['label'] == label:
                                    info_dict['prop_values'] = [{"text": "%s" % ('测试类目:' + category_path.split('>>')[-1])}]
                                    info.append(info_dict)
                            if fields['value_type'] == 'text':
                                info_dict['prop_values'] = [{"text": "%s" % '自动创建属性值'}]
                                info.append(info_dict)
                            elif fields['value_type'] == 'integer':
                                info_dict['prop_values'] = [{"text": "1111"}]
                                info.append(info_dict)
                            elif fields['value_type'] == 'decimal':
                                info_dict['prop_values'] = [{"text": "1111"}]
                                info.append(info_dict)
                            elif fields['value_type'] == 'url':
                                info_dict['prop_values'] = [{"text": ""}]
                                info.append(info_dict)
                            else:
                                info_dict['prop_values'] = [{"text": '自动创建属性：%s' % fields['label']}]
                                info.append(info_dict)
                        elif fields['field_type'] == 'textarea':
                            info_dict['id'] = fields['id']
                            info_dict['field_set'] = 'properties'
                            info_dict['uuid'] = f"{uuid.uuid4()}"
                            info_dict['value_type'] = fields['value_type']
                            info_dict['tp_id'] = fields['tp_id']
                            info_dict['_options_display'] = True
                            info_dict['prop_values'] = [{"text": "%s" % (fields['label'] + '自动创建属性')}]
                            info.append(info_dict)

                        elif fields['field_type'] == 'radio':
                            val = self.getValues(category_id, fields['id'], token, 1)
                            info_dict['id'] = fields['id']
                            info_dict['field_set'] = 'properties'
                            info_dict['uuid'] = f"{uuid.uuid4()}"
                            info_dict['value_type'] = fields['value_type']
                            info_dict['tp_id'] = fields['tp_id']
                            info_dict['prop_values'] = [{"id": val[0]['id'], "text": val[0]['text']}]
                            info.append(info_dict)

                        elif fields['field_type'] == 'select':
                            val = self.getValues(category_id, fields['id'], token, 1)
                            val_all = self.getValues_all(category_id, fields['id'], token)

                            if val[0]['options'] is None:
                                info_dict['id'] = fields['id']
                                info_dict['field_set'] = 'properties'
                                info_dict['uuid'] = f"{uuid.uuid4()}"
                                info_dict['value_type'] = fields['value_type']
                                info_dict['tp_id'] = fields['tp_id']
                                info_dict['_options_display'] = True
                                info_dict['prop_values'] = [{"id": val[0]['id'], "text": val[0]['text']}]
                                att[fields['id']] = val[0]['text']
                                info.append(info_dict)

                            # 去除属性值为空的属性
                            elif val is None:
                                info_dict['id'] = fields['id']
                                info_dict['field_set'] = 'properties'
                                info_dict['uuid'] = f"{uuid.uuid4()}"
                                info_dict['value_type'] = fields['value_type']
                                info_dict['tp_id'] = fields['tp_id']
                                info_dict['_options_display'] = True
                                info_dict['prop_values'] = []
                                info.append(info_dict)

                            # 把所有带联动属性，都放到options_data字典里
                            elif val[0]['options'] is not None:
                                for val_data in val_all:
                                    if val_data['options'] is not None:
                                        if fields['id'] not in options_data:
                                            options_data[fields['id']] = list()
                                            options_data[fields['id']].append(val_data)
                                        else:
                                            options_data[fields['id']].append(val_data)

                        elif fields['field_type'] == 'checkbox':
                            val = self.getValues(category_id, fields['id'], token, 2)
                            if val:
                                check_list = []
                                info_dict['id'] = fields['id']
                                info_dict['field_set'] = 'properties'
                                info_dict['uuid'] = f"{uuid.uuid4()}"
                                info_dict['value_type'] = fields['value_type']
                                info_dict['tp_id'] = fields['tp_id']
                                info_dict['_options_display'] = True
                                for item in val:
                                    check_list.append({"id": item['id'], "text": item['text']})
                                    info_dict['prop_values'] = check_list
                                info.append(info_dict)

                        elif fields['field_type'] == 'tb-material' or fields['field_type'] == 'tb-material-inner':
                            sub_props = {}
                            for i in fields['sub_props']:
                                if i['field_type'] == 'select':
                                    sub_props['sub_props_id'] = i['id']
                                elif i['field_type'] == 'input':
                                    sub_props['sub_props_val_id'] = i['id']

                            val = self.getValues(category_id, sub_props['sub_props_id'], token, 1)
                            if val:
                                info_dict['id'] = fields['id']
                                info_dict['field_set'] = 'properties'
                                info_dict['uuid'] = f"{uuid.uuid4()}"
                                info_dict['value_type'] = fields['value_type']
                                info_dict['tp_id'] = fields['tp_id']
                                info_dict['_options_display'] = True
                                info_dict['prop_values'] = [{"sub_props": [{"id": sub_props['sub_props_id'],
                                                                            "uuid": f"{uuid.uuid4()}",
                                                                            "prop_values": [
                                                                                {"id": val[0]['id'],
                                                                                 "text": val[0]['text']}],
                                                                            '_options_display': True},
                                                                           {"id": sub_props['sub_props_val_id'],
                                                                            "uuid": f"{uuid.uuid4()}",
                                                                            "prop_values": [{"text": "100.00"}],
                                                                            '_options_display': True}]}]

                            info.append(info_dict)

                    # 从所有带联动属性的中，分为二级联动属性和三级联动属性
                    if options_data:
                        for fields_id, options_value in options_data.items():
                            for val_options_data in options_value:
                                options = val_options_data['options']
                                # 上面1688 下面拼多多
                                # options: "{\"disable\": {\"$op\": \"nin\", \"$params\": [{\"$op\": \"valueOf\", \"$params\": [\"1367173\"]}, [\"国风复古\"]]}}"
                                # options: "{\"disable\": {\"$op\": \"and\", \"$params\": [[{\"$op\": \"nin\", \"$params\": [{\"$op\": \"valueOf\", \"$params\": [1318982]}, [\"化纤\", \"其它\", \"网纱\"]]}]]}}"
                                optionss = json.loads(options)["disable"]["$params"][1][0]

                                parent_id = int(json.loads(options)["disable"]["$params"][0]["$params"][0])

                                parent_select_value = att.get(parent_id)
                                if parent_select_value in optionss:
                                    if parent_id not in att_children:
                                        att_children[parent_id] = list()
                                        att_children[parent_id].append({fields_id: ({val_options_data['id']: val_options_data['text']})})
                                    else:
                                        att_children[parent_id].append({fields_id: ({val_options_data['id']: val_options_data['text']})})
                                elif parent_select_value not in optionss:
                                    if parent_id not in att_children_no:
                                        att_children_no[parent_id] = list()
                                        att_children_no[parent_id].append({fields_id: ({'id': ({val_options_data['id']: val_options_data['text']}),'options': options})})
                                    else:
                                        att_children_no[parent_id].append({fields_id: ({'id':({val_options_data['id']: val_options_data['text']}), 'options':options})})
                                else:
                                    continue

                    # 查找出二级联动属性，并拼到info大字典里
                    if att_children:
                        for att_key, att_value in att_children.items():
                            if len(att_children[att_key]) > 0:
                                children_data = random.choice(att_children[att_key])
                                children_id = [i for i in children_data.keys()][0]
                                children_text = [i for i in children_data.values()][0]
                                for children_key, children_value in children_text.items():
                                    info_dict_son['id'] = children_id
                                    info_dict_son['field_set'] = 'properties'
                                    info_dict_son['uuid'] = f"{uuid.uuid4()}"
                                    info_dict_son['value_type'] = 'text'
                                    info_dict_son['tp_id'] = fields['tp_id']
                                    info_dict_son['_options_display'] = True
                                    info_dict_son['prop_values'] = [{"id": children_key, "text": children_value}]
                                    import copy
                                    deep_info_dict = copy.deepcopy(info_dict_son)
                                    info.append(deep_info_dict)
                                    att_grandchild[children_id] = children_text

                    # 查找出三级联动属性
                    if att_children_no:
                        for att_key_no, att_value_no in att_children_no.items():
                            for att_value_san in att_value_no:
                                for att_value_san_key, att_value_san_value in att_value_san.items():
                                    options = att_value_san_value["options"]
                                    optionss = json.loads(options)["disable"]["$params"][1][0]
                                    parent_id = int(json.loads(options)["disable"]["$params"][0]["$params"][0])
                                    for att_grandchild_key, att_grandchild_value in att_grandchild.items():
                                        for att_grandchild_value_key, att_grandchild_value_value in att_grandchild_value.items():
                                            if parent_id == att_grandchild_key and att_grandchild_value_value in optionss:
                                                if att_value_san_key not in att_data_grandchild_data:
                                                    att_data_grandchild_data[att_value_san_key] = list()
                                                    att_data_grandchild_data[att_value_san_key].append(att_value_san_value['id'])
                                                else:
                                                    att_data_grandchild_data[att_value_san_key].append(att_value_san_value['id'])
                                    else:
                                        continue

                    # 将三级联动属性的列表，随机取值，然后拼到info大字典里
                    if att_data_grandchild_data:
                        for att_data_grandchild_data_key, att_data_grandchild_data_value in att_data_grandchild_data.items():
                            grandchild_data = random.choice(att_data_grandchild_data_value)
                            for data_key, data_value in grandchild_data.items():
                                info_dict_grand['id'] = att_data_grandchild_data_key
                                info_dict_grand['field_set'] = 'properties'
                                info_dict_grand['uuid'] = f"{uuid.uuid4()}"
                                info_dict_grand['value_type'] = 'text'
                                info_dict_grand['tp_id'] = fields['tp_id']
                                info_dict_grand['_options_display'] = True
                                info_dict_grand['prop_values'] = [{"id": data_key, "text": data_value}]
                                import copy
                                deep_info_dict_grand = copy.deepcopy(info_dict_grand)
                                info.append(deep_info_dict_grand)

                    body['info'] = json.dumps(info)
                print(json.dumps(body))
            return body
        else:
            return '请求错误，请检查平台id或属性id是否正确'

    def getSize(self, category_id, attr_ids, tp_ids, token, num=1):
        INFO('调用 获取商品尺码 接口')
        murl = '/catalog/categories/%s/props/%s/prop_values?tp_ids=%s' % (category_id, attr_ids, ','.join(tp_ids))
        res = http.get(murl, token)
        # print(json.loads(res))
        textlist = []
        childrenlist = []
        boylist = []
        girllist = []
        res = json.loads(res)
        if res['message'] == 'Success':
            res = res['data']['prop_values']
            for i in res:
                if i['group_name'] == '中国码':
                    if '大码' not in i['text'] and '加大' not in i['text']:
                        textlist.append({i['text']: i['prop_value_id']})
        # 唯品会蓝地女装，唯品会班尼路童装 男装，特殊的校验，传别的尺码上不去货
        # 设置童装 100 110 120
        for i in textlist:
            if '100' in i or '100cm' in i:
                childrenlist.append(i)
            elif '110' in i or '110cm' in i:
                childrenlist.append(i)
            elif '120' in i or '120cm' in i:
                childrenlist.append(i)
        # 设置男装 XS M L XL
        for i in textlist:
            if 'XS' in i :
                boylist.append(i)
            elif 'M' in i :
                boylist.append(i)
            elif 'L' in i :
                boylist.append(i)
            elif 'XL' in i :
                boylist.append(i)
        # 设置女装 S M
        for i in textlist:
            if 'S' in i :
                girllist.append(i)
            elif 'M' in i :
                girllist.append(i)

        num_list = []
        for i in range(num):
            num_list.append(random.randrange(0, len(textlist)))
        num_list_new = []
        for i in num_list:
            if i not in num_list_new:
                num_list_new.append(i)
        num_list_new.sort()
        size_list = []
        for i in num_list_new:
            size_list.append(textlist[i])
        # size_list = childrenlist
        # size_list = boylist
        # size_list = girllist
        # print(size_list)
        return size_list

    def checkTpid(self, category_id, tp_ids, token):
        INFO('调用 校验平台 接口')
        murl = '/catalog/categories/%s/mappings?tp_ids=%s' % (category_id, ','.join(tp_ids))
        res = http.get(murl, token)
        tp_ids = []
        res = json.loads(res)
        if res['message'] == 'Success':
            for i in res['data']['mappings']:
                if i['tp_category']:
                    tp_ids.append(str(i['tp_id']))
        return tp_ids

    def getValues(self, category_id, attr_ids, token, num=1):
        INFO('调用 获取商品属性值 接口')
        murl = '/catalog/tps/0/tp_categories/%s/tp_props/%s/tp_prop_values' % (category_id, attr_ids)
        res = http.get(murl, token)
        textlist = []
        res = json.loads(res)
        if res['message'] == 'Success':
            res = res['data']['tp_prop_values']
            for i in res:
                textlist.append(i)
        try:
            return random.sample(textlist, num)
        except:
            INFO('checkbox属性不足3个，默认选择1个')
            try:
                return random.sample(textlist, 1)
            except:
                error = '属性值为空：类目id：%s，属性id：%s' % (category_id, attr_ids)
                ERROR(error)
                writeFile('noneValues', '%s:%s' % (time.strftime('%Y-%m-%d-%H', time.localtime(time.time())), error))
                return None

    def getValues_all(self, category_id, attr_ids, token):
        INFO('调用 获取商品属性值 接口')
        murl = '/catalog/tps/0/tp_categories/%s/tp_props/%s/tp_prop_values' % (category_id, attr_ids)
        res = http.get(murl, token)
        textlist = []
        res = json.loads(res)
        if res['message'] == 'Success':
            res = res['data']['tp_prop_values']
            for i in res:
                textlist.append(i)
        # print('textlist', textlist)
        return textlist


    def getValueAndId(self, category_id, attr_ids, token, num=1):
        INFO('调用 获取商品属性值 接口')
        murl = '/catalog/tps/0/tp_categories/%s/tp_props/%s/tp_prop_values' % (category_id, attr_ids)
        res = http.get(murl, token)
        textlist = []
        res = json.loads(res)
        if res['message'] == 'Success':
            res = res['data']
            for i in res:
                textlist.append({i['tp_prop_values'], i['id']})
        try:
            return random.sample(textlist, num)
        except:
            INFO('checkbox属性不足3个，默认选择1个')
            try:
                return random.sample(textlist, 1)
            except:
                error = '属性值为空：类目id：%s，属性id：%s' % (category_id, attr_ids)
                ERROR(error)
                writeFile('noneValues', '%s:%s' % (time.strftime('%Y-%m-%d-%H', time.localtime(time.time())), error))
                return None

    def submitProduct(self, token, josnstr, productId):
        INFO('调用 提交商品 接口')
        from utils.globals import SECRET
        murl = '%s%s/%s/props' % (SECRET, '/v2/products', productId)
        res = http.request(murl, token, json.dumps(josnstr))
        try:
            return json.loads(res)
        except:
            self.fail('createProduct return:%s' % res)

    def uploadFile(self, token, filename, product_id, group_id, serverurl):
        INFO('调用 上传图片包接口 接口')
        from encapsulation.upload_file import upload_zip
        res = upload_zip(filename, product_id, group_id, token, os.path.join(TEST_DATA_DIR, filename), serverurl)
        res = json.loads(res)
        image_package_id = res['data']['id']

        if res['message'] == 'Success':
            task_id = res['data']['id']
            res = True
            while res:
                res = self.checkUpload(token, task_id)
                status = res['data']['status']
                if status == 'finished' or status == 'timeout' or status == 'unpacked':
                    cover_image = res['data']['cover_image']
                    res = False
                else:
                    continue
            return status, image_package_id, cover_image

    def checkUpload(self, token, task_id):
        from utils.globals import STORAGE
        INFO('调用 调用查询上传结果接口 接口')
        murl = '%s/%s/%s' % (STORAGE, 'zip', task_id)
        res = http.get(murl, token)
        res = json.loads(res)
        return res

    def LoadingProduct(self, tp_id, brand_id, shop_id, product_id, document_ids, batch_info_id, backup_code,
                       shipping_template_id, main_video_id
                       , shop_categories, water_mark_id):
        from utils.globals import SECRET
        INFO('调用 调用上货 接口')
        murl = '%s/%s/%s' % (SECRET, 'publish')
        body = {}
        alist = []
        body['tp_id'] = tp_id
        body['shop_id'] = shop_id
        body['brand_id'] = brand_id
        body['document_ids'] = document_ids
        body['product_id'] = product_id
        body['batch_info_id'] = batch_info_id
        body['backup_code'] = backup_code
        body['shipping_template_id'] = shipping_template_id
        body['main_video_id'] = main_video_id
        body['shop_categories'] = shop_categories
        body['water_mark_id'] = water_mark_id
        alist.append(body)

        res = http.request(murl, token, json.dumps(alist))
        print(res, 432424242)
        try:
            return json.loads(res)
        except:
            self.fail('LoadingProduct return:%s' % res)
