#encoding:utf-8

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
import datetime
from datetime import timedelta


class Host(models.Model):
    ip = models.GenericIPAddressField(null=False, default='0.0.0.0')
    name = models.CharField(max_length=32, null=False, default='')
    os = models.CharField(max_length=64, null=False, default='')
    kernel = models.CharField(max_length=64, null=False, default='')

    cpu_number = models.IntegerField(null=False, default=0)  
    cpu_core = models.IntegerField(null=False, default=0)
    cpu_vcore = models.IntegerField(null=False, default=0)
    arch = models.CharField(max_length=16, null=False, default='x86')

    mem_info = models.CharField(max_length=512,null=False, default='[]')
    disk_info = models.CharField(max_length=512, null=False, default='{}')
    gpu_info = models.CharField(max_length=512,null=False, default='')
    
    remark = models.TextField(null=False, default='')
    discover_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(null=False)


    @classmethod
    def create_or_replace(cls, ip, name, os, kernel, cpu_number, cpu_core, cpu_vcore, arch, mem_info, disk_info, gpu_info):
        obj = None
        try:
            obj = cls.objects.get(ip=ip)
        except ObjectDoesNotExist as e:
            obj = cls()
            obj.ip = ip
            obj.remark = '无'
            obj.discover_time = timezone.now()

        obj.name = name
        obj.os = os
        obj.kernel = kernel
        obj.cpu_number =cpu_number
        obj.cpu_core = cpu_core
        obj.cpu_vcore = cpu_vcore
        obj.arch = arch
        obj.mem_info = mem_info
        obj.disk_info = disk_info
        obj.gpu_info = gpu_info

        obj.update_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        obj.save()
        return obj

    @classmethod
    def delete(cls, id):
        return Host.objects.filter(pk=id).delete()


    @classmethod
    def update_remark(cls,ip,remark):

        return Host.objects.filter(ip=ip).update(remark=remark)


    def as_dict(self):
        rt = {}
        for k, v in self.__dict__.items():
            if isinstance(v, (int, float, bool, str,datetime.datetime)):
                rt[k] = v

        return rt


class Host_All(models.Model):
    ip = models.GenericIPAddressField(null=False, default='0.0.0.0')

    user = models.CharField(max_length=16, null=False, default='admin')
    mac = models.CharField(max_length=128, null=False, default='')
    cpu_name = models.CharField(max_length=512, null=False, default='')

    server_producter = models.CharField(max_length=64, null=False, default='made in china')
    server_name = models.CharField(max_length=64, null=False, default='')
    serial = models.CharField(max_length=64, null=False, default='')
    network = models.CharField(max_length=512, null=False, default='{}')
    partitions = models.CharField(max_length=1024, null=False, default='{}')

    update_time = models.DateTimeField(null=False)

    @classmethod
    def delete(cls, id):
        return Host_All.objects.filter(pk=id).delete()


    @classmethod
    def create_or_replace(cls, ip, mac, cpu_name, server_producter, server_name, serial, network, partitions):

        obj = None
        try:
            obj = cls.objects.get(ip=ip)
        except ObjectDoesNotExist as e:
            obj = cls()
            obj.ip = ip
            obj.user = 'admin'

        obj.mac = mac 
        obj.cpu_name = cpu_name
        obj.server_producter = server_producter
        obj.server_name =server_name
        obj.serial = serial
        obj.network = network
        obj.partitions = partitions
        
        obj.update_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        obj.save()
        return obj


    @classmethod
    def update_user(cls, ip, user):
        return Host_All.objects.filter(ip=ip).update(user=user)

    def as_dict(self):
        rt = {}
        for k, v in self.__dict__.items():
            if isinstance(v, (int, float, bool, str,datetime.datetime)):
                rt[k] = v

        return rt


class Resource(models.Model):
    ip = models.GenericIPAddressField(null=False, default='0.0.0.0')

    process_isalive = models.CharField(max_length=512, null=False, default='[]')
    process_cpu_use = models.CharField(max_length=512, null=False, default='[]')
    process_mem_use = models.CharField(max_length=512, null=False, default='[]')

    cpu_total_use = models.FloatField(null=False, default=0)
    mem_free = models.FloatField(null=False, default=0)
    disk_read = models.FloatField(null=False, default=0)
    disk_write = models.FloatField(null=False, default=0)

    network_upload = models.FloatField(null=False, default=0)
    network_download = models.FloatField(null=False, default=0)
    network_total_use = models.FloatField(null=False, default=0)

    created_time = models.DateTimeField(auto_now_add=True)


    @classmethod
    def create_or_replace(cls, ip, process_isalive, process_cpu_use, process_mem_use, cpu_total_use, mem_free, disk_read, disk_write, network_upload, network_download, network_total_use):
        resource = Resource()
        resource.ip = ip

        resource.process_isalive = process_isalive
        resource.process_cpu_use = process_cpu_use
        resource.process_mem_use = process_mem_use

        resource.cpu_total_use = cpu_total_use
        resource.mem_free = mem_free
        resource.disk_read = disk_read
        resource.disk_write = disk_write

        resource.network_upload = network_upload
        resource.network_download = network_download
        resource.network_total_use = network_total_use

        resource.created_time = timezone.now()
        resource.save()
        return resource


    def as_dict(self):
        rt = {}
        for k,v in self.__dict__.items():
            if isinstance(v, (int, float, bool, str, tuple, list,datetime.datetime)):
                rt[k] = v
        return rt

'''
class Gpu(models.Model):
    ip = models.GenericIPAddressField(null=False, default='0.0.0.0')

    gpu = models.CharField(max_length=1024, null=False, default='[]')

    created_time = models.DateTimeField(auto_now_add=True)


    @classmethod
    def create_or_replace(cls, ip, gpu):
        gpu = Gpu()
        gpu.ip = ip
        gpu.gpu = gpu

        gpu.save()
        return gpu
        '''