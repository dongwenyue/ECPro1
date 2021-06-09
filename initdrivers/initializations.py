from encapsulation import ECProServer
from utils.configures.paths import SYSCONFIG, TEST_DATA_DIR
from utils.httputils.isignetHttpUtils import HttpUtils

from utils.configures.confparser import InitConfigs

sysconfigs = InitConfigs(SYSCONFIG)

token = sysconfigs.get('server', 'token')

serverurl = sysconfigs.get('server', 'serverurl')

ECPro = ECProServer.ECProServer(HttpUtils(serverurl))
