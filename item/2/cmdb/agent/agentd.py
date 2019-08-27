# encoding: utf-8

import argparse
import logging
import os 
from queue import Queue
import time

from gconf import Config
from plugins.ens import ENS
from plugins.host import Host
from plugins.resource import Resource

logger = logging.getLogger(__name__)

def main(config):
    ths = []
    ths.append(ENS(config))
   # ths.append(Host(config))
    ths.append(Resource(config))

    for th in ths:
        th.start()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', type=str, default='127.0.0.1', help='Server Addr')
    parser.add_argument('-P', '--port', type=int, default=8123, help='Server Port')
    parser.add_argument('-V', '--verbose', action='store_true', help='DEBUG INFO')

    args = parser.parse_args()
    level = logging.DEBUG if args.verbose else logging.INFO

    # 处理日志
    fmt = '%(asctime)s - %(name)s - %(levelname)s:%(message)s'
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    pid = os.getpid()

    logging.basicConfig(
                        level = level, 
                        format = fmt,
                        filemode = 'w', 
                        filename = os.path.join(base_dir, 'logs', 'agentd.log')
                        )

    logger.info('agent started: [%s]', pid)


    # 初始化配置
    config = Config()

    setattr(config, 'SERVER', '{0}:{1}'.format(args.host, args.port))
    setattr(config, 'QUEUE', Queue())

    main(config)
