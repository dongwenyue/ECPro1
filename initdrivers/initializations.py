from encapsulation import ECProServer, ECProServer_parent, ECProServer_pdd,ECProServer_he
from utils.configures.paths import SYSCONFIG, TEST_DATA_DIR
from utils.httputils.isignetHttpUtils import HttpUtils

from utils.configures.confparser import InitConfigs

sysconfigs = InitConfigs(SYSCONFIG)

token = sysconfigs.get('server', 'token')

serverurl = sysconfigs.get('server', 'serverurl')

ECPro = ECProServer_he.ECProServer(HttpUtils(serverurl))

# ECPro = ECProServer_parent.ECProServer(HttpUtils(serverurl))
# ECPro = ECProServer_pdd.ECProServer(HttpUtils(serverurl))
