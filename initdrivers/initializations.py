from encapsulation import ECProServer
from utils.configures.paths import SYSCONFIG, DATACONFIG
from utils.httputils.isignetHttpUtils import HttpUtils
from .inidriver import initdriver

initdriver(DATACONFIG)

from utils.configures.confparser import InitConfigs

sysconfigs = InitConfigs(SYSCONFIG)

ECPro = ECProServer.ECProServer(HttpUtils(sysconfigs.get('server', 'serverurl')))
