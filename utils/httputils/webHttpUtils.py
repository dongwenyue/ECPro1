import json
import requests
import ssl
import time
import urllib

from urllib3.filepost import encode_multipart_formdata

from ..stringIO.logger.testlogger import DEBUG, ERROR, INFO


def check_url(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return True
        else:
            return r.status_code
    except Exception as e:
        return e


class HttpUtils(object):
    header = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Connection': 'keep-alive',
    }

    ssl._create_default_https_context = ssl._create_unverified_context
    ssl_flag = False
    cookie = None
    httpClient = requests.session()

    def __init__(self, url):
        if 'https' in url: self.ssl_flag = True
        self.url = url

    def _set_cookie(self, token):
        self.cookie = requests.cookies.RequestsCookieJar()
        self.cookie.set('token', token)

    def _check_header(self, header):
        if 'token' in header.keys(): return True
        return False

    def post(self, url, body):
        try:
            DEBUG(('http://%s request body :\n%s' % (
            self.url + url, json.dumps(body, sort_keys=True, indent=4, separators=(',', ':')))).decode(
                'unicode-escape'))
        except:
            DEBUG('http://%s request body :%s' % (self.url + url, body))
        try:
            time_start = time.time()
            response = self.httpClient.post(self.url + url, headers=self.header, data=json.dumps(body),
                                            cookies=self.cookie)
            DEBUG('%s updates cookies :%s' % (self.url + url, json.dumps(self.httpClient.cookies.get_dict())))
            time_end = time.time()
            INFO('%s takes：%.3f seconds' % (self.url + url, (time_end - time_start)))
        except Exception as e:
            ERROR('%s rerurn:%s' % (self.url + url, e))
            BaseException('%s rerurn:%s' % (self.url + url, e))

        if response.status_code == 200:
            if self._check_header(response.headers): self._set_cookie(response.headers.get('token'))
            return response.content
        else:
            ERROR('[HTTP] %s return %d' % (self.url + url, response.status_code))
            raise BaseException('[HTTP] %s return:%s' % (self.url + url, response.status_code))

    def post_param(self, url, body):
        header = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
        body = urllib.parse.urlencode(body)
        DEBUG(('http://%s request body : %s' % (self.url + url, body)))
        try:
            time_start = time.time()
            response = self.httpClient.post(self.url + url, headers=header, data=body, cookies=self.cookie)
            DEBUG('%s updates cookies :%s' % (self.url + url, json.dumps(self.httpClient.cookies.get_dict())))
            time_end = time.time()
            INFO('%s takes：%.3f seconds' % (self.url + url, (time_end - time_start)))
        except Exception as e:
            ERROR('%s rerurn:%s' % (self.url + url, e))
            BaseException('%s rerurn:%s' % (self.url + url, e))

        if response.status_code == 200:
            if self._check_header(response.headers): self._set_cookie(response.headers.get('token'))
            return response.content
        else:
            ERROR('[HTTP] %s return %d' % (self.url + url, response.status_code))
            raise BaseException('[HTTP] %s return:%s' % (self.url + url, response.status_code))

    def post_multipart(self, url, files):

        data = (files, open(files, 'rb').read())
        encode_data = encode_multipart_formdata(data)
        data = encode_data[0]
        header = {
            'Content-Type': '',
            'Connection': 'keep-alive'
        }

        header['Content-Type'] = encode_data[1]
        r = requests.post(url, headers=header, data=data)
        return r.content

    def get(self, url, mod=None):
        if mod:
            mod = urllib.parse.urlencode(mod)
            url = '%s%s' % (url, '?', mod)
        '''
        example:
            textmod = {'user':'admin','password':'admin'}
            textmod = urllib.urlencode(textmod)
            textmod = password=admin&user=admin 
        '''
        time_start = None
        try:
            time_start = time.time()
            response = self.httpClient.get(self.url + url, cookies=self.cookie, headers=self.header)
            DEBUG('%s updates cookies :%s' % (self.url + url, json.dumps(self.httpClient.cookies.get_dict())))
            INFO('get packetage from %s takes：%.3f seconds' % (self.url + url, (time.time() - time_start)))
            return response.content
        except Exception as e:
            INFO('get packetage from %s takes：%.3f seconds' % (self.url + url, (time.time() - time_start)))
            ERROR('get packetages from %s error: %s' % (self.url + url, e))
            raise BaseException('get packetages from %s error: %s' % (self.url + url, str(e)))
