# encoding: utf-8
from queue import Queue


class Config(object):
    """设置配置"""
    def __init__(self, args):
        super(Config, self).__init__()
        self.SERVER = '{0}:{1}'.format(args.host, args.port)
        self.QUEUE = Queue()
        self.ITEMS = args.items

    # def set(self, args):
    #     self.SERVER = '{0}:{1}'.format(self.args.host, self.args.port)
    #     self.QUEUE = Queue()

