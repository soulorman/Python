#encoding: utf-8

from .base import BaseThread
from utils import sysutils

class Host(BaseThread):

    def __init__(self, queue):
        super(Host, self).__init__('host', 5, queue)

    def make_event(self):
        return {
            'type' : self._type,
            'msg' : {
                'name' : sysutils.get_name(),
                'mac' : sysutils.get_mac(),
                'os' : sysutils.get_os(),
                'arch' : sysutils.get_arch(),
                'mem' : sysutils.get_mem(),
                'cpu' : sysutils.get_cpu(),
                'disk' : sysutils.get_disk(),
            }
        }
