import logging
import os

logger = logging.getLogger('fuqing')

fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
logging.basicConfig(format=fmt,filemode = 'w',filename='logger.log', level=logging.DEBUG)
pid = os.getpid()
logger.info(pid)
