#encoding: utf-8

# 收集一类消息的子进程
# 收集主面板的数据
# 和ens通信靠queue
from .base import BaseThread
from utils import main_sysutils, more_sysutils

class Host(BaseThread):
    """收集主机的硬件常用信息"""

    def __init__(self, queue):
        super(Host, self).__init__('host', 10, queue)
        self.items = queue.ITEMS
    
    def make_event(self):
        return {
            'type' : self._type,
            'url' : 'client/{0}/'.format(main_sysutils.get_addr()),
            'msg' : {
                'name' : main_sysutils.get_hostname(),
                'os' : main_sysutils.get_os(),
                'kernel' : main_sysutils.get_kernel(),
                'arch' : main_sysutils.get_arch(),
                'cpu_number' : main_sysutils.get_cpu_number(),
                'cpu_core' : main_sysutils.get_cpu_core(),
                'cpu_vcore' : main_sysutils.get_cpu_vcore(),
                'get_mem_info' : main_sysutils.get_mem_info(),
                'disk_info' : main_sysutils.get_disk_info(),
                'get_gpu_info' : main_sysutils.get_gpu_info(),

                'mac' : more_sysutils.get_mac_address(),
                'cpu_name' : more_sysutils.get_cpu_name(),
                'server_producter' : more_sysutils.get_server_producter(),
                'server_name' : more_sysutils.get_server_name(),
                'serial' : more_sysutils.get_serial(),
                'network' : more_sysutils.get_network(),
                'partitons' : more_sysutils.get_partitons(),
                'project' : self.items,
                }
        }
