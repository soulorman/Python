#encoding: utf-8

from .base import BaseThread
from utils import monitor_sysutils

class Monitor(BaseThread):

    def __init__(self, queue):
        super(Monitor, self).__init__('monitor', 10, queue)

    def make_event(self):
        return {
            'type' : self._type,
            'url' : 'client/{0}/monitor/'.format(monitor_sysutils.get_addr()),
            'msg' : {
                'process_isalive' : monitor_sysutils.get_program()['isalive'],
                'process_cpu_use' : monitor_sysutils.get_program()['cpu'],
                'process_mem_free' : monitor_sysutils.get_program()['mem'],

                'mem_free' : monitor_sysutils.get_mem_free(),
                'cpu_total_use' : monitor_sysutils.get_cpu_use(),
                'disk_read' : monitor_sysutils.get_disk_read(),
                'disk_write' : monitor_sysutils.get_disk_write(),
                'network_upload' : monitor_sysutils.get_network_upload(),
                'network_download' : monitor_sysutils.get_network_download(),
                'volume' : monitor_sysutils.get_volume(),
                }
        }