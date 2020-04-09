#enconding: utf-8

from djongo import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
import datetime

class Host(models.Model):
    ip = models.GenericIPAddressField(null=False, default='0.0.0.0')
    name = models.CharField(max_length=128, null=False, default='')
    mac = models.CharField(max_length=32, null=False, default='')
    os = models.CharField(max_length=64, null=False, default='')

    kernel = models.CharField(max_length=128, null=False, default='')
    cpu_core = models.IntegerField(null=False, default=0)
    cpu_thread = models.IntegerField(null=False, default=0)

    arch = models.CharField(max_length=16, null=False, default='')
    mem = models.FloatField(null=False, default=0.0)
    cpu = models.IntegerField(null=False, default=0)
    disk = models.CharField(max_length=512, default='{}')

    user = models.CharField(max_length=128, null=False, default='root')
    remark = models.TextField(null=False, default='')
    purchase_time = models.DateTimeField(null=False)
    # over_insurance_time = models.DateTimeField(null=False)
    created_time = models.DateTimeField(auto_now_add=True)
    last_time = models.DateTimeField(null=False)


    @classmethod
    def create_or_replace(cls, ip, name, mac, os, kernel, cpu_core, cpu_thread, arch, mem, cpu, disk):
        obj = None
        try:
            obj = cls.objects.get(ip=ip)
        except ObjectDoesNotExist as e:
            obj = cls()
            obj.ip = ip
            obj.created_time = timezone.now()
            obj.purchase_time = timezone.now()
            obj.user = 'admin'
            obj.remark = '办公室'

        obj.name = name
        obj.mac = mac
        obj.os = os

        obj.kernel = kernel
        obj.cpu_core = cpu_core
        obj.cpu_thread = cpu_thread

        obj.arch = arch
        obj.mem = mem
        obj.cpu = cpu
        obj.disk = disk

        obj.last_time = timezone.now()
        obj.save()
        return obj


    def as_dict(self):
        rt = {}
        for k,v in self.__dict__.items():
            if isinstance(v, (int, float, bool, str, tuple, datetime.datetime)):
                rt[k] = v
        return rt


class Host_All(models.Model):
    ip = models.GenericIPAddressField(null=False, default='0.0.0.0')
    cpu_type = models.CharField(max_length=128, null=False, default='')
    mem_scalable = models.IntegerField(null=False, default=0)
    mem_slot = models.IntegerField(null=False, default=0)
    server_type = models.CharField(max_length=128, null=False, default='')
    server_producter = models.CharField(max_length=128, null=False, default='')
    server_number = models.CharField(max_length=128, null=False, default='')
    gpu_info = models.CharField(max_length=128, null=False, default='')
    network = models.CharField(max_length=512, null=False, default='{}')
    root = models.CharField(max_length=512, null=False, default='{}')
    data = models.CharField(max_length=512, null=False, default='{}')

    @classmethod
    def create_or_replace(cls, ip, cpu_type, mem_scalable, mem_slot, server_type, server_producter, server_number, gpu_info, network, root, data):
        host_all = None
        try:
            host_all = cls.objects.get(ip=ip)
        except ObjectDoesNotExist as e:
            host_all = Host_All()
            host_all.ip = ip

        host_all.cpu_type =  cpu_type
        host_all.mem_scalable = mem_scalable
        host_all.mem_slot = mem_slot
        host_all.server_type = server_type
        host_all.server_producter = server_producter
        host_all.server_number = server_number
        host_all.gpu_info = gpu_info
        host_all.network = network
        host_all.root = root
        host_all.data = data

        host_all.save()
        return host_all


    def as_dict(self):
        rt = {}
        for k,v in self.__dict__.items():
            if isinstance(v, (int, float, bool, str, tuple, datetime.datetime)):
                rt[k] = v
        return rt


class Monitor(models.Model):
    ip = models.GenericIPAddressField(null=False, default='0.0.0.0')

    isalive = models.CharField(max_length=512, null=False, default='{}')
    cpu = models.CharField(max_length=512, null=False, default='{}')
    mem = models.CharField(max_length=512, null=False, default='{}')

    cpu_use = models.FloatField(null=False, default=0)
    mem_free = models.FloatField(null=False, default=0)
    disk_read = models.FloatField(null=False, default=0)
    disk_write = models.FloatField(null=False, default=0)
    upload_success = models.IntegerField(null=False, default=0)
    yuce_success = models.IntegerField(null=False, default=0)
    network = models.CharField(max_length=128, null=False, default='')

    created_time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create_or_replace(cls,ip,isalive,cpu,mem,cpu_use,mem_free,disk_read,disk_write,upload_success,yuce_success,network):
        monitor = None
        try:
            monitor = cls.objects.get(ip=ip)
        except ObjectDoesNotExist as e:
            monitor = Monitor()
            monitor.ip = ip

        monitor.isalive = isalive
        monitor.cpu = cpu
        monitor.mem = mem

        monitor.cpu_use = cpu_use
        monitor.mem_free = mem_free
        monitor.disk_read = disk_read
        monitor.disk_write = disk_write
        monitor.upload_success = upload_success
        monitor.yuce_success = yuce_success
        monitor.network = network
        monitor.created_time = timezone.now()

        monitor.save()
        return monitor

    def as_dict(self):
        rt = {}
        for k,v in self.__dict__.items():
            if isinstance(v, (int, float, bool, str, tuple, datetime.datetime)):
                rt[k] = v
        return rt


class Resource(models.Model):
    ip = models.GenericIPAddressField(null=False, default='0.0.0.0')

    gpu = models.CharField(max_length=512, null=False, default='[]')

    created_time = models.DateTimeField(auto_now_add=True)


    @classmethod
    def create_or_replace(cls, ip, **result):
        resource = None
        try:
            resource = cls.objects.get(ip=ip)
        except ObjectDoesNotExist as e:
            resource = Resource()
            resource.ip = ip

        resource.gpu = result

        resource.save()
        return resource