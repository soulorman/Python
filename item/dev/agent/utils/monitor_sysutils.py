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
    if 'isalive' in program:
        return json.loads(program)
    else:
        msg = {"isalive":"0","cpu":"0","mem":"0"}
        return msg

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
    """得到现在的data盘存储信息"""
    data_numbers = subprocess.getoutput("df -Th|egrep -w 'data[0-9]|mfs'|awk '{print $NF}'").split("\n")
    volume_dict = {}
    for data_num in data_numbers:
        data_used = psutil.disk_usage(data_num).percent
        volume_dict[data_num] = data_used

    return volume_dict


# 注意网卡的情况
def get_network_upload():
    bytes_rcvd = subprocess.getoutput("sar -n DEV 1 1|egrep 'enp3s0f0'|grep 'Ave*'|awk '{print $5}'")
#   net = psutil.net_io_counters()
#   bytes_sent = '{0:.2f} Mb'.format(net.bytes_recv // 1024 // 1024)
#   bytes_rcvd = '{0:.2f} Mb'.format(net.bytes_sent // 1024 // 1024)
    if bytes_rcvd:
        return bytes_rcvd
    else:
        return 0


def get_network_download():
    bytes_sent = subprocess.getoutput("sar -n DEV 1 1|egrep 'enp3s0f0'|grep 'Ave*'|awk '{print $6}'")    
    if bytes_sent:
        return bytes_sent
    else:
        return 0


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
