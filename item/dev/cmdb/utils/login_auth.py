# encoding: utf-8
from django.shortcuts import redirect
from django.http import JsonResponse
from functools import wraps


def login_required(func):
    """验证的装饰器
    
    缓存没有用户，而且没ajax的返回登录页面，缓存有ajax的返回403
    :param :func 不知道
    :return: 验证结果
    """
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.session.get('user') is None:
            if request.is_ajax():
                return JsonResponse({'code':403,'result':[]})
            return redirect('user:login')
        return func(request, *args, **kwargs)

    return wrapper