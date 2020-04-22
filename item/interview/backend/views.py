# encoding: utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import User, Scores, Other, UserTitle
from .validators import UserValiator
from .utils import login_required, UserAndTitle, as_dict, ScoreManage

from answer.models import Interview_options, Interview_sort_answer


# 用户主页面的逻辑处理
def index(request):
    '''主页面'''
    if not request.session.get('user') or request.session.get('user')[
            'name'] != 'admin':
        return redirect('backend:login')

    return render(request, 'backend/index.html', {
        'users': User.objects.all()
    })

def login(request):
    '''登录页面'''
    if 'GET' == request.method:
        return render(request, 'backend/login.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')
        user, errors = UserValiator.valid_login(name, password)
        result = {'default': '用户名或者密码错误'}
        if errors:
            result = errors
        if user:
            request.session['user'] = as_dict(user)
            return redirect('backend:index')
        else:
            return render(request, 'backend/login.html', {
                'name': name,
                'errors': result
            })

def logout(request):
    '''注销页面'''
    request.session.flush()
    return redirect('backend:login')

@login_required
def create_ajax(request):
    '''注册用户'''
    is_valid_user, user, errors = UserValiator.valid_create(request.POST)
    if is_valid_user:
        user.save()
        is_valid_user_title, user_title, errors = UserAndTitle.save_user_title(
            user.id)
        if is_valid_user_title:
            user_title.save()
        return JsonResponse({'code': 200})
    else:
        return JsonResponse({'code': 400, 'errors': errors})

@login_required
def delete_ajax(request):
    '''删除用户'''

    id = request.GET.get('id', '')
    User.objects.filter(pk=id).delete()
    return JsonResponse({'code': 200})

@login_required
def flush_ajax(request):
    '''刷新随机题'''
    tmp_id = request.GET.get('id', '')
    try:
        UserTitle.objects.filter(user_id=tmp_id).delete()
        is_valid_user_title, user_title, errors = UserAndTitle.save_user_title(
            tmp_id)
        if is_valid_user_title:
            user_title.save()
        return JsonResponse({'code': 200})
    except BaseException as e:
        return JsonResponse({'code': 400, 'errors': e})

@login_required
def edit_ajax(request):
    '''更新用户信息'''

    is_valid, user, errors = UserValiator.valid_update(request.POST)
    if is_valid:
        user.save()
        return JsonResponse({'code': 200})
    else:
        return JsonResponse(
            {'code': 400, 'errors': errors, 'result': user.as_dict()})

@login_required
def get_ajax(request):
    '''得到用户信息'''

    uid = request.GET.get('id', '')
    user = User.objects.get(pk=uid)

    return JsonResponse({'code': 200, 'result': user.as_dict()})

@login_required
def get_pass_ajax(request):
    '''得到用户密码信息'''
    uid = request.GET.get('id', '')
    user = User.objects.get(pk=uid)

    return JsonResponse({'code': 200, 'result': user.as_dict()})

@login_required
def changepass_ajax(request):
    '''改变用户密码信息'''

    is_valid, user, errors = UserValiator.valid_changepass(request.POST)
    if is_valid:
        User.objects.filter(pk=user.id).update(password=user.password)
        return JsonResponse({'code': 200})
    else:
        return JsonResponse({'code': 400, 'errors': errors})

# 成绩主页面的逻辑处理
@login_required
def scores(request):
    '''得到用户分数页面'''

    result = ScoreManage.main_score()
    return render(request, 'backend/answer_scores.html', {
        'result': result
    })

@login_required
def correct_short(request):
    '''批改简答题的页面'''

    result = ScoreManage.mark_short(request.GET)
    return render(request, 'backend/correct_short.html', {'results': result})

@login_required
def edit_short(request):
    '''传入分数，并记录总分'''

    flag, score, errors = ScoreManage.save_short_score(request.POST)
    if flag:
        score.save()
        return redirect('backend:scores')
    else:
        return render(request, 'backend/correct_short.html', {
            'errors': errors
        })

@login_required
def record(request):
    '''回溯页面'''

    name, option_dict, short_dict = ScoreManage.record_page(request.GET)
    return render(request, 'backend/answer_record.html', {
        'name': name,
        'option_dict': option_dict,
        'short_dict': short_dict,
    })
