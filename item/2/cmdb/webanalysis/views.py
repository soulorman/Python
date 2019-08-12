# encoding: utf-8

from django.shortcuts import render,HttpResponse,redirect
import os
from django.conf import settings
import time
import json
from .models import AccessLogFile, AccessLog
from django.http import JsonResponse
from functools import wraps


def login_required(func):

    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.session.get('user') is None:
            if request.is_ajax():
                return JsonResponse({'code':403,'result':[]})
            return redirect('user:login')

        return func(request, *args, **kwargs)

    return wrapper


@login_required
def index(request):
    files = AccessLogFile.objects.filter(status=0).order_by('created_time')[:10]
    return render(request, 'webanalysis/index.html', {"files" : files})


@login_required
def upload(request):
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
    _id = request.GET.get('id', 0)
    legend, series = AccessLog.dist_status_code(_id)

    return JsonResponse({'code' : 200,'result': {'legend':legend, 'series':series }})

@login_required
def tren_visit(request):
    _id = request.GET.get('id', 0)
    xAxis, series = AccessLog.tren_visit(_id)

    return JsonResponse({'code' : 200, 'result' : {'xAxis': xAxis, 'series':series }})