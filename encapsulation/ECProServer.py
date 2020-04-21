# -*- coding: utf-8 -*-


class ECProServer(object):
    def __init__(self, httpUtil):
        global http
        http = httpUtil

    def _init_data(self):
        pass

    def updateRolesInfo(self, name, role_id):
        INFO('调用 修改角色信息 接口')
        from utils.globals import SECRET
        murl = '%s/%s' % (SECRET, role_id)
        reqBody = {}
        reqBody['name'] = name
        reqBody = json.dumps(reqBody)
        INFO(reqBody)
        res = http.patch(murl, json.dumps(reqBody))
        try:
            return json.loads(res)
        except:
            self.fail('updateRolesInfo return:%s' % res)

    def deleteRoles(self, role_id):
        INFO('调用 删除角色 接口')
        from utils.globals import SECRET
        murl = '%s/%s' % (SECRET, role_id)
        res = http.delete(murl)
        try:
            return json.loads(res)
        except:
            self.fail('updateRolesInfo return:%s' % res)
