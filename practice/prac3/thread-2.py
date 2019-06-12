#encoding: utf-8

import threading
import logging
import time

logger = logging.getLogger(__name__)

class MyThread(threading.Thread):

    def __init__(self, name, *args, **kwargs): 
        super(MyThread, self).__init__(*args, **kwargs)
        self._name = name
        self.daemon = True
        
    def run(self):
        name = self._name
        for i in range(3):
            logger.info(' %s : %s ',name,i)
            time.sleep(0.1)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.info(' start')
    th1 = MyThread('th1')
    th2 = MyThread('th2')
    th3 = MyThread('th3')

    th1.start()
    th2.start()
    th3.start()

    # th1.join()
    # th2.join()
    # th3.join()

    logger.info(' end')