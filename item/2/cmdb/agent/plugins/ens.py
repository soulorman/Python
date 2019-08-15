#encoding: utf-8

# ens子进程发送所有消息给Server

import logging
from threading import Thread
import time
from queue import Empty
import requests

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
        _url = 'http://{0}/api/v1/{1}'.format(getattr(self._config, 'SERVER'), evt.get('url'))
        response =  requests.post(_url, json=evt.get('msg'))
        if not response.ok:
            logger.error(response.text)
        else:
            logger.debug('handle evt[ %s ], result: %s', evt, response.text)