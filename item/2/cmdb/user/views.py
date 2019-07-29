# encoding: utf-8

from django.shortcuts import render
from django.http import HttpResponse

from .models import get_users

import time

def index(request):
    return  render(request, 'user/index.html', {
                'current_time': time.time(), 
                'users' : get_users()
                })
   # return HttpResponse('我的第一个网页')
