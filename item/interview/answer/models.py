# encoding: utf-8

import hashlib

from django.db import models

def encrypt_password(password):
    if not isinstance(password, bytes):
        password = str(password).encode()

    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()


class Interview_options(models.Model):
    question_number = models.IntegerField(null=False, default=0)
    question_title = models.TextField(null=False, default='无')
    options_A = models.CharField(max_length=64, default='无')
    options_B = models.CharField(max_length=64, default='无')
    options_C = models.CharField(max_length=64, default='无')
    options_D =models.CharField(max_length=64, default='无')
    question_answer = models.TextField(null=False, default='无')
    scores = models.IntegerField(null=False, default=0) 
    
    update_time = models.DateTimeField(null=False)


    def as_dict(self):
        rt = {}
        for k, v in self.__dict__.items():
            if isinstance(v, (int, float, bool, str,datetime.datetime)):
                rt[k] = v

        return rt


class Interview_sort_answer(models.Model):
    question_number = models.IntegerField(null=False, default=0)
    question_title = models.TextField(null=False, default='无')
    question_answer = models.TextField(null=False, default='无')
    scores = models.IntegerField(null=False, default=0) 
    
    update_time = models.DateTimeField(null=False)


    def as_dict(self):
        rt = {}
        for k, v in self.__dict__.items():
            if isinstance(v, (int, float, bool, str,datetime.datetime)):
                rt[k] = v

        return rt
