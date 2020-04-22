# encoding: utf-8
import hashlib

from functools import wraps
from collections import defaultdict

from django.utils import timezone
from django.shortcuts import redirect
from django.http import JsonResponse

from .models import User, Scores, Other, UserTitle
from answer.models import Interview_options, Interview_sort_answer


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
            return redirect('user:login')
        return func(request, *args, **kwargs)

    return wrapper

class UserAndTitle(object):
    """将用户id和随机题目绑定一起"""

    @classmethod
    def select_title(cls, grade, option_question_number,
                     short_question_number):
        """随机筛选出各个阶段需要的题目数量

        :param grade: 难度
        :param option_question_number: 难度等级的选择题数量
        :param short_question_number: 难度等级的简答题数量
        :return: 相应的题号
        """
        option_question_numbers = Interview_options.objects.filter(
            flag=grade).order_by('?')[:option_question_number].values('id')
        short_question_numbers = Interview_sort_answer.objects.filter(
            flag=grade).order_by('?')[:short_question_number].values('id')
        # 只取id的值，列表循环并只取其中字典的值
        option_title_id = [
            v for i in option_question_numbers for k,
            v in i.items()]
        short_title_id = [
            v for i in short_question_numbers for k,
            v in i.items()]

        return option_title_id, short_title_id

    @classmethod
    def save_user_title(cls, id):
        """将用户id和随机题目绑定一起

        :param id:用户id
        :return: 判断错误的标准，具体信息，错误信息
        """
        is_valid = True
        errors = {}
        user_title = UserTitle()
        option_simple, short_simple = cls.select_title('简单', 4, 2)
        option_medium, short_medium = cls.select_title('中等', 4, 2)
        option_hard, short_hard = cls.select_title('困难', 2, 1)
        try:
            user_title.user_id = id
            user_title.option_simple_title = option_simple
            user_title.option_medium_title = option_medium
            user_title.option_hard_title = option_hard
            user_title.short_simple_title = short_simple
            user_title.short_medium_title = short_medium
            user_title.short_hard_title = short_hard
            user_title.create_time = timezone.now()
        except BaseException as e:
            is_valid = True
            errors['error'] = e

        return is_valid, user_title, errors


class ScoreManage(object):
    '''成绩页面处理逻辑'''

    @classmethod
    def main_score(cls):
        '''成绩显示的主页面'''
        scores = Scores.objects.all().values()
        others = Other.objects.all().values()

        score = [i for i in scores ]
        other = [i for i in others ]
        rs = score + other
        result_dict = defaultdict(dict)
        for d in rs:
            id_ = d['id']
            result_dict[id_].update(d)

        return result_dict.values()

    @classmethod
    def mark_short(cls, params):
        '''批改简答题部分'''

        temp_id = params.get('id', '')
        info = Other.objects.all().filter(pk=temp_id).values()
        score_info = Scores.objects.all().filter(pk=temp_id).values()
        # Scores表拿成绩，Other表拿答案
        short_answers = eval(info[0]['short_answer'])
        short_answer_score = eval(score_info[0]['short_answer_scores'])

        temp_list = []
        for k, v in short_answers.items():
            try:
                han_score = short_answer_score[k]
            except BaseException as e:
                han_score = 0

            x = ['serial', 'answer', 'score', 'id']
            y = [k, v, han_score, temp_id]

            temp_list.append(dict(zip(x, y)))

        result = []
        for i in temp_list:
            Serial_Number = [i['serial']]
            title = [j['question_title'] for j in Interview_sort_answer.objects.filter(
                question_number=i['serial']).values('question_title').order_by('question_number')]
            reference_answer = [x['question_answer'] for x in Interview_sort_answer.objects.filter(
                question_number=i['serial']).values('question_answer').order_by('question_number')]
            reference_score = [y['scores'] for y in Interview_sort_answer.objects.filter(
                question_number=i['serial']).values('scores').order_by('question_number')]
            short_answer = [i['answer']]
            short_answer_score = [i['score']]

            result.append(
                Serial_Number +
                title +
                reference_answer +
                reference_score +
                short_answer +
                short_answer_score +
                eval(
                    '[' +
                    temp_id +
                    ']'))

        return result

    @classmethod
    def save_short_score(cls, params):
        '''传入分数并算总分'''

        request_dict = {i: v for i, v in params.lists() if 'csrf' not in i}
        # table_id 为记录的id
        # title_id 为实际题的序号
        score_id = params.get('table_id', '0')
        score = Scores.objects.get(pk=score_id)

        total_answer_scores = 0
        short_answer_scores = {}
        errors = {}

        list1 = request_dict.get('title_id', 0)
        list2 = request_dict.get('score', 0)
        short_answer_scores = dict(zip(list1, list2))

        flag = True
        for short_score in list2:
            short_score = int(short_score)
            if short_score > 20:
                errors['error'] = '单个分数不能超过20分，请重新打分！'
                flag = False
                break

            total_answer_scores += short_score

        total_score = score.options_scores + total_answer_scores

        score.scores = total_score
        score.short_answer_scores = short_answer_scores

        return flag, score, errors

    @classmethod
    def record_page(cls, params):
        '''回溯页面'''

        temp_id = params.get('id', 0)
        info = Other.objects.get(pk=temp_id)
        temp_result = eval(info.interviewer_answer)

        option_list = []
        short_list = []
        
        for k, v in temp_result.items():

            if k.startswith('option_'):
                option = Interview_options.objects.filter(
                    question_number=k).values('question_title','question_answer').order_by('question_number')
                option_title = option[0].get('question_title', '无')                
                option_answer = option[0].get('question_answer', '无')
                option_list.append((option_title,v,option_answer))
            elif k.startswith('short_'):
                short = Interview_sort_answer.objects.filter(
                    question_number=k).values('question_title','question_answer')
                short_title = short[0].get('question_title', '无')
                short_answer = short[0].get('question_answer', '无')
                short_list.append((short_title,v,short_answer))

        return info.name, option_list, short_list