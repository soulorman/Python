# encoding: utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import User, Scores, Other
from .validators import UserValiator

from answer.models import Interview_options, Interview_sort_answer

def index(request):
    if request.session.get('user')['name'] != 'admin':
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
        user, errors = UserValiator.valid_login(name, password)
        result = {'default':'用户名或者密码错误'}
        if errors:
            result = errors

        if user:
            request.session['user'] = user.as_dict()
            return redirect('backend:index')
        else:
            return render(request, 'backend/login.html', {
                'name': name, 
                'errors': result
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



def correct_short(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    temp_id = request.GET.get('id', '')
    info = Other.objects.all().filter(pk=temp_id).values()
    score_info = Scores.objects.all().filter(pk=temp_id).values()

    short_answers = eval(info[0]['short_answer'])
    short_answer_score = eval(score_info[0]['short_answer_scores'])

    temp_list = []
    for k,v in short_answers.items():
        try:
            han_score = short_answer_score[k]
        except BaseException as e:
            han_score = 0

        x = [ 'serial', 'answer', 'score','id' ]
        y = [ k, v , han_score,temp_id ]
        
        temp_list.append(dict(zip(x,y)))

    result = []
    for i in temp_list:
        Serial_Number =[ i['serial']]
        title = [ j['question_title'] for j in Interview_sort_answer.objects.filter(question_number=i['serial']).values('question_title').order_by('question_number')]
        reference_answer = [x['question_answer'] for x in Interview_sort_answer.objects.filter(question_number=i['serial']).values('question_answer').order_by('question_number')]
        reference_score =[ y['scores'] for y in Interview_sort_answer.objects.filter(question_number=i['serial']).values('scores').order_by('question_number')]
        short_answer =[i['answer']]
        short_answer_score =[i['score']]

        result.append(Serial_Number + title + reference_answer + reference_score + short_answer + short_answer_score + list(temp_id))

    return  render(request, 'backend/correct_short.html',{'results' : result})



def edit_short(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    
    request_dict = { i : v  for i,v in request.POST.lists() if 'csrf' not in i }
    # table_id 为记录的id
    # title_id 为实际题的序号
    score_id = request.POST.get('table_id', '0')
    score = Scores.objects.get(pk=score_id)
    
    total_answer_scores = 0
    short_answer_scores = {}
    errors = {}

    list1 = request_dict.get('title_id',0)
    list2 = request_dict.get('score',0)
    short_answer_scores =  dict(zip(list1,list2))

    flag = True
    for short_score in list2:
        short_score = int(short_score)
        if short_score > 5:
            errors['error'] = '分数不能超过5分，请重新打分！'
            flag = False
            break
        
        total_answer_scores += short_score
     
    total_score = score.options_scores + total_answer_scores


    score.scores = total_score
    score.short_answer_scores = short_answer_scores
    if flag:    
        score.save()
        return redirect('backend:scores')
    else:
        return render(request, 'backend/correct_short.html', {
                'errors': errors
                })
        #return render(request, 'backend/error.html',{'errors' : errors})


def record(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    temp_id = request.GET.get('id', 0)
    info = Other.objects.get(pk=temp_id)
    temp_result = eval(info.interviewer_answer)
    
    option_dict = {}
    short_dict = {}
    for k,v in temp_result.items():
        if k.startswith('option_'):
            option = Interview_options.objects.filter(question_number=k).values('question_title')
            option_title = option[0].get('question_title','无')

            option_dict[option_title] = v

            
        elif k.startswith('short_'):
            short = Interview_sort_answer.objects.filter(question_number=k).values('question_title')
            short_title = short[0].get('question_title','无')

            short_dict[short_title] = v

    return  render(request, 'backend/answer_record.html',{
            'name' : info.name,
            'option_dict' : option_dict,
            'short_dict' : short_dict,
        })   