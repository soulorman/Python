# encoding: utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import User, Scores, Other
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

    score = Scores.objects.all().values()
    other = Other.objects.all().values()

    result = []
    for i in score: 
        for j in other:
            if i['id'] == j['id']:
                i.update(j)
                result.append(i)

    return  render(request, 'backend/answer_scores.html', {
                    'result' : result
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
    info = Other.objects.all().filter(pk=uid).values()
    info1 = Scores.objects.all().filter(pk=uid).values()

    first = eval(info[0]['short_answer'])
    b = eval(info1[0]['short_answer_scores'])


    li = []
    for k,v in first.items():
        try:
            han_score = b[k]
        except BaseException as e:
            han_score = 0

        x = [ 'serial', 'answer', 'score','id' ]
        y = [ k, v , han_score,uid ]
        
        li.append(dict(zip(x,y)))

    to = []
    for i in li:
        Serial_Number =[ i['serial']]
        title = [ j['question_title'] for j in Interview_sort_answer.objects.filter(question_number=i['serial']).values('question_title').order_by('question_number')]
        reference_answer = [x['question_answer'] for x in Interview_sort_answer.objects.filter(question_number=i['serial']).values('question_answer').order_by('question_number')]
        reference_score =[ y['scores'] for y in Interview_sort_answer.objects.filter(question_number=i['serial']).values('scores').order_by('question_number')]
        short_answer =[i['answer']]
        short_answer_score =[i['score']]

        to.append(Serial_Number + title + reference_answer + reference_score + short_answer + short_answer_score + list(uid))

    return  JsonResponse({'code' : 200, 'result': to})


def edit_short(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    score_id = request.POST.get('id', '0')
    score = Scores.objects.get(pk=score_id)

    total_answer_scores = 0
    short_answer_scores = {}
    errors = {}
    for i in range(1,3):

        short_answer_score = int(request.POST.get(str(i) + '_score', '0'))
        if short_answer_score > 10:
            errors['error'] = '分数不能超过10分，请重打分！'
            break
        total_answer_scores += short_answer_score
        short_answer_scores[str(i)] = short_answer_score

    total_score = score.options_scores + total_answer_scores

    score.scores = total_score
    score.short_answer_scores = short_answer_scores
    if short_answer_scores:    
        score.save()
        return JsonResponse({'code' : 200 })
    else:
        return JsonResponse({'code' : 400, 'errors' : errors})