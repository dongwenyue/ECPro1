import json


def is_json(myjson):
    if not type(myjson) == type({'': ''}):
        return False
    return True


def is_containJson(strMsg):
    if '{' in strMsg and '}' in strMsg:
        myjson = getJson(strMsg)
        try:
            myjson = json.loads(myjson)
            return True
        except Exception:
            return False
    return False


def getJson(strMsg):
    return fomartImageInJson(strMsg[strMsg.find('{'):strMsg.rfind('}') + 1])


def jsonFomart(strJson):
    myJson = json.loads(strJson)
    return json.dumps(myJson, sort_keys=True, indent=2)


def fomartJsonFromStr(strMsg):
    return strMsg[0:strMsg.find('{')] + '\n' + jsonFomart(getJson(strMsg))


def fomartJsonFromStr4Html(strMsg):
    strMsg = strMsg[0:strMsg.find('{')] + '<br>' + jsonFomart(getJson(strMsg))
    strMsg = strMsg.replace('\n', '<br>')
    strMsg = strMsg.replace(' ', '&nbsp;&nbsp;&nbsp;&nbsp;')
    return strMsg


def fomartImageInJson(strMsg):
    try:
        htmlJson = json.loads(strMsg.replace('\\', ''))
    except:
        return

    imageKeyWords = ['idcard_negtive', 'idcard_positive', 'image', 'signImage']
    for keyword in imageKeyWords:
        if keyword in htmlJson.keys():
            htmlJson[keyword] = '<img src="data:image/png;base64,%s"/> ' % htmlJson[keyword]
    return json.dumps(htmlJson)
