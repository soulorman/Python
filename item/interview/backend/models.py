# encoding: utf-8
from django.db import models


class User(models.Model):
    '''用户的数据库'''
    name = models.CharField(max_length=32, null=False, default='')
    password = models.CharField(max_length=512, null=False, default='')
    age = models.IntegerField(null=False, default=0)
    remark = models.CharField(max_length=32, null=False, default='')
    sex = models.BooleanField(null=False, default=True)
    create_time = models.DateTimeField(null=False)


class Other(models.Model):
    '''记录答案数据库'''
    name = models.CharField(max_length=32, null=False, default='')
    short_answer = models.CharField(max_length=128, null=False, default='')
    interviewer_answer = models.TextField(default='无')
    remark = models.TextField(default='无')

    create_time = models.DateTimeField(null=False)


class Scores(models.Model):
    '''分数的数据库'''
    name = models.CharField(max_length=32, null=False, default='')
    scores = models.CharField(max_length=32, null=False, default='未批改简答题')
    options_scores = models.IntegerField(default=0)
    short_answer_scores = models.TextField(default='0')

    create_time = models.DateTimeField(null=False)


class UserTitle(models.Model):
    '''记录用户和题的数据库'''
    user_id = models.IntegerField(default=0)
    option_simple_title = models.CharField(
        max_length=32, null=False, default='[]')
    option_medium_title = models.CharField(
        max_length=32, null=False, default='[]')
    option_hard_title = models.CharField(
        max_length=32, null=False, default='[]')

    short_simple_title = models.CharField(
        max_length=32, null=False, default='[]')
    short_medium_title = models.CharField(
        max_length=32, null=False, default='[]')
    short_hard_title = models.CharField(
        max_length=32, null=False, default='[]')

    create_time = models.DateTimeField(null=False)
