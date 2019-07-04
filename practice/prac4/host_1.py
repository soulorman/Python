#!/usr/bin/python3
#Name:total.py
#Author:amd5.cn
#Datetime: 2018-06-28 
#for windows or Linux
#主机资源监控
import psutil
#cpu
def cpu_t(n):
    print('当前连续%d秒CPU使用率:'%(n),end='')
    for i in range(n):
        cpu=str(psutil.cpu_percent(1))+'%'
        print(cpu,end=' ')
    print('\n')
#内存统计
def memory_t():
    mem = psutil.virtual_memory()
    mem_free = mem.free/(1024.0*1024.0) #空闲内存
    mem_total = mem.total/(1024*1024)   #总内存
    print('总内存：%.1fM'%(mem_total))
    print('空闲：%.1fM'%(mem_free))
    print('使用率：%.1f%%'%(mem.percent))
    print('')
#硬盘统计
def disk_t():
    devs = psutil.disk_partitions()
    print('%2s %3s %3s %5s'%('分区','容量','空闲','使用率'))
    for dev in devs:
        try:
            disk_part = (dev.device)    #分区
            part = psutil.disk_usage(disk_part)
            part_total = part.total/(1024.0*1024.0*1024.0) #总容量
            part_free = part.free/(1024.0*1024.0*1024.0)   #空闲容量
            print('%3s %4dG %4dG  %6.1f%%'%(disk_part,part_total,part_free,part.percent))
        except PermissionError:
            print('',end='')
    print('\n')
#网络流量统计
def net_t():
    net_all = psutil.net_io_counters()
    net_sent = net_all.bytes_sent/(1024*1024)
    net_recv = net_all.bytes_recv/(1024*1024)
    print('发送流量：%.1fMb,接收流量：%.1fMb'%(net_sent,net_recv))
cpu_t(3)
memory_t()
disk_t()
net_t()
