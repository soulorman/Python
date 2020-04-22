# encoding: utf-8
# 总启动脚本

import argparse
import logging
import os
from queue import Queue
import time

from gconf import Config
from plugins.ens import ENS
from plugins.host import Host
from plugins.monitor import Monitor

# 先定义日志获取路径
logger = logging.getLogger(__name__)

def main(config):
    """启动所有进程

    :param config:传入配置项，包括服务器名称、端口地址和队列
    :return
    """
    ths = []
    ths.append(ENS(config))
    ths.append(Host(config))
    ths.append(Monitor(config))

    for th in ths:
        th.start()


if __name__ == '__main__':
    """运行该进程"""
    
    # 自带帮助，也就是自带-h选项，自己写了会冲突
    parser = argparse.ArgumentParser(description='this is start collection process')
    parser.add_argument('-H', '--host', type=str, default='192.168.31.104', help='Server Addr')
    parser.add_argument('-P', '--port', type=int, default=8123, help='Server Port')
    parser.add_argument('-I', '--items', type=str, default='ESD', help='items name')
    parser.add_argument('-V', '--verbose', action='store_true', help='DEBUG INFO')
    parser.add_argument('-v', '--version', action='version', version='v1.0')

    args = parser.parse_args()
    level = logging.DEBUG if args.verbose else logging.INFO

    # 处理日志
    fmt = '%(asctime)s - %(name)s - %(levelname)s:%(message)s'
    base_dir = os.path.dirname(os.path.abspath(__file__))
    logging.basicConfig(
                        level = level, 
                        format = fmt,
                        filemode = 'w', 
                        filename = os.path.join(base_dir, 'logs', 'agentd.log')
                        )

    pid = os.getpid()
    logger.info('agent started: [%s]', pid)

    # 初始化配置
    config = Config(args)
    main(config)