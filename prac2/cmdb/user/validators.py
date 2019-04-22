#enconding: utf-8
from django.utils import timezone
from .models  import User

class validator(object):

    @classmethod
    def is_interger(cls,value):
        try:
            int(value)
            return True
        except BaseException as e:
            return False


class UserValiator(validator):

    @classmethod
    def valid_login(cls, name, password):
        user = None
        try:
            user = User.objects.get(name=name)
        except BaseException as e:
            print(e)

        if user is None:
            return None
        if user.password == password:
            return user
        return None


    @classmethod
    def valid_name_unique(cls, name, id=None):
        user = None
        try:
            user = User.objects.get(name=name)
        except BaseException as e:
            print(e)

        if user is None:
            return True
        else:
            return str(user.id) == str(id)


    @classmethod
    def valid_update(cls, params):
        is_valid =True
        user = None
        errors = {}

        try:
            user = User.objects.get(pk=params.get('id', '').strip())
        except BaseException as e:
            errors['id'] = '用户信息不存在'
            is_valid = False
            return is_valid, user, errors
        
        name = params.get('name', '').strip()
        if name == '':
            is_valid = False
            errors['name'] = '用户名不能为空'
        elif not cls.valid_name_unique(name, user.id):
            errors['name'] = '用户名已存在'
            is_valid = False
        else:
            user.name = name

        age = params.get('age', '0').strip()
        if not cls.is_interger(age):
            errors['age'] = '年龄格式错误'
            is_valid = False
        else:
            user.age = int(age)

        user.tel = params.get('tel', '').strip()
        user.sex= int(params.get('sex', '1').strip())

        return is_valid, user, errors


    @classmethod
    def valid_create(cls, params):
        is_valid = True
        user = User()
        errors = {}

        user.name = params.get('name',  '').strip()
        if user.name == '':
            is_valid = False
            errors['name'] = '用户名不能为空'
        else:
            try:
                User.objects.get(name=user.name)
                is_valid = False
                errors['name'] = '用户名重复'
            except BaseException as e:
                pass

        user.age = params.get('age',  '0').strip()
        if not user.age.isdigit():
            errors['age'] = '年龄格式错误'
            is_valid = False

        user.tel = params.get('tel',  '')
        user.sex = int(params.get('sex',  '1'))
        user.password = params.get('password',  '').strip()
        user.create_time = timezone.now()

        if user.password == '' or params.get('other_password') != user.password:
            is_valid = False
            errors['password'] = '密码不能为空,  且两次输入密码必须相同'
        
        return is_valid, user, errors