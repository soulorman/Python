#encoding: utf-8

from .base import BaseThread
from utils import sysutils

class Resource(BaseThread):

    def __init__(self, queue):
        super(Resource, self).__init__('resource', 5, queue)
    
    def make_event(self):
        return {
            'type' : self._type,
            'url' : 'client/{0}/resource/'.format(sysutils.get_addr()),
            'msg' : {
                'cpu' : sysutils.get_cpu_precent(),
                'mem' : sysutils.get_mem_precent(),
                }
        }