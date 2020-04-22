#encoding: utf-8

import socket
import uuid
import subprocess

def get_addr():
    return socket.gethostbyname(socket.gethostname())

def get_mac_address():
    mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

def get_cpu_name():
    return subprocess.getoutput("cat /proc/cpuinfo |grep 'model name'|uniq|awk '{for(i=4;i<=NF;i++) printf$i}'")

def get_server_producter():
    return subprocess.getoutput("dmidecode -s baseboard-manufacturer|head -1")

def get_server_name():
    return subprocess.getoutput("dmidecode -s system-version|head -1")

def get_serial():
    return subprocess.getoutput("dmidecode -s baseboard-serial-number|head -1")

def get_partitons():
    # 上传服务器有可能字典乱序，但是改成其他类型，上传的时候符号不对  总是[]
    partitons_name = subprocess.getoutput("df -Th |grep ^/dev|awk '{print $1}'").split('\n')
    partitons_info = subprocess.getoutput("df -Th |grep ^/dev|awk '{print $2\",\"$3\",\"$NF}'").split('\n')
    return dict(zip(partitons_name,partitons_info))

def get_network():
    # 上传服务器有可能字典乱序，但是改成其他类型，上传的时候符号不对  总是[]
    network_name = subprocess.getoutput("ip add|awk '{print $2}'|egrep 'en|do'|cut -d: -f 1").split('\n')
    network_address = subprocess.getoutput("ip add|grep inet|grep -v inet6|awk '{print $2}'|grep -v '127.0.0.1'").split('\n')
    return dict(zip(network_name,network_address))

if __name__ == '__main__':
    print(get_addr())
    print(get_mac_address())
    print(get_cpu_name())
    print(get_server_producter())
    print(get_server_name())
    print(get_serial())
    print(get_network())
    print(get_partitons())