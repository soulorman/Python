#encoding: utf-8
from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import get_users, delete_user, get_user, \
                    valid_update_user, update_user, \
                    valid_create_user, create_user

from .models import valid_login as valid_login_func

def index(request):
    print(request.session)
    if not request.session.get('user'):
        return redirect('user:login')

    return render(request, 'user/index.html', {
        'users' : get_users()
    })


def login(request):
    if 'GET' == request.method:
        return render(request, 'user/login.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = valid_login_func(name, password)
        if user:
            request.session['user'] = user
            print(request.session)
            return redirect('user:index') 
            # app_name(urls.py=>app_name): route_name(urls.py urlpatterns url name)
            #return redirect('/user/index/')
        else:
            return render(request, 'user/login.html', {
                'name': name,
                'errors' : {'default' : '用户名或密码错误'}
            })


def logout(request):
    request.session.flush()
    return redirect('user:login')


def delete(request):
    if not request.session.get('user'):
        return redirect('user:login')

    uid = request.GET.get('uid', '')
    delete_user(uid)

    return redirect('user:index')


def view(request):
    if not request.session.get('user'):
        return redirect('user:login')

    uid = request.GET.get('uid', '')
    return render(request, 'user/view.html', {
        'user' : get_user(uid)
    })


def update(request):
    if not request.session.get('user'):
        return redirect('user:login')

    is_valid, user, errors = valid_update_user(request.POST)
    if is_valid:
        update_user(user)
        return redirect('user:index')
    else:
        return render(request, 'user/view.html', {
            'user' : user,
            'errors' : errors,
            })


def create(request):
    if not request.session.get('user'):
        return redirect('user:login')

    if 'GET' == request.method:
        return render(request, 'user/create.html')

    else:
        is_valid, user, errors = valid_create_user(request.POST)
        if is_valid:
            create_user(user)
            return redirect('user:index')
        else:
            return render(request, 'user/create.html', {
                'user' : user,
                'errors' : errors,
                })