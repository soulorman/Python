# encoding: utf-8

from .base import BaseThread
from utils import process_util

class Resource(BaseThread):

    def __init__(self, queue):
        super(Resource, self).__init__('resource', 5, queue)
    
    def make_event(self):
        return {
            'type' : self._type,
            'url' : 'client/{0}/resource/'.format(process_util.get_addr()),
            'msg' : {
                'process_isalive' : process_util.get_cpu_use(),
                'process_cpu_use' : process_util.get_mem_free(),
                'process_mem_use' : process_util.get_disk_read(),
                get_disk_write
                get_network

                }
        }