#encoding: utf-8

# 收集一类消息的子进程
# 收集主面板的数据
# 和ens通信靠queue

from .base import BaseThread
from utils import sysutils, hostall_util

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
                'kernel' : sysutils.get_kernel(),
                'arch' : sysutils.get_arch(),
                'cpu_number' : sysutils.get_cpu_number(),
                'cpu_core' : sysutils.get_cpu_core(),
                'cpu_vcore' : sysutils.get_cpu_vcore(),
                'mem_size' : sysutils.get_mem_size(),
                'disk_info' : sysutils.get_disk_info(),
                'mac' : hostall_util.get_mac(),
                'cpu_name' : hostall_util.get_cpu_name(),
                'server_producter' : hostall_util.get_server_producter(),
                'server_name' : hostall_util.get_server_name(),
                'serial' : hostall_util.get_serial(),
                'network' : hostall_util.get_network(),
                'partitons' : hostall_util.get_partitons(),
                }
        }
