#enconding: utf-8

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'webanalysis/index.html')

def upload(request):
    log = request.FILES.get('log')
    if log:
        print(dir(log))
        print(log.read())

    return HttpResponse("upload")