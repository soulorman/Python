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


def delete(request):
    if not request.session.get('user'):
        return redirect('user:login')

    id = request.GET.get('uid', '')
    User.objects.filter(id=id).delete()

    return redirect('user:index')


def view(request):
    if not request.session.get('user'):
        return redirect('user:login')

    uid = request.GET.get('uid', '')

    return  render(request, 'user/view.html', {
        'user': User.objects.get(pk=uid)
        })


def update(request):
    if not request.session.get('user'):
        return redirect('user:login')

    is_valid, user, errors = UserValiator.valid_update(request.POST)
    if is_valid:
        user.save()
        return redirect('user:index')
    else:
        return  render(request, 'user/view.html', {'user': user, 'errors' : errors})


def create_view(request):
    if not request.session.get('user'):
        return redirect('user:login')   
    
    return render(request, 'user/create.html')


def create(request):
    if not request.session.get('user'):
        return redirect('user:login')

    is_valid, user, errors = UserValiator.valid_create(request.POST)
    if is_valid:
        user.save()
        return redirect('user:index')
    else:
        return render(request, 'user/create.html', {'errors' : errors})


def changepass_view(request):
    if not request.session.get('user'):
        return redirect('user:login')

    uid = request.GET.get('uid', '')

    return render(request, 'user/changepass.html', {'user': User.objects.get(pk=uid)})


def changepass(request):
    if not request.session.get('user'):
        return redirect('user:login')

    is_valid, user, errors = UserValiator.valid_changepass(request.POST)
    if is_valid:
        User.objects.filter(id=user.id).update(password=user.password)
        return redirect('user:index')
    else:
        return render(request, 'user/changepass.html', {'user': user,'errors' : errors})


def create_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    is_valid, user, errors = UserValiator.valid_create(request.POST)
    if is_valid:
        user.save()
        return JsonResponse({'code' : 200 })
    else:
        return JsonResponse({'code' : 400, 'errors' : errors })