#encoding: utf-8

from .base import BaseThread

class Host(BaseThread):

    def __init__(self, queue):
        super(Host, self).__init__('host', 5, queue)

    def make_event(self):
        return {
            'type' : self._type,
            'msg' : {
                'ip' : '1.1.1.1',
                'name' : 'nameaaaa',
                'mac' : '',
                'os' : '',
                'kernel' : '',
                'cpu_core' : 0,
                'cpu_thread' : 0,
                'arch' : '',
                'mem' : 0,
                'cpu' : 0,
                'disk' : '{}',
            }
        }
