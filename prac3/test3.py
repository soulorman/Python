#encoding: utf-8

import logging

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.debug('debug')
    logger.exception('ex')
    logger.error('error')


