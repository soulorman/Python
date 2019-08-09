# encoding: utf-8

from django.db import models

class AccessLogFile(models.Model):
    name = models.CharField(max_length=128, null=False, default='')
    path = models.CharField(max_length=1024, null=False, default='')
    status = models.IntegerField(default=0)

    created_time = models.DateTimeField(auto_now_add=True)


class AccessLog(models.Model):
    file_id = models.IntegerField(null=False, default=0)
    ip = models.CharField(max_length=128, null=False, default='')
    url = models.CharField(max_length=1024, null=False, default='')
    status_code = models.IntegerField(null=False, default=0)

    access_time = models.DateTimeField(null=False)