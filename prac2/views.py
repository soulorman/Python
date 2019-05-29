#enconding: utf-8

import os
import time

from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'webanalysis/index.html')

def upload(request):
    log = request.FILES.get('log')
    if log:
        path = os.path.join(settings.BASE_DIR,'media','uploads', str(time.time()))
        fhandler = open(path, "wb")
        fhandler.write(log.read())
        fhandler.close()
    return HttpResponse("upload")