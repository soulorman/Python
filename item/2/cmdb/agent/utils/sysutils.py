#encoding: utf-8

import socket
import platform
import psutil
import subprocess

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


def get_mem_size():
    return str(psutil.virtual_memory().total // 1024 ** 3) + "GB"


def get_disk_info():
    disk_name = subprocess.getoutput("lsblk -d|awk 'NR!=1{print $1}'").split('\n')
    disk_size = subprocess.getoutput("lsblk -d|awk 'NR!=1{print $4}'").split('\n')

    return dict(zip(disk_name,disk_size))

def get_cpu_precent():
    return psutil.cpu_percent()


def get_mem_precent():
    return psutil.virtual_memory().percent


if __name__ == '__main__':
    print(get_addr())
    print(get_name())
    print(get_mac())
    print(get_arch())
    print(get_os())
    print(get_kernel())
    print(get_cpu_number())
    print(get_cpu_core())
    print(get_cpu_vcore())
    print(get_mem_size())
    print(get_disk_info())
    print(get_cpu_precent())
    print(get_mem_precent())