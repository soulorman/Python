# encoding: utf-8
import hmac
import time
import requests
import urllib
import urllib.parse

def get_sign(data, time, key, secret):
    sign_data = data.copy()
    sign_data['time'] = time

    # 排序，不然会乱
    sorted_sign_data = sorted(sign_data.items())
    text_sign_data =  secret + ':' + urllib.parse.urlencode(sorted_sign_data)
    
    _hmac = hmac.HMAC(key.encode())
    _hmac.update(text_sign_data.encode())

    return _hmac.hexdigest()


if __name__ == '__main__':
    key = '123456789'
    secret = 'abcdef'
    unix_time = int(time.time())
    data = {
        'name' : 'kk',
    }

    url = 'http://localhost:8123/api/v3/client/192.168.31.106/'

    sign = get_sign(data, unix_time, key, secret)
    url += '?' + urllib.parse.urlencode({'time' : unix_time, 'key' : key, 'sign' : sign})
    for _ in range(1000):
        response = requests.post(url, json=data)
        print(response.json())
