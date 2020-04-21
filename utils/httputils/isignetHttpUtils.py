import requests
import ssl
import time
import urllib
import urllib3

from ..stringIO.logger.testlogger import *

requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning)  # @UndefinedVariable


class HttpUtils(object):
    header = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Connection': 'keep-alive',
    }

    ssl._create_default_https_context = ssl._create_unverified_context
    ssl_flag = False

    httpClient = requests

    proxies = {'http': '', 'https': ''}

    def __init__(self, url, proxy=None):

        if 'https' in url: self.ssl_flag = True
        self.url = url

        if proxy:
            self.proxies['http'] = 'http://%s' % proxy
            self.proxies['https'] = 'https://%s' % proxy
        else:
            self.proxies = None

    def request(self, url, body):
        DEBUG('[HTTP] %s request body :%s' % (self.url + url, json.dumps(json.loads(body), ensure_ascii=False)))
        try:
            time_start = time.time()
            print(self.url + url)
            response = requests.post(self.url + url, headers=self.header, data=body.encode(), proxies=self.proxies,
                                     verify=False)
            DEBUG('[HTTP] %s takes: %.3f seconds' % (self.url + url, (time.time() - time_start)))
        except Exception as e:
            ERROR('[HTTP] %s rerurn:%s' % (self.url + url, e))
            raise BaseException('[HTTP] %s rerurn:%s' % (self.url + url, e))

        if response.status_code == 200:
            return response.content
        else:
            ERROR('[HTTP] %s return %d' % (self.url + url, response.status_code))
            raise BaseException('[HTTP] %s return:%s' % (self.url + url, response.status_code))

    def post_multipart(self, url, files, datas):
        content = open('%s' % (files), 'rb').read()
        fields = {'file': (files[files.rfind('\\') + 1:], content)}
        if datas:
            merge = dict(fields)
            merge.update(datas)
            encode_data = urllib3.encode_multipart_formdata(merge)
        else:
            encode_data = urllib3.encode_multipart_formdata(fields)

        header = {
            'Content-Type': 'multipart/form-data',
            'Content-Length': str(len(content)),
            'Connection': 'keep-alive'
        }
        header['Content-Type'] = encode_data[1]

        r = requests.post(self.url + url, headers=header, data=encode_data[0], proxies=self.proxies, verify=False)

        if r.status_code == 200:
            return r.content
        else:
            ERROR('[HTTP] %s return %d' % (self.url + url, r.status_code))
            raise BaseException('[HTTP] %s return:%s' % (self.url + url, r.status_code))

    def get(self, url, mod=None):
        if mod:
            mod = urllib.parse.urlencode(mod)
            url = '%s%s' % (url, mod)
        '''
        example:
            textmod = {'user':'admin','password':'admin'}
            textmod = urllib.urlencode(textmod)
            textmod = password=admin&user=admin 
        '''
        time_start = None
        try:
            time_start = time.time()
            response = self.httpClient.get(self.url + url, headers=self.header, proxies=self.proxies)
            INFO('get packetage from %s takes：%.3f seconds' % (self.url + url, (time.time() - time_start)), False)
            return response.content
        except Exception as e:
            INFO('get packetage from %s takes：%.3f seconds' % (self.url + url, (time.time() - time_start)))
            ERROR('get packetages from %s error: %s' % (self.url + url, e))
            raise BaseException('get packetages from %s error: %s' % (self.url + url, str(e)))

    def getByUrl(self, url, mod=None):
        if mod:
            mod = urllib.parse.urlencode(mod)
            url = '%s%s' % (url, mod)
        '''
        example:
            textmod = {'user':'admin','password':'admin'}
            textmod = urllib.urlencode(textmod)
            textmod = password=admin&user=admin 
        '''
        time_start = None
        try:
            time_start = time.time()
            response = self.httpClient.get(url, headers=self.header, proxies=self.proxies)
            INFO('get packetage from %s takes：%.3f seconds' % (url, (time.time() - time_start)), False)
            return response.content
        except Exception as e:
            INFO('get packetage from %s takes：%.3f seconds' % (url, (time.time() - time_start)))
            ERROR('get packetages from %s error: %s' % (url, e))
            raise BaseException('get packetages from %s error: %s' % (url, str(e)))

    def delete(self, url, body=None):
        if body:
            DEBUG('[HTTP] %s delete body :%s' % (self.url + url, json.dumps(json.loads(body), ensure_ascii=False)))
            try:
                time_start = time.time()
                response = requests.delete(self.url + url, headers=self.header, data=body.encode(),
                                           proxies=self.proxies,
                                           verify=False)
                DEBUG('[HTTP] %s takes: %.3f seconds' % (self.url + url, (time.time() - time_start)))
            except Exception as e:
                ERROR('[HTTP] %s rerurn:%s' % (self.url + url, e))
                raise BaseException('[HTTP] %s rerurn:%s' % (self.url + url, e))
        else:
            try:
                time_start = time.time()
                response = requests.delete(self.url + url, headers=self.header, proxies=self.proxies,
                                           verify=False)
                DEBUG('[HTTP] %s takes: %.3f seconds' % (self.url + url, (time.time() - time_start)))
            except Exception as e:
                ERROR('[HTTP] %s rerurn:%s' % (self.url + url, e))
                raise BaseException('[HTTP] %s rerurn:%s' % (self.url + url, e))

        if response.status_code == 200:
            return response.content
        else:
            ERROR('[HTTP] %s return %d' % (self.url + url, response.status_code))
            raise BaseException('[HTTP] %s return:%s' % (self.url + url, response.status_code))

    def patch(self, url, data, username=None, password=None):
        DEBUG('[HTTP] %s patch body :%s' % (self.url + url, json.dumps(json.loads(data), ensure_ascii=False)))
        if username:
            auth = {'username': username, 'password': password}
        try:
            time_start = time.time()
            response = requests.patch(self.url + url, headers=self.header, data=data, proxies=self.proxies,
                                      verify=False)
            DEBUG('[HTTP] %s takes: %.3f seconds' % (self.url + url, (time.time() - time_start)))
        except Exception as e:
            ERROR('[HTTP] %s rerurn:%s' % (self.url + url, e))
            raise BaseException('[HTTP] %s rerurn:%s' % (self.url + url, e))

        if response.status_code == 200:
            return response.content
        else:
            ERROR('[HTTP] %s return %d' % (self.url + url, response.status_code))
            raise BaseException('[HTTP] %s return:%s' % (self.url + url, response.status_code))
