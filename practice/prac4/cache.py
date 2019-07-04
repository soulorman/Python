# coding:utf8
import time
import json

"""
简单的内存缓存参数
"""


def simple_cache(timeout=3):
    def decorator(f):
        def ff(*args, **kwargs):
            arg = json.dumps([args, kwargs])
            res = None
            key = f.__module__ + f.__name__ + arg
            if hasattr(f, key):
                res = getattr(f, key)
                if time.time() - res['last_time'] > timeout:
                    res = None
            if res is None:
                res = {'last_time': time.time(), 'data': f(*args, **kwargs)}
                setattr(f, key, res)
            return res['data']

        return ff

    return decorator

if __name__ == '__main__':
    @simple_cache(timeout=3)
    def haha(user_id):
        print("haha", user_id)


    @simple_cache(timeout=3)
    def baga(user_id):
        print("baga", user_id)


    haha(0)
    baga(0)
    haha(0)
    haha(1)
    time.sleep(5)
    haha(1)
