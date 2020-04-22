# encoding: utf-8
from backend.models import User
from .utils import encrypt_password
from django.utils import timezone


class ValidatorUtils(object):
    """验证用户输入的年龄是否是整数"""

    @staticmethod
    def is_integer(value):
        """验证整数类型"""

        try:
            int(value)
            return True
        except BaseException as e:
            return False


class UserValiator(object):
    """用户验证模块"""

    @classmethod
    def valid_login(cls, name, password):
        """用户登录认证用户名、密码和权限

        :param name: 用户名
        :param password: 密码
        :return: 用户的对象或者报错信息
        """        
        user = None
        try:
            user = User.objects.get(name=name)
        except BaseException as e:
            pass

        if user is None:
            return None
        
        password = encrypt_password(password)
        if user.password == password:
            return user

        return None


    @classmethod 
    def valid_name_unique(cls, name, uid=None):
        '''验证用户名的唯一性

        :param name: 用户名
        :param id: 编号
        :return: 对比结果（反着的）
        '''        
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
        '''更新验证模块

        :param params: 前端返回的数据
        :return: 验证结果、用户对象、报错信息
        '''       
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
        '''注册用户名的验证

        :param params: 前端返回的数据
        :return: 验证结果、用户对象、报错信息
        '''       
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

        user.tel = params.get('tel', '0').strip()
        user.sex = int(params.get('sex', '1').strip())
        user.create_time = timezone.now()

        return is_valid, user, errors


    @classmethod
    def valid_passwd(cls, password, uid=None):
        """密码认证

        :param password: 密码
        :param uid: 用户id
        :return: 密码对比结果
        """        
        user = None
        try:
            user = User.objects.get(pk=uid)
        except BaseException as e:
            pass
        
        password = encrypt_password(password)
        if user is None or user.password != password:
            return True
        else:
            return str(user.id) != str(uid)


    @classmethod 
    def valid_changepass(cls, params):
        """新密码认证

        :param params: 前端请求页面信息
        :return: 验证结果、用户对象、报错信息
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
            user.password = encrypt_password(password_new)

        return is_valid, user, errors