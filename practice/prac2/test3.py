#encoding: utf-8

import logging

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        filename='info.log',
        filemode='w',
        format='%(asctime)s - %(name)s - %(levelname)s:%(message)s',
        )
    logger.debug('debug')
    logger.exception('ex')
    logger.error('error')
