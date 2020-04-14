# encoding: utf-8
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=32, null=False)
    password = models.CharField(max_length=512, null=False)
    age = models.IntegerField(default=0)
    tel = models.CharField(max_length=32, default='无')
    sex = models.BooleanField(default=True)
    create_time = models.DateTimeField(null=False)

    def as_dict(self):
        """把对象转换为可序列化的dict

        :param self:传入对象
        :return: 返回字典
        """
        rt = {}
        for k, v in self.__dict__.items():
            if isinstance(v, (int, float, bool, str,datetime.datetime)):
                rt[k] = v

        return rt
