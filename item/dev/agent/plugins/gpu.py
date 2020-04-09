# encoding: utf-8

from .base import BaseThread
from utils import sysutils
from nvml import Nvml


class Gpu(BaseThread):
    def __init__(self, queue):
        super(Gpu, self).__init__('gpu', 10, queue)    

    def make_event(self):
        return {
            'type' : self._type,
            'url' : 'client/{0}/gpu/'.format(sysutils.get_addr()),
            'msg' : {
                'gpu_use_process' : Nvml.user_info()['pid'],
                'gpu_user_uid' : Nvml.user_info()['uid'],
                'gpu_use_mem' : Nvml.user_info()['mem'],
                }
        }
