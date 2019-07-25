#!/bin/bash
#the script is collected info of mem

#Memory scalable size(GB)
Mem_scalable=`sudo dmidecode -t memory|grep 'Maximum Capacity'|awk '{sum += $3} END {print sum}'` &> /dev/null
#Memory slot
Mem_slot_Number=`sudo dmidecode -t memory|grep 'Number Of Devices'|awk '{sum += $NF} END {print sum}'` &> /dev/null

#Motherboard type
Server_Type=`sudo dmidecode |grep 'Product Name'|tail -1|awk '{print $3" "$4}'` &> /dev/null
#Manufacturer
Server_Producter=`sudo dmidecode | grep -A 1 "Base Board"|tail -1|awk '{$1="";print}'` &> /dev/null
#serial number
Server_Number=`sudo dmidecode | grep -A 4 "Base Board"|tail -1|awk '{print $3}'` &> /dev/null

#cpu info
Cpu_Type=`sudo dmidecode -t processor|grep 'Version'|tail -1 |awk '{$1="";print}'` &> /dev/null

# root size(MB)
Root_Size=`sudo df -h|grep -w /|awk '{print $2}'` &> /dev/null
# Data_Size=`df -m|grep data|awk '{if(NR != "'"$Data_Number"'")print "\"" $NF "\"" ":" $2 ",";else print "\"" $NF "\"" ":" $2}'`
Data_Size=`sudo df -h|grep data|awk '{printf  $NF ":" $2 ","}'` &> /dev/null

table=()
count=0
# network interface name 
Network_Name=`ifconfig |grep enp |awk '{print $1}'`
for interface in $Network_Name
do
    # network mac address
    Network_Mac=`ifconfig  $interface|grep HWaddr |awk '{print $5}'`
    # networkip address
    Network_Ip=`ifconfig $interface|grep -oP '(?<=addr:)[\d\.]+'`
    table[$count]="{\"Network_Name\" : \"$interface\" , \"Network_Mac\" : \"$Network_Mac\", \"Network_Ip\" : \"$Network_Ip\"}," 
    let count++
done
table[$count-1]="{\"Network_Name\" : \"$interface\" , \"Network_Mac\" : \"$Network_Mac\", \"Network_Ip\" : \"$Network_Ip\"}" 


sudo nvidia-smi &> /dev/null
if [ $? -eq 0 ]
then
    List=()
    num=0
    # gpu name
    Gpu_Name=`sudo nvidia-smi -q|grep "Product Name"|awk '{print $5$6$7}'`
    for interface in $Gpu_Name
    do
        # gpu total memory(MB)
        Gpu_Total_Mem=`sudo nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits -i $num`
        List[$num]="{\"GPU_Name\" : \"$interface\" , \"Gpu_Total_Mem\" : \"$Gpu_Total_Mem\"},"
        let num++
    done
    List[$num-1]="{\"GPU_Name\" : \"$interface\" , \"Gpu_Total_Mem\" : \"$Gpu_Total_Mem\"}"
    echo -e "{\"Mem_scalable\":$Mem_scalable,\"Mem_slot_Number\":$Mem_slot_Number,\"Server_Type\":\"$Server_Type\",\"Server_Producter\":\"$Server_Producter\",\"Server_Number\":\"$Server_Number\",\"Network_Info\":[${table[@]}],\"Cpu_Type\":\"$Cpu_Type\",\"Gpu_info\":[${List[@]}],\"Root_Size\":\"$Root_Size\",\"Data_Size\":'[$Data_Size]'}"
else
    echo -e "{\"Mem_scalable\":$Mem_scalable,\"Mem_slot_Number\":$Mem_slot_Number,\"Server_Type\":\"$Server_Type\",\"Server_Producter\":\"$Server_Producter\",\"Server_Number\":\"$Server_Number\",\"Network_Info\":[${table[@]}],\"Cpu_Type\":\"$Cpu_Type\",\"Gpu_info\":[\"无GPU\"],\"Root_Size\":\"$Root_Size\",\"Data_Size\":'[$Data_Size]'}"
fi

