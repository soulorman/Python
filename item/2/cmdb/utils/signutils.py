# encoding: utf-8

import hmac
import time
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