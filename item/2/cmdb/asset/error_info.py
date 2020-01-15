# 查询sql
# encoding: utf-8
from .models import Host, Host_All, Resource, Gpu, Deploy

error_dict = {
                'mem_error':'内存资源不足',
                'cpu_error':'cpu资源不足',
                'disk_error':'磁盘资源不足',
                'process_error': '进程已关闭',
                'process_error_mem': '进程内存超过90%',
                'process_error_cpu': '进程CPU超过90%',
            }

legend = [
    'auth',
    'path',
    'recovery',
    'thoslide',
    'config',
    'registry',
    'tensorflow_model_server',
    'save_log',
    'celery',
    'redis',
    'nginx',
    'mysql'
]


def get_error_info(address_ip, start_time):
    mem_error = Resource.objects.filter(ip=address_ip, mem_free__lte=2000, created_time__gte=start_time).values('mem_free','created_time').last()
    cpu_error = Resource.objects.filter(ip=address_ip, cpu_total_use__gte=85, created_time__gte=start_time).values('cpu_total_use','created_time').last()
    
    disk_error = Resource.objects.filter(ip=address_ip, created_time__gte=start_time).values('volume','created_time').last()
    process_error = Resource.objects.filter(ip=address_ip, created_time__gte=start_time).values('process_isalive','created_time').last()
    
    process_error_mem = Resource.objects.filter(ip=address_ip, created_time__gte=start_time).values('process_mem_use','created_time').last()
    process_error_cpu = Resource.objects.filter(ip=address_ip, created_time__gte=start_time).values('process_cpu_use','created_time').last()

    result = []
    if mem_error:
        result.append((error_dict['mem_error'],mem_error.get('mem_free',''),mem_error['created_time'].strftime('%Y-%m-%d_%H:%M:%S')))

    if cpu_error:
        result.append((error_dict['cpu_error'],cpu_error.get('cpu_total_use',''),cpu_error['created_time'].strftime('%Y-%m-%d_%H:%M:%S')))

    if process_error:
        for idx_process,v_process in enumerate(process_error.get('process_isalive',[]).replace(' ','').split(',')[:-1:]):
            if '0' == v_process:
                result.append((error_dict['process_error'],legend[idx_process],process_error['created_time'].strftime('%Y-%m-%d_%H:%M:%S')))
    
    if disk_error:
        for idx_disk,v_disk in enumerate(disk_error.get('volume',[]).replace(' ','').split(',')[:-1:]):
            if int(v_disk.split(':')[1][:-2:]) <= 100:
                result.append((error_dict['disk_error'],disk_error.get('volume',[]).replace(' ','').split(',')[:-1:][idx_disk],disk_error['created_time'].strftime('%Y-%m-%d_%H:%M:%S')))

    if process_error_cpu:
        for idx_process_cpu,v_process_cpu in enumerate(process_error_cpu.get('process_cpu_use',[]).replace(' ','').split(',')[:-1:]):
            if float(v_process_cpu) >= 90:
                result.append((error_dict['process_error_cpu'],legend[idx_process_cpu],process_error_cpu.get('process_cpu_use',[]).replace(' ','').split(',')[:-1:][idx_process_cpu],process_error_cpu['created_time'].strftime('%Y-%m-%d_%H:%M:%S')))

    if process_error_mem:
        for idx_process_mem,v_process_mem in enumerate(process_error_mem.get('process_mem_use',[]).replace(' ','').split(',')[:-1:]):
            if float(v_process_mem) >= 90:
                result.append((error_dict['process_error_mem'],legend[idx_process_mem],process_error_mem.get('process_mem_use',[]).replace(' ','').split(',')[:-1:][idx_process_mem],process_error_mem['created_time'].strftime('%Y-%m-%d_%H:%M:%S')))


    return  result