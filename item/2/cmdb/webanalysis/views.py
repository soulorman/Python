# encoding: utf-8

from django.shortcuts import render,HttpResponse
import os
from django.conf import settings
import time
import json
from .models import AccessLogFile


def index(request):
    files = AccessLogFile.objects.filter(status=0).order_by('-created_time')[:10]
    return render(request, 'webanalysis/index.html', {"files" : files})


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
