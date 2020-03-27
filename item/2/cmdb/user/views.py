# encoding: utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse

from .models import User
from .validators import UserValiator

def index(request):
    if not request.session.get('user'):
        return redirect('user:login')

    return  render(request, 'user/index.html', {
                    'users' : User.objects.all()
                    })


def login(request):
    if 'GET' == request.method:
        return render(request, 'user/login.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = UserValiator.valid_login(name, password)
        print(user)
        if user:
            request.session['user'] = user.as_dict()
            return redirect('user:index')
        else:
            return render(request, 'user/login.html', {
                'name': name, 
                'errors': {'default':'用户名或者密码错误'}
                })


def logout(request):
    request.session.flush()
    return redirect('user:login')


def create_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    is_valid, user, errors = UserValiator.valid_create(request.POST)
    
    if is_valid:
        user.save()
        return JsonResponse({'code' : 200 })
    else:
        return JsonResponse({'code' : 400, 'errors' : errors })


def delete_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    id = request.GET.get('id', '')
    User.objects.filter(pk=id).delete()

    return JsonResponse({'code' : 200 })


def edit_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    is_valid, user, errors = UserValiator.valid_update(request.POST)
    if is_valid:
        user.save()
        return JsonResponse({'code' : 200 })
    else:
        return JsonResponse({'code' : 400, 'errors' : errors, 'result' : user.as_dict()})


def get_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    uid = request.GET.get('id', '')
    user = User.objects.get(pk=uid)

    return  JsonResponse({'code' : 200, 'result': user.as_dict()})



def get_pass_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    uid = request.GET.get('id', '')
    user = User.objects.get(pk=uid)

    return  JsonResponse({'code' : 200, 'result': user.as_dict()})


def changepass_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    is_valid, user, errors = UserValiator.valid_changepass(request.POST)
    if is_valid:
        User.objects.filter(pk=user.id).update(password=user.password)
        return JsonResponse({'code' : 200 })
    else:
        return JsonResponse({'code' : 400, 'errors' : errors })
