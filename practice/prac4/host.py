
import psutil
import time
import datetime
 
"""
获取系统基本信息
"""
 
EXPAND = 1024 * 1024
 
def mems():
    ''' 获取系统内存使用情况 '''
    mem = psutil.virtual_memory()
    mem_str = " 内存状态如下:\n"
    mem_str += "   系统的内存容量为: " + str(mem.total / EXPAND) + " MB\n"
    mem_str += "   系统的内存已使用容量为: " + str(mem.used / EXPAND) + " MB\n"
    mem_str += "   系统可用的内存容量为: " + str(mem.total / EXPAND - mem.used / (1024 * 1024)) + " MB\n"
    # mem_str += "   内存的buffer容量为: " + str(mem.buffers / EXPAND) + " MB\n"
    # mem_str += "   内存的cache容量为:" + str(mem.cached / EXPAND) + " MB\n"
    return mem_str
 
 
def cpus():
    ''' 获取cpu的相关信息 '''
    cpu_str = " CPU状态如下:\n"
    cpu_status = psutil.cpu_times()
    cpu_str += "   user = " + str(cpu_status.user) + "\n"
    # cpu_str += "   nice = " + str(cpu_status.nice) + "\n"
    cpu_str += "   system = " + str(cpu_status.system) + "\n"
    cpu_str += "   idle = " + str(cpu_status.idle) + "\n"
    # cpu_str += "   iowait = " + str(cpu_status.iowait) + "\n"
    # cpu_str += "   irq = " + str(cpu_status.irq) + "\n"
    # cpu_str += "   softirq = " + str(cpu_status.softirq) + "\n"
    # cpu_str += "   steal = " + str(cpu_status.steal) + "\n"
    # cpu_str += "   guest = " + str(cpu_status.guest) + "\n"
    return cpu_str
 
 
def disks():
    ''' 查看硬盘基本信息 '''
    ''' psutil.disk_partitions()    获取磁盘的完整信息
        psutil.disk_usage('/')      获得分区的使用情况,这边以根分区为例
        psutil.disk_io_counters()   获取磁盘总的io个数
        perdisk 默认为False
        psutil.disk_io_counters(perdisk=True)   perdisk为True 返回单个分区的io个数
    '''
    disk_str = " 硬盘信息如下:\n"
    disk_status = psutil.disk_partitions()
    for item in disk_status:
        disk_str += str(item) + "\n"
        p = item.device
        disk = psutil.disk_usage(p)
        disk_str += p+"盘容量为: " + str(disk.total / EXPAND) + " MB\n"
        disk_str += p+"盘已使用容量为: " + str(disk.used / EXPAND) + " MB\n"
        disk_str += p+"盘可用的内存容量为: " + str(disk.free / EXPAND) + " MB\n"
    return disk_str
 
 
def users():
    ''' 查看当前登录的用户信息 '''
    user_str = " 登录用户信息如下:\n "
    user_status = psutil.users()
    for item in user_status:
        user_str += str(item) + "\n"
    return user_str
 
def process():
    ''' 查看进程信息 '''
    pids = psutil.pids()
    proces = []
    for pid in pids:
        p = psutil.Process(pid)
        jctime = str(datetime.datetime.fromtimestamp(p.create_time()))[:19]
        p_info = [
            p.name(),       # 进程的名字
            #p.exe(),        # 进程bin文件位置
            #p.cwd(),        # 进程的工作目录的绝对路径
            p.status(),     # 进程的状态
            jctime,         # 进程的创建时间
            #p.uids(),       # 进程的uid信息
            #p.gids(),       # 进程的gid信息
            p.cpu_times(),  # cup时间信息
            p.memory_info(),# 进程内存的利用率
            p.io_counters() # 进程的io读写信息
        ]
        proces.append(p_info)
    return proces
 
if __name__ == '__main__':
    print(mems())   # 内存
    print(cpus())   # CPU
    print(disks())  # 硬盘
    print(users())  # 登录用户
    proces = process()
    print(proces[0])
