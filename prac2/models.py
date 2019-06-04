#encoding: utf-8
from django.db import models


class AccessLogFileModel(models.Model):
    name = models.CharField(max_length=128, null=False, default='')
    path = models.CharField(max_length=1024, null=False, default='')
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)

class AccessLog(models.Model):
    file_id = models.IntegerField(default=0, null=False)
    ip = models.GenericIPAddressField(null=False, default='0.0.0.0')
    url = models.CharField(max_length=1024, null=False, default='')
    status_code = models.IntegerField(default=0, null=False)
    access_time = models.DateTimeField(null=False)