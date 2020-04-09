# encoding: utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from backend.models import User,Scores, Other

from .models import  Interview_options, Interview_sort_answer
from .validators import UserValiator

from django.utils import timezone
import datetime
from datetime import timedelta

def index(request):
    if not request.session.get('user'):
        return redirect('answer:login')

    return  render(request, 'answer/index.html')


def login(request):
    if 'GET' == request.method:
        return render(request, 'answer/login.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = UserValiator.valid_login(name, password)
        if user:
            request.session['user'] = user.as_dict()
            return redirect('answer:index')
        else:
            return render(request, 'answer/login.html', {
                'name': name, 
                'errors': {'default':'用户名或者密码错误'}
                })


def logout(request):
    request.session.flush()
    return redirect('answer:login')


def interview_options(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    try:
        #results = Interview_options.objects.all().order_by('question_number').values('question_number','question_title','options_A','options_B','options_C','options_D')
        #results = Interview_options.objects.all().values('question_number','question_title','options_A','options_B','options_C','options_D')
        results = Interview_options.objects.order_by('?')[:3].values('question_number','question_title','options_A','options_B','options_C','options_D')
        result = [ i for i in results]

        return JsonResponse({'code' : 200, 'result': result})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400 ,'errors' : e})


def interview_sort_answer(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    try:
        results = Interview_sort_answer.objects.order_by('?')[:3].values('question_number','question_title')
        result = [ i for i in results]
        return JsonResponse({'code' : 200, 'result': result})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400 ,'errors' : e})


def interview_options_answer(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    # 原计划想返回值是列表的情况
    #request_dict = { i : v  for i,v in request.POST if 'csrf' not in i }    

    scores = 0
    option_answer = {}
    short_answer = {}
    for j in request.POST.keys():
        # 选择题的答案返回并保持在Scores数据库
        if j.startswith('option_'):
            answer_option = request.POST.get(j,0)
            results = Interview_options.objects.filter(question_number=j).values('question_answer','scores')
            option_answer[j] = answer_option

            if results[0].get('question_answer',0) == answer_option:
                scores += results[0].get('scores',0)        
        # 
        elif j.startswith('short_'):
            short_answer[j] = request.POST.get(j,0)
            results = Interview_sort_answer.objects.filter(question_number=j).values('question_answer','scores')

    interviewer_answer = dict(option_answer,**short_answer)

    score = Scores()
    score.name = request.session.get('user')['name']
    score.options_scores = scores
    score.create_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    score.save()

    other = Other()
    other.name = request.session.get('user')['name']
    other.remark = request.session.get('user')['remark']
    other.short_answer = short_answer
    other.interviewer_answer = interviewer_answer
    other.create_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    other.save()

    return HttpResponse("答题完成，请等待试卷批改完成！")
    #return  render(request, 'answer/ok.html')
