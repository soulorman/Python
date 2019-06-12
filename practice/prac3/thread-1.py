#enconding: utf-8

import threading
import logging
import time

logger = logging.getLogger(__name__)

def run(name):
    for i in range(3):
        logger.info(' %s : %s ',name,i)
        time.sleep(0.1)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.info(' start')
    th1 = threading.Thread(target=run, args=('th1',))
    th1.daemon = True
    th2 = threading.Thread(target=run, args=('th2',))
    th2.daemon = True
    th3 = threading.Thread(target=run, args=('th3',))
    th3.daemon = True
    
    th1.start()
    th2.start()
    th3.start()

    # th1.join()
    # th2.join()
    # th3.join()

    logger.info(' end')