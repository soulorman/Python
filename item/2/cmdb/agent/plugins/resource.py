#encoding: utf-8

from .base import BaseThread
from utils import process_util

class Resource(BaseThread):

    def __init__(self, queue):
        super(Resource, self).__init__('resource', 10, queue)

    def make_event(self):
        return {
            'type' : self._type,
            'url' : 'client/{0}/resource/'.format(process_util.get_addr()),
            'msg' : {
                'process_isalive' : process_util.get_program()['isalive'],
                'process_cpu_use' : process_util.get_program()['cpu'],
                'process_mem_free' : process_util.get_program()['mem'],

                'mem_free' : process_util.get_mem_free(),
                'cpu_total_use' : process_util.get_cpu_use(),
                'disk_read' : process_util.get_disk_read(),
                'disk_write' : process_util.get_disk_write(),
                'network_upload' : process_util.get_network_upload(),
                'network_download' : process_util.get_network_download(),
                'volume' : process_util.get_volume(),
                }
        }