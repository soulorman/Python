# encoding: utf-8

import hashlib

from django.db import models

def encrypt_password(password):
    if not isinstance(password, bytes):
        password = str(password).encode()

    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()


class User(models.Model):
    name = models.CharField(max_length=32, null=False, default='')
    password = models.CharField(max_length=512, null=False, default='')
    age = models.IntegerField(null=False, default=0)
    remark = models.CharField(max_length=32, null=False, default='')
    sex = models.BooleanField(null=False, default=True)
    create_time = models.DateTimeField(null=False)


    def as_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'age' :  self.age,
            'remark' : self.remark,
            'sex' : self.sex,
            'password' : self.password
        }


class Other(models.Model):
    name = models.CharField(max_length=32, null=False, default='')
    short_answer = models.CharField(max_length=128, null=False, default='')
    interviewer_answer = models.TextField(default='无')
    remark = models.TextField(default='无')
    
    create_time = models.DateTimeField(null=False)

    def as_dict(self):
        rt = {}
        for k, v in self.__dict__.items():
            if isinstance(v, (int, float, bool, str)):
                rt[k] = v

        return rt


class Scores(models.Model):
    name = models.CharField(max_length=32, null=False, default='')
    scores = models.CharField(max_length=32, null=False, default='未批改简答题')
    options_scores = models.IntegerField(default=0)
    short_answer_scores = models.TextField(default='0')
    
    create_time = models.DateTimeField(null=False)

    def as_dict(self):
        rt = {}
        for k, v in self.__dict__.items():
            if isinstance(v, (int, float, bool, str)):
                rt[k] = v

        return rt
