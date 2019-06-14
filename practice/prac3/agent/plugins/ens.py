#encondig: utf-8

import logging
from threading import Thread
import time
from queue import Empty

logger = logging.getLogger(__name__)


class ENS(Thread):
    def __init__(self, config):
        super(ENS, self).__init__()
        self._config = config

    def run(self):
        _queue = getattr(self._config, 'QUEUE')

        while True:
            try:
                evt = _queue.get(block=True, timeout=3)
                logger.debug('ENS get event: %s', evt)
            except Empty as e:
                time.sleep(3)