#enconding: utf-8

import os
import time
import json
from functools import wraps

from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import AccessLogFileModel,AccessLog
from django.http import JsonResponse
from django.db.models import Count

def login_required(func):

    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.session.get('user') is None:
            if request.is_ajax():
                return JsonResponse({'code' : 403, 'result' : []})
            return redirect('user:login')
        return func(request, *args, **kwargs)

    return wrapper

@login_required
def index(request):
    files = AccessLogFileModel.objects.filter(status=0).order_by('-created_time')[:10]
    return render(request,'webanalysis/index.html', {"files" : files})

@login_required
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

@login_required
def dist_status_code(request):
    objs = AccessLog.objects.values("status_code").filter(file_id=request.GET.get('id',0)).annotate(codecount=Count("status_code")).order_by('-codecount')

    legend = []
    series = []
    for line in objs:
        legend.append(line.get('status_code'))
        series.append({"name" : line.get('status_code'), "value" : line.get('codecount')})

    return JsonResponse({'code' : 200, 'result' : {'legend' : legend, 'series' : series}})

@login_required
def trend_visit(request):

    time = []
    abc = {}
    access_time= AccessLog.objects.filter(file_id=request.GET.get('id',0)).values("access_time")
    for i in access_time:
        time.append(i.get("access_time").strftime("%Y-%m-%d %H:00:00"))

    for j in time:
       if abc.get(j, None) is None:
           abc[j] = 1
       else:
           abc[j] += 1

    series = []
    xAxis = []
    for k,v in abc.items():
        xAxis.append(k)
        series.append(v)

    return JsonResponse({'code' : 200, 'result' : {'xAxis' : xAxis, 'series' : series}})