#enconding: utf-8

import argparse
import os
import logging

logger = logging.getLogger(__name__)

if __name__  == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', type=str, default='127.0.0.1', help='Server Addr')
    parser.add_argument('-P', '--port', type=int, default=8888, help='Server Port')
    parser.add_argument('-V', '--verbose', action='store_true', help='DEBUG INFO')

    args = parser.parse_args()

    level = logging.DEBUG if args.verbose else logging.INFO
    fmt = '%(asctime)s - %(name)s - %(levelname)s : %(message)s'
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pid = os.getpid()

    logging.basicConfig(
                        level=level,
                        format=fmt,
                        filemode='w',
                        filename=os.path.join(base_dir, 'logs', 'agentd.log')
                    )

    logger.info('started: [%s]', pid)
    logger.debug('debug msg')
