'''
@author: wangsiyu
'''


def java_str2bytes(inData):
    import jpype
    if inData != None:
        arr_cls = jpype.JArray(jpype.JByte)
        java_arr = arr_cls(inData.encode())
        return java_arr
    return None


def java_Exception2py(e):
    from jpype import JavaException
    if e != None:
        return JavaException.message()
    return None


def java_bytes2str(inData):
    import jpype
    if inData != None:
        javaClass = jpype.JClass('java.lang.String')
        javaStr = javaClass(inData)
        return javaStr.toString()
    return None


def covert_Jlist2Plist(jList):
    ret = []
    if jList is None:
        return ret
    for i in range(jList.size()):
        ret.append(str(jList.get(i)))
    return ret


def covert_PlistTOJlist(pList):
    import jpype
    arryList = jpype.JClass('java.util.ArrayList')
    ret = arryList()
    for i in range(len(pList)):
        ret.add(pList[i])
    return ret
