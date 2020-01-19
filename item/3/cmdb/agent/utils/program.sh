#!/bin/bash

isalive=()
cpu=()
mem=()
count=0
for p in auth-service path-service insights-service thoslide-service config-mongo registry tensorflow_model_server save_log celery redis nginx: mysqld
do
    program=`ps -aux|grep -w $p|grep -v grep|wc -l`
    cpu_use=`ps -axo pcpu,command|grep  "$p"|grep -v grep|awk '{sum += $1} END {print sum}'`
    mem_use=`ps -axo pmem,command|grep  "$p"|grep -v grep|awk '{sum += $1} END {print sum}'`

    isalive[$count]="${program},"
    if [[ $program -eq 0 ]]
    then
        cpu[$count]="0,"
        mem[$count]="0,"
    else
        cpu[$count]="${cpu_use},"
        mem[$count]="${mem_use},"
    fi
    let count+=1
done

echo -e "{\"isalive\":\"${isalive[@]}\",\"cpu\":\"${cpu[@]}\",\"mem\":\"${mem[@]}\"}"