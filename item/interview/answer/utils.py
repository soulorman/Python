# encoding: utf-8
import hashlib

from functools import wraps

from django.shortcuts import redirect
from django.http import JsonResponse
from django.utils import timezone

from backend.models import Scores, Other, UserTitle
from .models import  Interview_options, Interview_sort_answer


def login_required(func):
    """验证的装饰器

    缓存没有用户，而且没ajax的返回登录页面，缓存有ajax的返回403
    :param :func 验证的方法
    :return: 验证结果
    """
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.session.get('user') is None:
            if request.is_ajax():
                return JsonResponse({'code': 403, 'result': []})
            return redirect('answer:login')
        return func(request, *args, **kwargs)

    return wrapper


def encrypt_password(password):
    '''密码的加密

    :param password: 未加密密码
    :return: 加密完成的密码
    '''
    if not isinstance(password, bytes):
        password = str(password).encode()

    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()

def as_dict(params):
    """把对象转换为可序列化的dict

    :param params:传入对象
    :return: 返回字典
    """
    rt = {}
    # 调用了魔术方法__dict__
    for k, v in params.__dict__.items():
        if isinstance(v, (int, float, bool, str)):
            rt[k] = v

    return rt

class  AnswerTitle(object):
    """答题页面显示，选择题批发，简答题传送"""

    # @classmethod
    # def handle_title(csl, params)

    @classmethod
    def options(cls, params):
        '''选择题部分显示

        :param params: 缓存
        :return: 选择题列表
        '''
        user_id = params.get('user')['id']
        tmp = UserTitle.objects.get(user_id=user_id)

        option_simple = []
        option_medium = []
        option_hard = []
        for i in eval(tmp.option_simple_title):
            option_simple += Interview_options.objects.filter(pk=i).values('question_number','question_title','options_A','options_B','options_C','options_D')
        
        for i in eval(tmp.option_medium_title):
            option_medium += Interview_options.objects.filter(pk=i).values('question_number','question_title','options_A','options_B','options_C','options_D')
    
        for i in eval(tmp.option_hard_title):
            option_hard += Interview_options.objects.filter(pk=i).values('question_number','question_title','options_A','options_B','options_C','options_D')

        result = [i for i in option_simple] + [i for i in option_medium] + [i for i in option_hard]

        return result

    @classmethod
    def short(cls, params):
        '''简答题部分显示

        :param params: 缓存
        :return: 简答题列表
        '''
        user_id = params.get('user')['id']
        tmp = UserTitle.objects.get(user_id=user_id)

        short_simple = []
        short_medium = []
        short_hard = []
        for i in eval(tmp.short_simple_title):
            short_simple += Interview_sort_answer.objects.filter(pk=i).values('question_number','question_title')
        
        for i in eval(tmp.short_medium_title):
            short_medium += Interview_sort_answer.objects.filter(pk=i).values('question_number','question_title')
    
        for i in eval(tmp.short_hard_title):
            short_hard += Interview_sort_answer.objects.filter(pk=i).values('question_number','question_title')

        result = [i for i in short_simple] + [i for i in short_medium] + [i for i in short_hard]

        return result

    @classmethod
    def handle_option_short(cls, params, session):
        '''批改选择题，回传简答题

        :param params: POST请求
        :param session: 缓存
        :return: 是否存储成功
        '''
        # 原计划想返回值是列表的情况
        #request_dict = { i : v  for i,v in params if 'csrf' not in i }    
        flag = False
        scores = 0
        option_answer = {}
        short_answer = {}
        score = Scores()
        other = Other()
        try:
            for j in params.keys():
                # 选择题的答案返回并保持在Scores数据库
                if j.startswith('option_'):
                    answer_option = params.get(j,0)
                    results = Interview_options.objects.filter(question_number=j).values('question_answer','scores')
                    option_answer[j] = answer_option

                    if results[0].get('question_answer',0) == answer_option:
                        scores += results[0].get('scores',0)

                elif j.startswith('short_'):
                    short_answer[j] = params.get(j,0)
                    results = Interview_sort_answer.objects.filter(question_number=j).values('question_answer','scores')

            interviewer_answer = dict(option_answer,**short_answer)
            score.name = session.get('user')['name']
            score.options_scores = scores
            score.create_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            other.name = session.get('user')['name']
            other.remark = session.get('user')['remark']
            other.short_answer = short_answer
            other.interviewer_answer = interviewer_answer
            other.create_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            score.save()
            other.save()
            flag = True
        except BaseException as e:
            raise e

        return flag