# encoding: utf-8
from django.db import models
import datetime

class BaseModels(models.Model):
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