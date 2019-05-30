#enconding: utf-8

import os
import time
import json

from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import render

from .models import AccessLogFileModel


def index(request):
    return render(request,'webanalysis/index.html')

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