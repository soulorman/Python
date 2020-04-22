#encoding: utf-8

import logging
from threading import Thread
import time

logger = logging.getLogger(__name__)

class BaseThread(Thread):
    """各工作线程的基础线程，父类"""

    def __init__(self, type, interval, config):
        super(BaseThread, self).__init__()
        self.daemon = True
        self._type = type
        self._interval = interval
        self._config = config

    def make_event(self):
        return None

    def run(self):
        """运行收集日志，并写进队列"""
        
        _type = self._type
        _interval = self._interval
        _config = self._config

        #_queue = getattr(_config, 'QUEUE')
        _queue = _config.QUEUE
        logger.info('plugin[ %s ] running ...', _type)

        while True:
            evt = self.make_event()
            if evt:
                logger.debug('plugin[ %s ] make event: %s', _type, evt)
                _queue.put(evt)

            time.sleep(_interval)