#encoding:utf-8

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

class Host(models.Model):
    ip = models.GenericIPAddressField(null=False, default='0.0.0.0')
    name = models.CharField(max_length=128, null=False, default='')
    os = models.CharField(max_length=64, null=False, default='')
    kernel = models.CharField(max_length=128, null=False, default='')

    cpu = models.IntegerField(null=False, default=0)  
    cpu_core = models.IntegerField(null=False, default=0)
    cpu_thread = models.IntegerField(null=False, default=0)
    arch = models.CharField(max_length=16, null=False, default='')

    mem = models.CharField(max_length=64,null=False, default='')
    disk = models.CharField(max_length=512, null=False, default='{}')
    
    remark = models.TextField(null=False, default='')
    last_time = models.DateTimeField(null=False)

    @classmethod
    def create_or_replace(cls, ip, name, os, kernel, cpu, cpu_core, cpu_thread, arch, mem, disk):
        obj = None
        try:
            obj = cls.objects.get(ip=ip)
        except ObjectDoesNotExist as e:
            obj = cls()
            obj.ip = ip
            obj.remark = '无'

            
        obj.name = name
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

    def as_dict(self):
        return {
            'id' : self.id,
            'ip' : self.ip,
            'name': self.name,
            'os': self.os,
            'kernel': self.kernel,
            'cpu': self.cpu,
            'cpu_core': self.cpu_core,
            'cpu_thread' : self.cpu_thread,
            'arch': self.arch,
            'mem': self.mem,
            'disk': self.disk,
            'last_time': self.last_time,
            'remark': self.remark,
        }
