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
    arch = models.CharField(max_length=16, null=False, default='X86')

    mem_size = models.CharField(max_length=32,null=False, default='')
    disk_info = models.CharField(max_length=512, null=False, default='{}')
    
    remark = models.TextField(null=False, default='')
    discover_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(null=False)


    @classmethod
    def create_or_replace(cls, ip, name, os, kernel, cpu_number, cpu_core, cpu_vcore, arch, mem_size, disk_info):
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
        obj.mem_size = mem_size
        obj.disk_info = disk_info

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

    user = models.CharField(max_length=128, null=False, default='admin')
    mac = models.CharField(max_length=128, null=False, default='')
    cpu_name = models.CharField(max_length=1024, null=False, default='')
   # mem_scalable = models.IntegerField(null=False, default=0)
   # mem_slot = models.IntegerField(null=False, default=0)

    server_producter = models.CharField(max_length=64, null=False, default='made in china')
    server_name = models.CharField(max_length=2048, null=False, default='')
    serial = models.CharField(max_length=128, null=False, default='')
    #gpu_info = models.CharField(max_length=128, null=False, default='')
    network = models.CharField(max_length=512, null=False, default='{}')
    partitons = models.CharField(max_length=512, null=False, default='{}')

    update_time = models.DateTimeField(null=False)


    @classmethod
    def create_or_replace(cls, ip, mac, cpu_name, server_producter, server_name, serial, network, partitons):

        obj = None
        try:
            obj = cls.objects.get(ip=ip)
        except ObjectDoesNotExist as e:
            obj = cls()
            obj.ip = ip
            obj.user = 'admin'

        obj.mac = mac 
        obj.cpu_name = cpu_name
       # obj.mem_scalable = mem_scalable
       # obj.mem_slot = mem_slot
        obj.server_producter = server_producter
        obj.server_name =server_name
        obj.serial = serial
       # obj.gpu_info = gpu_info
        obj.network = network
        obj.partitons = partitons
        
        obj.update_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        obj.save()
        return obj


    @classmethod
    def update_user(cls, ip, user):
        return Host_All.objects.filter(ip=ip).update(user=user)


class Resource(models.Model):
    ip = models.GenericIPAddressField(null=False, default='0.0.0.0')
    cpu = models.FloatField(null=False, default=0)
    mem = models.FloatField(null=False, default=0)  

    created_time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create_obj(cls, ip, cpu, mem):
        resoruce = Resource()
        resoruce.ip = ip
        resoruce.cpu = cpu
        resoruce.mem = mem
        resoruce.save()
        return resoruce

    @classmethod
    def get_resource_data(cls, ip):
        start_time = timezone.now() - timedelta(hours=5)
        end_time = timezone.now()
        resources = Resource.objects.filter(ip=ip, created_time__gte=start_time).order_by('created_time')

        tmp_resources = {}
        for resource in resources:
            tmp_resources[resource.created_time.strftime('%Y-%m-%d %H:%M')] = {'cpu' : resource.cpu,'mem' : resource.mem}

        xAxis = []
        CPU_datas = []
        MEM_datas = []
        while start_time <= end_time:
            key = start_time.strftime('%Y-%m-%d %H:%M')
            resource = tmp_resources.get(key, {})

            xAxis.append(key)
            CPU_datas.append(resource.get('cpu', 0))
            MEM_datas.append(resource.get('mem', 0))
            start_time += timedelta(minutes=5)

 #       xAxis = []
 #       CPU_datas = []
 #       MEM_datas = []

 #       for resource in resources:
  #          xAxis.append(resource.created_time.strftime('%m-%d %H:%M'))
   #         CPU_datas.append(resource.cpu)
   #         MEM_datas.append(resource.mem)

        return xAxis, CPU_datas, MEM_datas