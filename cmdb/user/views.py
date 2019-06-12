#encoding: utf-8

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import User
from .validators import UserValiator

def index(request):
    if not request.session.get('user'):
        return redirect('user:login')

    return render(request,'user/index.html', {'users' : User.objects.all()})


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
        else:
            return render(request,'user/login.html',{'name' : name,'errors':{'default' : '用户名或密码错误'}})          

def logout(request):
    request.session.flush()
    return redirect('user:login')


def delete_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' :403})

    uid = request.GET.get('id', '')
    User.objects.filter(id=uid).delete()

    return JsonResponse({'code' : 200})


def create_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' :403})

    is_valid, user, errors = UserValiator.valid_create(request.POST)
    if is_valid:
        user.save()
        return JsonResponse({'code' :200})
    else:
        return JsonResponse({'code' :400, 'errors' : errors})


def get_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' :403})

    uid = request.GET.get('id','')
    try:
        user = User.objects.get(id=uid)
        return JsonResponse({'code' : 200, 'result' : user.as_dict()})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'errors' : { "id" : "操作对象不存在" }})

def update_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' :403})

    is_valid, user, errors = UserValiator.valid_update(request.POST)
    if is_valid:
        user.save()
        return JsonResponse({'code' : 200})
    else:
        return JsonResponse({'code' :400, 'errors' : errors, 'user' : user.as_dict()})
