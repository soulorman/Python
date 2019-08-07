#encoding:utf-8

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

class Host(models.Model):
    ip = models.GenericIPAddressField(null=False, default='0.0.0.0')
    name = models.CharField(max_length=128, null=False, default='')
    mac = models.CharField(max_length=32, null=False, default='')
    os = models.CharField(max_length=64, null=False, default='')
    kernel = models.CharField(max_length=128, null=False, default='')

    cpu = models.IntegerField(null=False, default=0)  
    cpu_core = models.IntegerField(null=False, default=0)
    cpu_thread = models.IntegerField(null=False, default=0)
    arch = models.CharField(max_length=16, null=False, default='')

    mem = models.BigIntegerField(null=False, default=0)
    disk = models.CharField(max_length=512, null=False, default='{}')
    
    user = models.CharField(max_length=32, null=False, default='')
    remark = models.TextField(null=False, default='')
    purchase_time = models.DateTimeField(null=False)
    created_time = models.DateTimeField(null=False, auto_now_add=True)
    last_time = models.DateTimeField(null=False)

    @classmethod
    def create_or_replace(cls, ip, name, mac, os, kernel, cpu, cpu_core, cpu_thread, arch, mem, disk):
        obj = None
        try:
            obj = cls.objects.get(ip=ip)
        except ObjectDoesNotExist as e:
            obj = cls()
            obj.ip = ip
            obj.user = 'admin'
            obj.remark = '无备注，可以修改'
            obj.purchase_time = timezone.now()
            obj.created_time = timezone.now()
            
        obj.name = name
        obj.mac = mac
        obj.os = os
        obj.kernel = kernel
        obj.cpu =cpu
        obj.cpu_core = cpu_core
        obj.cpu_thread = cpu_thread
        obj.arch = arch
        obj.mem = mem
        obj.disk = disk

        obj.last_time = timezone.now()
        obj.save()
        return obj