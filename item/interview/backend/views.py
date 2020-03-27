# encoding: utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import User, Scores
from .validators import UserValiator

from answer.models import Interview_options, Interview_sort_answer

def index(request):
    if not request.session.get('user'):
        return redirect('backend:login')

    return  render(request, 'backend/index.html', {
                    'users' : User.objects.all()
                    })


def login(request):
    if 'GET' == request.method:
        return render(request, 'backend/login.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = UserValiator.valid_login(name, password)
        if user:
            request.session['user'] = user.as_dict()
            return redirect('backend:index')
        else:
            return render(request, 'backend/login.html', {
                'name': name, 
                'errors': {'default':'用户名或者密码错误'}
                })


def logout(request):
    request.session.flush()
    return redirect('backend:login')


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


def scores(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    return  render(request, 'backend/answer_scores.html', {
                    'scores' : Scores.objects.all().order_by('id').reverse()
                    })


def record(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    return  render(request, 'backend/answer_record.html', {
                    'scores' : Scores.objects.all()
                    })   


def get_short(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    uid = request.GET.get('id', '')
    info = Scores.objects.all().filter(pk=uid).values('short_answer')
    
    to = []
    for i,v in eval(info[0]['short_answer']).items():
        
        a = [ j['question_title'] for j in Interview_sort_answer.objects.filter(question_number=i).values('question_title').order_by('question_number')]
        b = [ v ]
        c = [ i ]
        to.append([ c + a + b ])

    return  JsonResponse({'code' : 200, 'result': to})



def edit_short(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    uid = request.GET.get('id', '')
    user = Scores.objects.get(pk=uid)

    return  JsonResponse({'code' : 200, 'result': user.as_dict()})