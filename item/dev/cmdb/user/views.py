# encoding: utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse

from .models import User
from .validators import UserValiator, login_required


@login_required
def index(request):
    """首页

    查询缓存里有无用户名，有的话，登录首页，没有就是跳转登录页面
    :param: request:前端页面返回的请求内容
    :return: 无
    """
    return  render(request, 'user/index.html', {
                    'users' : User.objects.all()
                    })


def login(request):
    """登录函数

    登录并验证密码对错
    :param: request:前端页面返回的请求内容
    :return: 验证通过就返回主页面，验证不通过返回错误警告
    """
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
                'errors': {'default':'用户名或者密码错误'}
                })


def logout(request):
    """退出登录

    清除缓存并退出
    :param request:前端页面返回的请求内容
    :return: 返回登录页面
    """
    request.session.flush()
    return redirect('user:login')


@login_required
def create_ajax(request):
    """创建用户

    :param request:前端页面返回的请求内容
    :return: 根据验证结果，返回创建成功，或者返回报错信息
    """
    is_valid, user, errors = UserValiator.valid_create(request.POST)
    if is_valid:
        user.save()
        return JsonResponse({'code' : 200 })
    else:
        return JsonResponse({'code' : 400, 'errors' : errors })


@login_required
def delete_ajax(request):
    """删除用户
    
    :param request:前端页面返回的请求内容
    :return: 返回删除成功
    """
    id = request.GET.get('id', '')
    User.objects.filter(pk=id).delete()

    return JsonResponse({'code' : 200 })


@login_required
def get_ajax(request):
    """得到编辑前的用户信息

    :param request:前端页面返回的请求内容
    :return: 返回用户信息
    """
    uid = request.GET.get('id', '')
    user = User.objects.get(pk=uid)

    return  JsonResponse({'code' : 200, 'result': user.as_dict()})


@login_required
def edit_ajax(request):
    """修改用户信息
    
    :param request:前端页面返回的请求内容
    :return: 修改成功或者报错信息
    """
    is_valid, user, errors = UserValiator.valid_update(request.POST)
    if is_valid:
        user.save()
        return JsonResponse({'code' : 200 })
    else:
        return JsonResponse({'code' : 400, 'errors' : errors, 'result' : user.as_dict()})

@login_required
def changepass_ajax(request):
    """修改用户密码
    
    :param request:前端页面返回的请求内容
    :return: 修改成功或者报错信息
    """
    is_valid, user, errors = UserValiator.valid_changepass(request.POST)
    if is_valid:
        User.objects.filter(pk=user.id).update(password=user.password)
        return JsonResponse({'code' : 200 })
    else:
        return JsonResponse({'code' : 400, 'errors' : errors })