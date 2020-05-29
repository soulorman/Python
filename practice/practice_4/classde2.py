from functools import wraps

def get_permissions():
    return {'root'}

class Require:
    def __init__(self,permissions):
        self.permissions = permissions

    def __call__(self, fn):
        @wraps(fn)
        def wrap(*args, **kwargs):
            if len(set(self.permissions).intersection(get_permissions())) <= 0:
                raise Exception('Permissions denied')
            return fn(*args, **kwargs)
        return wrap

@Require({'root'})
def reboot():
    print('正在关机')

reboot()
