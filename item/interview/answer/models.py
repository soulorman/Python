# encoding: utf-8
from django.db import models

class Interview_options(models.Model):
    '''选择题数据表'''

    question_number = models.TextField(null=False, default='无')
    question_title = models.TextField(null=False, default='无')
    options_A = models.CharField(max_length=64, default='无')
    options_B = models.CharField(max_length=64, default='无')
    options_C = models.CharField(max_length=64, default='无')
    options_D =models.CharField(max_length=64, default='无')
    question_answer = models.TextField(null=False, default='无')
    scores = models.IntegerField(null=False, default=0) 
    update_time = models.DateTimeField(null=False)
    flag = models.CharField(max_length=16, default='')

class Interview_sort_answer(models.Model):
    '''简答题数据表'''

    question_number = models.TextField(null=False, default='无')
    question_title = models.TextField(null=False, default='无')
    question_answer = models.TextField(null=False, default='无')
    scores = models.IntegerField(null=False, default=0)
    flag = models.CharField(max_length=16, default='')
    update_time = models.DateTimeField(null=False)