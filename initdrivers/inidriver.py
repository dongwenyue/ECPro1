def initdriver(inidata):
    from configparser import ConfigParser
    global configs
    configs = ConfigParser()
    configs.read(inidata)


def getdata(tag, case):
    return (configs.get(tag, case)).decode('utf-8')
