# encoding: utf-8

from .base import BaseThread
from utils import gpu_sysutils

class Gpu(BaseThread):
    def __init__(self, queue):
        super(Gpu, self).__init__('gpu', 10, queue)

    def make_event(self):
        return {
            'type' : self._type,
            'url' : 'client/{0}/gpu/'.format(gpu_sysutils.get_addr()),
            'msg' : {
                      'gpu_user' : gpu_sysutils.get_gpu_user(),
                    }
        }