import time
class Time(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        start_time = time.time()
        self._func()
        end_time = time.time()
        a = end_time - start_time
        print("花费了{}".format(a))

@Time
def sum():
    print('shijian')
    time.sleep(1.25)

sum()
