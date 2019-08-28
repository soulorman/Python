#encoding: utf-8

import subprocess

def get_gpu_user():
    return subprocess.getoutput("for i in `seq 0 8`;do bash /etc/zabbix/zabbix_agentd.d/gpu_user_1.sh $i;done").split('\n')

def get_gpu_use():
    return subprocess.getoutput("for i in `seq 0 8`;do bash /etc/zabbix/zabbix_agentd.d/gpu_use.sh $i;done").split('\n')

#def get_gpu_program():
#    return subprocess.getoutput("cat /proc/cpuinfo | grep 'processor' | sort | uniq | wc -l")

if __name__ == '__main__':
    print(get_gpu_user())
    print(get_gpu_use())
