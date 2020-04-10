#encoding: utf-8

import subprocess
import json
import psutil
import socket

def get_addr():
    return socket.gethostbyname(socket.gethostname())


# 在服务器上需要这个脚本
def get_program():
    program = subprocess.getoutput("bash utils/program.sh")
    return json.loads(program)


def get_cpu_use():
    return psutil.cpu_percent(interval=1)
    #return subprocess.getoutput("top -b -n 1 |grep Cpu|awk '{printf \"%.2f\",100-$8}'")


def get_mem_free():
    # 单位M
    return psutil.virtual_memory().available // 1024 // 1024
    #return subprocess.getoutput("free -m|grep Mem|awk '{print $NF}'")


def get_disk_read():
    #return psutil.disk_io_counters(perdisk=True)['sda'].read_bytes // 1024 //1024
    return subprocess.getoutput("iostat |grep ^sda| awk '{print $3}'")


def get_disk_write():
    #return psutil.disk_io_counters(perdisk=True)['sda'].write_bytes // 1024 // 1024
    return subprocess.getoutput("iostat |grep ^sda| awk '{print $4}'")    


def get_volume():
    return subprocess.getoutput("df -Th|grep data|awk '{print $NF\":\"$5}'").split("\n")

# 注意网卡的情况
def get_network_upload():
    bytes_rcvd = subprocess.getoutput("sar -n DEV 1 1|egrep 'enp'|grep 'Ave*'|awk '{print $5}'")
#   net = psutil.net_io_counters()
#   bytes_sent = '{0:.2f} Mb'.format(net.bytes_recv // 1024 // 1024)
#   bytes_rcvd = '{0:.2f} Mb'.format(net.bytes_sent // 1024 // 1024)
    return bytes_rcvd


def get_network_download():
    bytes_sent = subprocess.getoutput("sar -n DEV 1 1|egrep 'enp'|grep 'Ave*'|awk '{print $6}'")    
    return bytes_sent


if __name__ == '__main__':
    print(get_addr())
    print(get_program())
    print(get_cpu_use())
    print(get_mem_free())
    print(get_disk_read())
    print(get_disk_write())
    print(get_network_download())
    print(get_network_upload())
    print(get_volume())
