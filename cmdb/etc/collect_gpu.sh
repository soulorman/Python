#!/bin/bash

nvidia-smi &> /dev/null
if [ $? -eq 0 ]
then
table=()
count=0

for i in `seq 0 8`
do
    PID=`nvidia-smi -q -i $i|grep "Process ID"|awk '{print $NF}'|head -1`
    if [ ! -z $PID ]
    then
        USERS=`/bin/ps aux|grep -v grep|grep $PID|awk '{print $1}'|head -1`
        if [ "$USERS" == "sunzhuo" ]
        then
           USER="孙卓"
        elif [ "$USERS" == "calvinku" ]
        then
           USER="健白"
        elif [ "$USERS" == "root" ]
        then
           USER="灿灿"
        elif [ "$USERS" == "xugang" ]
        then
           USER="徐罡"
       fi
    else
        USER="没人"
    fi
    use=`nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits -i $i`
    table[$count]="{\"$USER\":\"$use%\"},"
    let count++

done
echo "{\"gpu_user\" : [${table[@]}] }"    
else
    echo "{\"gpu_user\" : [] }"    
fi
