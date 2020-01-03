#encoding: utf-8

import socket
import platform
import psutil
import subprocess

import collections

def get_addr():
    return socket.gethostbyname(socket.gethostname())

def get_name():
    return socket.gethostname()

def get_arch():
    return platform.architecture()[0]


def get_os():
    return platform.linux_distribution()[0]+" "+platform.linux_distribution()[1]


def get_kernel():
    return platform.release()


def get_cpu_number():
    return subprocess.getoutput("cat /proc/cpuinfo | grep 'physical id' | sort | uniq | wc -l")


def get_cpu_core():
    return subprocess.getoutput("cat /proc/cpuinfo | grep 'core id' | sort | uniq | wc -l")


def get_cpu_vcore():
    return subprocess.getoutput("cat /proc/cpuinfo | grep 'processor' | sort | uniq | wc -l")


def get_disk_info():
    # 上传服务器有可能字典乱序，但是改成其他类型，上传的时候符号不对  总是[]
    disk_name = subprocess.getoutput("lsblk -d|awk 'NR!=1{print $1}'").split('\n')
    disk_size = subprocess.getoutput("lsblk -d|awk 'NR!=1{print $4}'").split('\n')

    return dict(zip(disk_name,disk_size))

def get_mem_info():
    return subprocess.getoutput("dmidecode -t memory|grep 'Size'|awk '{print $2$3$4}'").split('\n')

def get_gpu_info():
    return subprocess.getoutput("nvidia-smi -q|grep 'Product Name'|awk '{print $4\" \"$5\" \"$6}'").split('\n')

if __name__ == '__main__':
    print(get_addr())
    print(get_name())
    print(get_arch())
    print(get_os())
    print(get_kernel())
    print(get_cpu_number())
    print(get_cpu_core())
    print(get_cpu_vcore())
    print(get_disk_info())
    print(get_mem_info())
    print(get_gpu_info())