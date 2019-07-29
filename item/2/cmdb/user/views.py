from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import time

def index(request):
    return  render(request, 'user/index.html', {'current_time': time.time()})
   # return HttpResponse('我的第一个网页')
