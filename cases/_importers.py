from initdrivers.global_importers import *

from utils.configures.paths import *

from utils.testutils.faker.generator import *

from utils.converter.encoding import *

from initdrivers.globals import *

from utils.converter.base64utils import *

import datetime,uuid


def setup(fn):
    def setDatas(*args):
        SETDATAS('%s.ini'%args[0].__class__.__name__)
        result = fn(*args)
        return result
    return setDatas