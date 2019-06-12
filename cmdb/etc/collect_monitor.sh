#/bin/bash
#....

Isalive=()
Cpu=()
Mem=()

count=0
for p in auth-service path-service insights-service thoslide-service config-mongo registry tensorflow_model_server save_log celery redis nginx: mysqld
do
    program=`ps -uax|grep $p|grep -v grep|wc -l`
    cpu=`ps -axo pcpu,command|grep "$p"|grep -v grep|awk '{sum += $1} END {print sum}'`
    mem=`ps -axo pmem,command|grep "$p"|grep -v grep|awk '{sum += $1} END {print sum}'`

    if [ -z $cpu ] && [ -z $mem ]
    then
       Isalive[$count]=$program,
       Cpu[$count]=0,
       Mem[$count]=0,
    else
       Isalive[$count]=$program,
       Cpu[$count]=$cpu,
       Mem[$count]=$mem,
    fi
    let count++
done


#包括cpu的wait字段
cpu_use=`top -b -n 1 |grep Cpu|awk '{printf "%.2f",100-$8}'`


# 剩余内存容量
mem_free=`free -m|grep Mem|awk '{print $NF}'`


disk_read=`iostat |grep sda| awk '{print $3}'`
disk_write=`iostat |grep sda| awk '{print $4}'`


#调节sql语句
time=`date +%Y-%m-%d`

total_success=`cat /opt/info/upload_total  &> /dev/null|awk '{if($2==$time)print $1}'`
yuce_success=`cat /opt/info/predict_success  &> /dev/null|awk  '{if($2==$time)print $1}'`
if [ -z $total_success ] && [ -z $yuce_success ]  
then
   yuce_success=0
   total_success=0
fi


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
