# encoding: utf-8
from django.db import models
import datetime

class User(models.Model):
    name = models.CharField(max_length=32, null=False)
    password = models.CharField(max_length=512, null=False)
    age = models.IntegerField(default=0)
    tel = models.CharField(max_length=32, default='无')
    sex = models.BooleanField(default=True)
    create_time = models.DateTimeField(null=False)

    def as_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'age' :  self.age,
            'tel' : self.tel,
            'sex' : self.sex,
            'password' : self.password
        }