# encoding: utf-8
from django.shortcuts import render,redirect

from .models import get_users,valid_user,delete_user,get_user_by_id,valid_update_user,update_user,valid_add_user,add_user,valid_changepass,changepassword

def index(request):
    if not request.session.get('user'):
        return redirect('user:login')

    return  render(request, 'user/index.html', {
                    'users' : get_users()
                    })


def login(request):
    if 'GET' == request.method:
        return render(request, 'user/login.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = valid_user(name, password)
        if user:
            request.session['user'] = user
            return redirect('user:index')
        else:
            return render(request, 'user/login.html', {'name': name, 'errors': {'default':'用户名或者密码错误'}})


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

    return  render(request, 'user/view.html', {'user': get_user_by_id(uid)})


def update(request):
    if not request.session.get('user'):
        return redirect('user:login')

    is_valid, user, errors = valid_update_user(request.POST)
    if is_valid:
        update_user(user)
        return redirect('user:index')
    else:
        return  render(request, 'user/view.html', {'user': user, 'errors' : errors})


def view(request):
    if not request.session.get('user'):
        return redirect('user:login')

    uid = request.GET.get('uid', '')
    user = get_user_by_id(uid)

    return  render(request, 'user/view.html', {'user': user})


def add_view(request):
    if not request.session.get('user'):
        return redirect('user:login')   
    
    return render(request, 'user/add.html')


def add(request):
    if not request.session.get('user'):
        return redirect('user:login')

    is_valid, user, errors = valid_add_user(request.POST)
    if is_valid:
        add_user(user)
        return redirect('user:index')
    else:
        return render(request, 'user/add.html', {'errors' : errors})


def changepass_view(request):
    if not request.session.get('user'):
        return redirect('user:login')

    uid = request.GET.get('uid', '')
    user = get_user_by_id(uid)
    
    return render(request, 'user/changepass.html', {'user': user})


def changepass(request):
    if not request.session.get('user'):
        return redirect('user:login')

    is_valid, user, errors = valid_changepass(request.POST)
    if is_valid:
        changepassword(user)
        return redirect('user:index')
    else:
        return render(request, 'user/changepass.html', {'user': user,'errors' : errors})