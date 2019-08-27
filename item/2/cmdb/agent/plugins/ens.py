#encoding: utf-8

# ens子进程发送所有消息给Server

import logging
from threading import Thread
import time
from queue import Empty
import requests

import hmac
import urllib
import urllib.parse

logger = logging.getLogger(__name__)

class ENS(Thread):

    def __init__(self, config):
        super(ENS, self).__init__()
        self._config = config


    def run(self):
        _queue = getattr(self._config, 'QUEUE')

        _handle = self.handle
        while True:
            try:
                evt = _queue.get(block=True, timeout=3)
                logger.debug('ENS get event: %s', evt)
                _handle(evt)
            except Empty as e:
                time.sleep(3)


    def handle(self, evt): 
        key = '123456789'
        secret = 'abcdef'
        unix_time = int(time.time())

        sign = get_sign(evt.get('msg'), unix_time, key, secret)
        
        _url = 'http://{0}/api/v4/{1}'.format(getattr(self._config, 'SERVER'), evt.get('url'))
        _url += '?' + urllib.parse.urlencode({'time' : unix_time, 'key' : key, 'sign' : sign})

        response =  requests.post(_url, json=evt.get('msg'))
        
        if not response.ok:
            logger.error(response.text)
        else:
            logger.debug('handle evt[ %s ], result: %s', evt, response.text)


def get_sign(data, time, key, secret):
    sign_data = data.copy()
    sign_data['time'] = time

    # 排序，不然会乱
    sorted_sign_data = sorted(sign_data.items())
    text_sign_data =  secret + ':' + urllib.parse.urlencode(sorted_sign_data)
    
    _hmac = hmac.HMAC(key.encode())
    _hmac.update(text_sign_data.encode())

    return _hmac.hexdigest()