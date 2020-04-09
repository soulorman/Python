# encoding: utf-8
from django.shortcuts import redirect
from django.http import JsonResponse
from django.utils import timezone

from .models import User
from functools import wraps
import hashlib

def encrypt_password(password: str) -> str:
    """加密用户的密码

    md5加密用户密码
    : param password:明文密码
    : return : 加密后的密码
    """
    if not isinstance(password, bytes):
        password = str(password).encode()

    md5 = hashlib.md5()
    md5.update(password)
    
    return md5.hexdigest()


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


class ValidatorUtils(object):
    @staticmethod
    def is_integer(value):
        """判断是不是int类型，使用方式是强转int类型

        :param value:需要判断/转化的值
        :return: 返回转化成功，或者转化失败
        """
        try:
            int(value)
            return True
        except BaseException as e:
            return False


class UserValiator(object):
    @classmethod
    def valid_login(cls, name, password):
        """认证用户名/密码

        : param name:用户名
        : param password:密码
        : return: 验证成功返回用户信息，验证错误返回None
        """
        user = None
        try:
            user = User.objects.get(name=name)
        except BaseException as e:
        #     pass
        # if user is None:
            return None
        
        password = encrypt_password(password)
        if user.password == password:
            return user

        return None

    @classmethod 
    def valid_name_unique(cls, name, uid=None):
        """验证用户名是否唯一

        :param name:用户名
        :param uid:用户id信息
        :return: true或者false
        """
        user = None
        try:
            user = User.objects.get(name=name)
        except BaseException as e:
            return True

        if user:
            return str(user.id) == str(uid)

    @classmethod
    def valid_update(cls, params):
        """验证用户信息

        :param params:编辑完的用户信息
        :return: 验证信息，新的用户信息，报错信息
        """
        is_valid = True
        errors = {}
        user = None

        try:
            user = User.objects.get(pk=params.get('id', '').strip())
        except BaseException as e:
            is_valid = False
            errors['id'] = '用户信息不存在'
            return is_valid, user, errors

        name = params.get('name', '').strip()
        if name == '':
            is_valid = False
            errors['name'] = '用户名不能为空'
        elif not cls.valid_name_unique(name, user.id):
            is_valid = False
            errors['name'] = '用户名已存在'
        else:
            user.name = name

        age = params.get('age', '0').strip()
        if not ValidatorUtils.is_integer(age):
            is_valid = False
            errors['age'] = '年龄格式错误'
        else:
            user.age = int(age)

        user.tel = params.get('tel', '无').strip()
        user.sex = int(params.get('sex', '1').strip())
        user.create_time = timezone.now()

        return is_valid, user, errors

    @classmethod 
    def valid_create(cls, params):
        """验证创建的用户

        :param params: 创建的用户所有信息
        :return: 返回验证信息，用户信息，错误信息
        """
        is_valid = True
        errors = {}
        user = User()
    
        user.name = params.get('name', '').strip()
        if user.name == '':
            is_valid = False
            errors['name'] = '用户名不能为空'
        else:
            try:
                User.objects.get(name=user.name)
                is_valid = False
                errors['name'] = '用户名已存在'
            except BaseException as e:
                pass

        user.password = params.get('password', '').strip()
        user.password_new = params.get('password_new', '').strip()
        if user.password == '' or user.password != user.password_new:
            is_valid = False
            errors['password'] = '密码不能为空,且两次密码不匹配'
        else:
            user.password = encrypt_password(user.password)

        user.age = params.get('age', '0').strip()
        if not ValidatorUtils.is_integer(user.age):
            is_valid = False
            errors['age'] = '年龄格式错误'
        else:
            user.age = int(user.age)

        user.tel = params.get('tel', '无').strip()
        user.sex = int(params.get('sex', '1').strip())
        user.create_time = timezone.now()

        return is_valid, user, errors

    @classmethod 
    def valid_changepass(cls, params):
        """验证密码

        :param param:传入2个密码
        :return: 返回验证信息，用户信息，错误信息
        """
        is_valid = True
        errors = {}
        user = None

        try:
            user = User.objects.get(pk=params.get('id', '').strip())
        except BaseException as e:
            is_valid = False
            errors['id'] = '用户信息不存在'
            return is_valid, user, errors

        password = params.get('password', '').strip()
        if user.password != encrypt_password(password):
            is_valid = False
            errors['password'] = '密码认证失败'

        password_new = params.get('password_new', '').strip()
        password_new_1 = params.get('password_new_1', '').strip()
        if password_new == '' or password_new_1 == '':
            is_valid = False
            errors['password_new'] = '新密码不能为空'
        elif password_new != password_new_1:
            is_valid = False
            errors['password_new'] = '新密码不匹配'
        else:
            user.password = encrypt_password(password_new)

        return is_valid, user, errors