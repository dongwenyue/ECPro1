from configparser import ConfigParser


def getConfigs(config):
    configs = ConfigParser()
    configs.read(config)
    return configs


def InitConfigs(config):
    configs = ConfigParser()
    configs.read(config)
    from ..globals import SET_SECRET
    SET_SECRET(configs.get('server', 'secret'))
    return configs
