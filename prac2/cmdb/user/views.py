#encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponse

from .models import get_users
from .models import valid_login as valid_login_func

def index(request):
    return render(request,'user/index.html',{
        'users' : get_users()
        })

def login(request):
    return render(request,'user/login.html')

def valid_login(request):
    name = ''
    password = ''
    user = valid_login_func(name,password)
    if user:
        return render(request,'user/index.html',{'users' : get_users()})
    else:
        return render(request,'user/login.html',{'name' : name,'errors':{'default' : '用户名密码错误'}})

