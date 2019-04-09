#encoding: utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import get_users,delete_user
from .models import valid_login as valid_login_func

def index(request):
    if not request.session.get('user'):
        return redirect('user:login')

    return render(request,'user/index.html',{'users' : get_users()})

def login(request):
    if 'GET' == request.method:
        return render(request,'user/login.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = valid_login_func(name,password)
        if user:
            request.session['user'] = user
            return redirect('user:index')
            #return render(request,'user/index.html',{'users' : get_users()})
        else:
            return render(request,'user/login.html',{'name' : name,'errors':{'default' : '用户名密码错误'}})          

def logout(request):
    request.session.flush()
    return redirect('user:login')

def delete(request):
    if not request.session.get('user'):
        return redirect('user:login')

    uid = request.GET.get('uid','')
    delete_user(uid)
    return redirect('user:index')
