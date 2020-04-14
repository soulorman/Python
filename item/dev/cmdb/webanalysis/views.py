# encoding: utf-8
from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.http import JsonResponse

from .models import AccessLogFile, AccessLog
from utils.login_auth import login_required

import os
import time
import json


@login_required
def index(request):
    """日志分析首页

    :param: request:前端页面返回的请求内容
    :return: 日志分析首页，所有信息
    """
    files = AccessLogFile.objects.filter(status=0).order_by('created_time')[:3]
    return render(request, 'webanalysis/index.html', {"files" : files})


@login_required
def upload(request):
    """上传文件

    :param: request:前端页面返回的请求内容
    :return: 上传成功页面
    """
    log = request.FILES.get('log', None)
    if log:
        path = os.path.join(settings.BASE_DIR, 'media', 'uploads', str(time.time()))
        f = open(path, 'wb')
        for chunk in log.chunks():
            f.write(log.read())
        f.close()

        obj = AccessLogFile(name=log.name, path=path)
        obj.save()

        path = os.path.join(settings.BASE_DIR, 'media', 'notices', str(time.time()))
        with open(path, 'w') as f:
            f.write(json.dumps({'id':obj.id, 'path':obj.path}))

    return HttpResponse("upload")


@login_required
def dist_status_code(request):
    """扇形图

    :param: request:前端页面返回的请求内容
    :return: x，y轴信息
    """
    _id = request.GET.get('id', 0)
    legend, series = AccessLog.dist_status_code(_id)

    return JsonResponse({'code' : 200,'result': {'legend':legend, 'series':series }})


@login_required
def tren_visit(request):
    """柱状图

    :param: request:前端页面返回的请求内容
    :return: x，y轴信息
    """
    _id = request.GET.get('id', 0)
    xAxis, series = AccessLog.tren_visit(_id)

    return JsonResponse({'code' : 200, 'result' : {'xAxis': xAxis, 'series':series }})