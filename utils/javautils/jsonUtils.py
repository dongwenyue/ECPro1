# -*- coding: utf-8 -*-
'''
@author: wsy
'''
from utils.javautils.JClass import GsonBuilder, Gson, TypeToken


def Object2JSON2(obj):
    return GsonBuilder().serializeNulls().disableHtmlEscaping().create().toJson(obj)


def JSON2Object(json, valueType):
    valueClassName = valueType.getName()
    if 'map' in valueClassName.toLowerCase():
        return Gson().fromJson(json, TypeToken().getType())
    else:
        return Gson().fromJson(json, valueType)
