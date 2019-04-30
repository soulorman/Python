#encoding: utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import User
from .validators import UserValiator

def index(request):
    if not request.session.get('user'):
        return redirect('user:login')

    return render(request,'user/index.html',{'users' : User.objects.all()})


def login(request):
    if 'GET' == request.method:
        return render(request,'user/login.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = UserValiator.valid_login(name,password)
        if user:
            request.session['user'] = user.as_dict()
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
    User.objects.filter(id=uid).delete()
    return redirect('user:index')

def view(request):
    if not request.session.get('user'):
        return redirect('user:login')

    uid = request.GET.get('uid','')
    return render(request,'user/view.html',{'user' : User.objects.get(id=uid)})


def update(request):
    if not request.session.get('user'):
        return redirect('user:login')

    is_valid, user, errors = UserValiator.valid_update(request.POST)
    if is_valid:
        user.save()
        return redirect('user:index')
    else:
        return render(request,'user/view.html',{ 'user' : user, 'errors' : errors})


def create(request):
    if not request.session.get('user'):
        return redirect('user:login')
    if 'GET' == request.method:
        return render(request, 'user/create.html')
    else:
        is_valid, user, errors = UserValiator.valid_create(request.POST)
        if is_valid:
            user.save()
            return redirect('user:index')
        else:
            return render(request, 'user/create.html', {'user' : user,'errors' : errors})