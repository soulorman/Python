#encoding: utf-8

from .base import BaseThread
from utils import sysutils

class Host(BaseThread):

    def __init__(self, queue):
        super(Host, self).__init__('host', 5, queue)
    
    def make_event(self):
        return {
            'type' : self._type,
            'url' : 'client/{0}/'.format(sysutils.get_addr()),
            'msg' : {
                'name' : sysutils.get_name(),
                'os' : sysutils.get_os(),
                'cpu_number' : sysutils.get_cpu(),
                'arch' : sysutils.get_arch(),
                'mem_size' : sysutils.get_mem(),
                'disk_info' : sysutils.get_disk()
                }
        }