# encoding: utf-8
from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse

from .validators import UserValiator
from .utils import login_required, as_dict, AnswerTitle


@login_required
def index(request):
    '''主页面'''

    return  render(request, 'answer/index.html')

def login(request):
    '''登录页面'''

    if 'GET' == request.method:
        return render(request, 'answer/login.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = UserValiator.valid_login(name, password)
        if user:
            request.session['user'] = as_dict(user)
            return redirect('answer:index')
        else:
            return render(request, 'answer/login.html', {
                'name': name, 
                'errors': {'default':'用户名或者密码错误'}
                })

def logout(request):
    '''注销页面'''
    request.session.flush()
    return redirect('answer:login')

@login_required
def interview_options(request):
    '''选择题展示'''
    try:
        result = AnswerTitle.options(request.session)
        return JsonResponse({'code' : 200, 'result': result})
    except BaseException as e:
        raise e

@login_required
def interview_sort_answer(request):
    '''选择题展示'''
    try:
        result = AnswerTitle.short(request.session)
        return JsonResponse({'code' : 200, 'result': result})
    except BaseException as e:
        raise e    

@login_required
def interview_options_answer(request):
    '''处理选择题/简答题'''
    
    result = AnswerTitle.handle_option_short(request.POST,request.session)
    if result:
        return HttpResponse("答题完成，请等待试卷批改完成！")
