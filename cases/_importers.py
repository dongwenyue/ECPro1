from utils.configures.paths import *


def setup(fn):
    def setDatas(*args):
        SETDATAS('%s.ini' % args[0].__class__.__name__)
        result = fn(*args)
        return result

    return setDatas
