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

    process_isalive = models.CharField(max_length=128, null=False, default='[]')
    process_cpu_use = models.CharField(max_length=128, null=False, default='[]')
    process_mem_use = models.CharField(max_length=128, null=False, default='[]')

    cpu_total_use = models.FloatField(null=False, default=0)
    mem_free = models.FloatField(null=False, default=0)
    disk_read = models.FloatField(null=False, default=0)
    disk_write = models.FloatField(null=False, default=0)

    network_upload = models.FloatField(null=False, default=0)
    network_download = models.FloatField(null=False, default=0)
    volume = models.CharField(max_length=1024, null=False, default='[]')

    created_time = models.DateTimeField(auto_now_add=True)


    @classmethod
    def create_or_replace(cls, ip, process_isalive, process_cpu_use, process_mem_use, cpu_total_use, mem_free, disk_read, disk_write, network_upload, network_download, volume):
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
        resource.volume = volume

        resource.created_time = timezone.now()
        resource.save()
        return resource


    def as_dict(self):
        rt = {}
        for k,v in self.__dict__.items():
            if isinstance(v, (int, float, bool, str, tuple, list,datetime.datetime)):
                rt[k] = v
        return rt


class Gpu(models.Model):
    ip = models.GenericIPAddressField(null=False, default='0.0.0.0')

    gpu_user_name = models.CharField(max_length=1024, null=False, default='[]')

    update_time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create_or_replace(cls, ip, gpu_user_name):
        gpu = Gpu()
        gpu.ip = ip
        gpu.gpu_user_name = gpu_user_name

        gpu.update_time = timezone.now()
        gpu.save()
        return gpu


    def as_dict(self):
        rt = {}
        for k, v in self.__dict__.items():
            if isinstance(v, (int, float, bool, str,datetime.datetime)):
                rt[k] = v

        return rt


class Deploy(models.Model):
    hospital_address = models.CharField(max_length=128, null=False, default='无')
    project_name = models.CharField(max_length=64, null=False, default='无')
    deploy_version = models.CharField(max_length=64, null=False, default='无')
    update_time = models.CharField(max_length=64, null=False, default='无时间')
    remark = models.TextField(null=False, default='无')

    @classmethod
    def create_or_replace(cls, hospital_address, project_name, deploy_version, remark='无'):
        deploy = None
        try:
            deploy = cls.objects.get(hospital_address=hospital_address)
        except ObjectDoesNotExist as e:
            deploy = Deploy()
            deploy.hospital_address = hospital_address
            
        deploy.project_name = project_name
        deploy.deploy_version = deploy_version
        deploy.remark = remark

        deploy.update_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        deploy.save()
        return deploy

    @classmethod
    def delete(cls, id):
        return Deploy.objects.filter(pk=id).delete()

    @classmethod
    def update_remark(cls, hospital_address, project_name, deploy_version, update_time, remark):
        return Deploy.objects.filter(hospital_address=hospital_address).update(project_name=project_name, deploy_version=deploy_version, update_time=update_time, remark=remark)

    def as_dict(self):
        rt = {}
        for k, v in self.__dict__.items():
            if isinstance(v, (int, float, bool, str,datetime.datetime)):
                rt[k] = v

        return rt


class Wealth(models.Model):
    ip = models.GenericIPAddressField(null=False, default='0.0.0.0')
    name = models.CharField(max_length=32, null=False, default='')
    host_address = models.CharField(max_length=32, null=False, default='无')
    service_role = models.CharField(max_length=256, null=False, default='')
    
    update_time = models.DateTimeField(auto_now_add=True)
    remark = models.TextField(null=False, default='无')

    @classmethod
    def create_or_replace(cls, ip, name, host_address, service_role):
        wealth = None
        try:
            wealth = cls.objects.get(ip=ip)
        except ObjectDoesNotExist as e:
            wealth = Wealth()
            wealth.ip = ip
            
        wealth.name = name
        wealth.host_address = host_address
        wealth.service_role = service_role
        wealth.remark = '无'

        wealth.update_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        wealth.save()
        return wealth

    def as_dict(self):
        rt = {}
        for k, v in self.__dict__.items():
            if isinstance(v, (int, float, bool, str,datetime.datetime)):
                rt[k] = v

        return rt


class Interview(models.Model):
    question_type_number = models.CharField(max_length=128, null=False, default='无')
    question_answer = models.TextField(null=False, default='无')
    scores = models.IntegerField(null=False, default=0) 
    
    update_time = models.DateTimeField(null=False)

class Interview_SA(models.Model):
    question_type = models.CharField(max_length=64, null=False, default='无')
    question_number = models.IntegerField(null=False, default=0)
    title = models.TextField(null=False, default='无')
    question_answer = models.TextField(null=False, default='无')
    scores = models.IntegerField(null=False, default=0)
    
    update_time = models.DateTimeField(null=False)

    def as_dict(self):
        rt = {}
        for k, v in self.__dict__.items():
            if isinstance(v, (int, float, bool, str,datetime.datetime)):
                rt[k] = v

        return rt

#题型           题号  题目                                                            参考答案       分数   创建时间
#SA_question    1    '写出把/opt/目录下小于100K的文件全部转移到/tmp下的shell命令'     'mv /opt /tmp'     5    2020-2-27
