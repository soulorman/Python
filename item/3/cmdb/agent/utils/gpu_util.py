# encoding: utf-8
# 没有使用
from nvml import Nvml
import socket

def get_addr():
    return socket.gethostbyname(socket.gethostname())


def get_gpu_uid():
    text = Nvml.user_info()
    for gpu in text:
        try:
            for i in gpu:
                print(i['uid'])
                print(i['pid'])
                print(i['mem'])
        except BaseException as e:
            pass


#def get_gpu_process():
#    text = Nvml.user_info()
#    for gpu in text:
#        print(gpu)


#def get_gpu_mem():
#    text = Nvml.user_info()
##    for gpu in text:
#        print(gpu)

get_gpu_uid()