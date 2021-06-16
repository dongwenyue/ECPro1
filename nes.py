import requests
import oss2

def get_sts():
    '''获取STS'''
    url = f'http://api-qa.ecpro.com/storage-internal/sign'
    data = requests.post(url).json()['data']
    print(data)
    return data


def aliyun_url(key, sts_data):
    '''通过key获取图片的URL'''
    access_key_id = sts_data['access_key_id']
    access_key_secret = sts_data['access_key_secret']
    security_token = sts_data['security_token']
    bucket_name = sts_data['bucket_name']
    auth = oss2.StsAuth(access_key_id, access_key_secret, security_token)
    bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', bucket_name)
    url = bucket.sign_url(method='GET', expires=86400, key=key)
    return url


if __name__ == '__main__':
    sts_data = get_sts()
    key = 'assets/1000082/d0e582b5-0bcf-4ad3-8d9d-e9c6b5188391.png'
    print(aliyun_url(key, sts_data))