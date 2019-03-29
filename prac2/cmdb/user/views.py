#encoding: utf-8
from django.shortcuts import render
#from django.http import HttpResponse
import time
from user import user

def index(request):
    users = user.load_data()
#    return HttpResponse('我的第一个网页')dd
    return render(request,'user/index.html',{'current_time' :time.time(),'users' : users.items()})
