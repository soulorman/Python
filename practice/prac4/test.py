#enconding: utf-8

import hmac
#import requests
import time
import urllib
import urllib.parse

def get_sign(data, time, key, secret):
    sign_data = data.copy()
    sign_data['time'] = time

    sorted_sign_data = sorted(sign_data.items())
    text_sign_data = urllib.parse.urlencode(sorted_sign_data)
    _hmac = hmac.HMAC(key.encode())
    _hmac.update(text_sign_data.encode())
    return _hmac.hexdigest()

if __name__ == '__main__':
    key = '123456789'
    secret = 'abcdef'
    
    ctime = int(time.time())
    data = {
        'name' : 'kk',
    
    }
    url = 'http://localhost:8889/api/v1/client/1.1.1.1/'
    sign = get_sign(data, ctime, key, secret)
    url += '?' + urllib.parse.urlencode({'time' : ctime, 'key' : key, 'sign' : sign})

    print(url)
    print(data)
    #requests.post( , json=data)