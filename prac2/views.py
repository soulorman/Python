#enconding: utf-8

import os
import time
import json

from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import render

from .models import AccessLogFileModel,AccessLog
from django.http import JsonResponse
from django.db.models import Count


def index(request):
    files = AccessLogFileModel.objects.filter(status=0).order_by('-created_time')[:10]
    return render(request,'webanalysis/index.html', {"files" : files})

def upload(request):
    log = request.FILES.get('log')
    if log:
        path = os.path.join(settings.BASE_DIR,'media','uploads', str(time.time()))
        fhandler = open(path, "wb")

        for chunk in log.chunks():
            fhandler.write(log.read(chunk))
        fhandler.close()

        obj = AccessLogFileModel(name=log.name, path=path)
        obj.save()

        path = os.path.join(settings.BASE_DIR,'media','notices', str(time.time()))
        with open(path,'w') as fhandler:
            fhandler.write(json.dumps({'id' : obj.id, 'path' : obj.path}))

    return HttpResponse("upload")


def dist_status_code(request):
    objs = AccessLog.objects.values("status_code").filter(file_id=request.GET.get('id',0)).annotate(codecount=Count("status_code")).order_by('-codecount')

    legend = []
    series = []
    for line in objs:
        legend.append(line.get('status_code'))
        series.append({"name" : line.get('status_code'), "value" : line.get('codecount')})

    return JsonResponse({'code' : 200, 'result' : {'legend' : legend, 'series' : series}})


def trend_visit(request):
    objs = AccessLog.objects.values("status_code").filter(file_id=request.GET.get('id',0)).annotate(codecount=Count("status_code"))

    series = []
    xAxis = []
    for line in objs:
        xAxis.append(line.get('xAxis'))
        series.append({"name" : line.get('status_code'), "value" : line.get('codecount')})

    return JsonResponse({'code' : 200, 'result' : {'xAxis' : xAxis, 'series' : series}})