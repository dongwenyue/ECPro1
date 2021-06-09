from configparser import ConfigParser


def getConfigs(config):
    configs = ConfigParser()
    configs.read(config)
    return configs


def InitConfigs(config):
    configs = ConfigParser()
    configs.read(config)
    from ..globals import SET_SECRET,SET_EXPORT,SET_ATTR,SET_ATTRVALUE,SER_STORAGE,SER_PAGE
    SET_SECRET(configs.get('server', 'secret'))
    SET_EXPORT(configs.get('server', 'export'))
    SET_ATTR(configs.get('server', 'attr'))
    SET_ATTRVALUE(configs.get('server', 'attrValue'))
    SER_STORAGE(configs.get('server', 'storage'))
    SER_PAGE(configs.get('server', 'page'))
    return configs
