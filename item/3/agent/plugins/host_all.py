#encoding: utf-8


#不需要
from .base import BaseThread
from utils import hostall_util

class Host_All(BaseThread):

    def __init__(self, queue):
        super(Host_All, self).__init__('hostall', 10, queue)
    
    def make_event(self):
        return {
            'type' : self._type,
            'url' : 'client/{0}/'.format(hostall_util.get_addr()),
            'msg' : {
                'mac' : hostall_util.get_mac(),
                'cpu_name' : hostall_util.get_cpu_name(),
                'server_producter' : hostall_util.get_server_producter(),
                'server_name' : hostall_util.get_server_name(),
                'serial' : hostall_util.get_serial(),
                'network' : hostall_util.get_network(),
                'partitons' : hostall_util.get_partitons()
                }
        }

