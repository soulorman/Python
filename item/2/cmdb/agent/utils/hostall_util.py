#encoding: utf-8

import socket
import platform
import psutil
import uuid
import subprocess

def get_addr():
    return socket.gethostbyname(socket.gethostname())

def get_mac():
    mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

def get_cpu_name():

    return subprocess.getoutput("cat /proc/cpuinfo |grep 'model name'|uniq|awk '{for(i=4;i<=NF;i++) printf$i}'")

def get_server_producter():
    return subprocess.getoutput("dmidecode -s baseboard-manufacturer")

def get_server_name():
    return subprocess.getoutput("dmidecode -s system-version")

def get_serial():
    return subprocess.getoutput("dmidecode -s baseboard-serial-number")

def get_network():
    return socket.gethostname()

    def get_partitons():
    return socket.gethostname()