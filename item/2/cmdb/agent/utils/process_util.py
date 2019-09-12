#encoding: utf-8

import subprocess
import json
import psutil


def get_addr():
    return socket.gethostbyname(socket.gethostname())

def get_program():
    program = subprocess.getoutput("bash /home/ubuntu/program.sh")
    return json.loads(program)

def get_cpu_use():
    return psutil.cpu_percent(interval=1)
    #return subprocess.getoutput("top -b -n 1 |grep Cpu|awk '{printf \"%.2f\",100-$8}'")

def get_mem_free():
    # 单位M
    return psutil.virtual_memory().available // 1024 // 1024
    #return subprocess.getoutput("free -m|grep Mem|awk '{print $NF}'")
    
def get_disk_read():
    return psutil.disk_io_counters(perdisk=True)['sda'].read_bytes // 1024 //1024
    #return subprocess.getoutput("iostat |grep sda| awk '{print $3}'")

def get_disk_write():
    return psutil.disk_io_counters(perdisk=True)['sda'].write_bytes // 1024 // 1024
    #return subprocess.getoutput("iostat |grep sda| awk '{print $4}'")    

def get_容量():
    pass

def get_network():
    net = psutil.net_io_counters()
    bytes_sent = '{0:.2f} Mb'.format(net.bytes_recv // 1024 // 1024)
    bytes_rcvd = '{0:.2f} Mb'.format(net.bytes_sent // 1024 // 1024)
    result = u"网卡接收流量 %s 网卡发送流量 %s" % (bytes_rcvd, bytes_sent)
    
    return result


if __name__ == '__main__':
    #print(get_program())
    print(get_cpu_use())
    print(get_mem_free())
    print(get_disk_read())
    print(get_disk_write())
    print(get_network())
    #print(get_容量())

