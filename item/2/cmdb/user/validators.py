# encoding: utf-8

from .models import User
from django.utils import timezone

class ValidatorUtils(object):

    @staticmethod
    def is_integer(value):
        try:
            int(value)
            return True
        except BaseException as e:
            return False


class UserValiator(object):

    @classmethod
    def valid_login(cls, name, password):
        user = None
        try:
            user = User.objects.get(name=name)
        except BaseException as e:
            pass

        if user is None:
            return None
        
        if user.password == password:
            return user

        return None


    @classmethod 
    def valid_name_unique(cls, name, uid=None):
        user = None
        try:
            user = User.objects.get(name=name)
        except BaseException as e:
            pass

        if user is None:
            return True
        else:
            return str(user.id) == str(uid)


    @classmethod
    def valid_update(cls, params):
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

        user.tel = params.get('tel', '0').strip()
        user.sex = int(params.get('sex', '1').strip())
        user.create_time = timezone.now()

        return is_valid, user, errors


    @classmethod 
    def valid_create(cls, params):
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

        user.age = params.get('age', '0').strip()
        if not ValidatorUtils.is_integer(user.age):
            is_valid = False
            errors['age'] = '年龄格式错误'
        else:
            user.age = int(user.age)

        user.tel = params.get('tel', '0').strip()
        user.sex = int(params.get('sex', '1').strip())
        user.create_time = timezone.now()

        return is_valid, user, errors


    @classmethod
    def valid_passwd(cls, password, uid=None):
        user = None
        try:
            user = User.objects.get(pk=uid)
        except BaseException as e:
            pass
            
        if user is None or user.password != password:
            return True
        else:
            return str(user.id) != str(uid)


    @classmethod 
    def valid_changepass(cls, params):
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
        if password == '':
            is_valid = False
            errors['password'] = '密码不能为空'
        elif cls.valid_passwd(password, user.id):
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
            user.password = password_new

        return is_valid, user, errors