#!/bin/bash

file_name="json.txt"
select=$1

# 所有有用的东西
all_info=`tail -400 $file_name|awk '/Raw/,/successfully/{print}'|egrep -v "^=|^-|^cancer|^rotate|^tiss|^divi|^v_mi|^adjus|^slide|^h_mi|^cutmark|^[0-9]|^$|^Pro|INFO|^JSON"`

# shijian是时间 b是接收json，job_id是发送的json(以及处理的编号), slide_paths是切片编号  所有需要的消息 原始数据
info_first=`tail -400 $file_name|awk '/Raw/,/successfully/{print}'|egrep -v "^=|^-|^cancer|^rotate|^tiss|^divi|^v_mi|^adjus|^slide|^h_mi|^cutmark|^[0-9]|^$|^Pro|INFO|^JSON"|egrep "^Raw|^b|job"|sed 'N;N;N;s/\n/;/g'`

# 多少个记录
info_first_line=`tail -400 $file_name|awk '/Raw/,/successfully/{print}'|egrep -v "^=|^-|^cancer|^rotate|^tiss|^divi|^v_mi|^adjus|^slide|^h_mi|^cutmark|^[0-9]|^$|^Pro|INFO|^JSON"|egrep "^Raw|^b|job"|sed 'N;N;N;s/\n/;/g'|wc -l`

# 单独的错误和时间
error_log=`tail -400 $file_name|awk '/Raw/,/successfully/{print}'|egrep -v "^=|^-|^cancer|^rotate|^tiss|^divi|^v_mi|^adjus|^slide|^h_mi|^cutmark|^[0-9]|^$|^Pro|INFO|^JSON"|egrep -v "^b|job"`

for((i=1;i<=$info_first_line;i++))
do
    time=`tail -400 $file_name|awk '/Raw/,/successfully/{print}'|egrep -v "^=|^-|^cancer|^rotate|^tiss|^divi|^v_mi|^adjus|^slide|^h_mi|^cutmark|^[0-9]|^$|^Pro|INFO|^JSON"|egrep "^Raw|^b|job"|sed 'N;N;N;s/\n/;/g'|tail -n $i|head -1|awk -F";" '{print $1}'|awk -F[\(\)] '{print $2}'|awk '{print $3" "$4}'`
    job_id=`tail -400 $file_name|awk '/Raw/,/successfully/{print}'|egrep -v "^=|^-|^cancer|^rotate|^tiss|^divi|^v_mi|^adjus|^slide|^h_mi|^cutmark|^[0-9]|^$|^Pro|INFO|^JSON"|egrep "^Raw|^b|job"|sed 'N;N;N;s/\n/;/g'|tail -n $i|head -1|awk -F";" '{print $3}'|awk -F: '{print $2}'`
    echo -e "job_id:$job_id($time)\n接收的json为:"
    tail -400 $file_name|awk '/Raw/,/successfully/{print}'|egrep -v "^=|^-|^cancer|^rotate|^tiss|^divi|^v_mi|^adjus|^slide|^h_mi|^cutmark|^[0-9]|^$|^Pro|INFO|^JSON"|egrep "^Raw|^b|job"|sed 'N;N;N;s/\n/;/g'|tail -n $i|head -1|awk -F";" '{print $2}'|grep "b'"|sed "s/b'\|'/ /g"|jq -c
    send_json=`tail -400 $file_name|awk '/Raw/,/successfully/{print}'|egrep -v "^=|^-|^cancer|^rotate|^tiss|^divi|^v_mi|^adjus|^slide|^h_mi|^cutmark|^[0-9]|^$|^Pro|INFO|^JSON"|egrep "^Raw|^b|job"|sed 'N;N;N;s/\n/;/g'|tail -n $i|head -1|awk -F";" '{print $4}'` 2> /dev/null
    if [ -z "$send_json" ]
    then
        echo "无任何发送json信息,错误信息如下："
        tail -400 $file_name|awk '/Raw/,/successfully/{print}'|egrep -v "^=|^-|^cancer|^rotate|^tiss|^divi|^v_mi|^adjus|^slide|^h_mi|^cutmark|^[0-9]|^$|^Pro|INFO|^JSON"|egrep -v "^b|job"|grep -A 15 "$time"
    else
        echo -e "发送的json为:"
        echo $send_json|jq -c
        echo "错误信息如下："
        tail -400 $file_name|awk '/Raw/,/successfully/{print}'|egrep -v "^=|^-|^cancer|^rotate|^tiss|^divi|^v_mi|^adjus|^slide|^h_mi|^cutmark|^[0-9]|^$|^Pro|INFO|^JSON"|egrep -v "^b|job"|grep -A 15 "$time"
    fi
    echo -e "****************************************************"
done

