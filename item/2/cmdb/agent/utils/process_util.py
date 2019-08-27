#encoding: utf-8

import subprocess
import json

def get_addr():
    return socket.gethostbyname(socket.gethostname())

def get_program():
    program = subprocess.getoutput("bash /home/ubuntu/program.sh")
    return json.loads(program)





if __name__ == '__main__':
    print(get_program())


'''

#包括cpu的wait字段
cpu_use=`top -b -n 1 |grep Cpu|awk '{printf "%.2f",100-$8}'`


# 剩余内存容量
mem_free=`free -m|grep Mem|awk '{print $NF}'`

disk_read=`iostat |grep sda| awk '{print $3}'`
disk_write=`iostat |grep sda| awk '{print $4}'`

#调节sql语句
time=`date +%Y-%m-%d`

table=()
num=0
Net_File1=/tmp/.net1
Net_File2=/tmp/.net2
for interface in  `ifconfig |grep enp |awk '{print $1}'`
do
    cat /proc/net/dev |grep $interface | awk '{print $1"\t"$2"\t"$10}'  > $Net_File1
    sleep 1
    cat /proc/net/dev |grep $interface | awk '{print $1"\t"$2"\t"$10}'  > $Net_File2
    A=`cat $Net_File1 |awk '{print $2}'`
    B=`cat $Net_File2 |awk '{print $2}'`
    C=`cat $Net_File1 |awk '{print $3}'`
    D=`cat $Net_File2 |awk '{print $3}'`
    upload=`echo "($B-$A)/2/1024/1024" |bc`
    download=`echo "($D-$C)/2/1024/1024" |bc`

    table[$num]="{\"name\":\"$interface\",\"upload\":\"${upload}Mb/s\",\"download\":\"${download}Mb/s\"},"
    let num++
done

echo -e "{\"isalive\":\"${Isalive[@]}\",\"cpu\":\"${Cpu[@]}\",\"mem\":\"${Mem[@]}\",\"cpu_use\":$cpu_use,\"mem_free\":$mem_free,\"disk_read\":$disk_read,\"sda_write\":$disk_write,\"total_success\":$total_success,\"yuce_success\":$yuce_success,\"network_info\":[${table[@]}]}"




{"isalive":"2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 0, 1,",

"cpu":"1.6, 1.7, 2.9, 0.2, 0.2, 1.1, 0, 0, 0, 0.1, 0, 3.1,","mem":"2.1, 2.2, 2.4, 2, 1.8, 2.1, 0, 0, 0, 0, 0, 0.7,",
"cpu_use":7.90,
"mem_free":24486,

"disk_read":27.35,
"sda_write":366.23,

"network_info":[{"name":"enp4s0","upload":"0Mb/s","download":"0Mb/s"},]}

'''