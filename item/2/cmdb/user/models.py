# encoding: utf-8
import json

from django.db import models
from .dbutils import DBconnection


class User(object):
    SQL_LOGIN = '''
                    SELECT id,name,age,tel,sex 
                    FROM user 
                    where name=%s and password=%s LIMIT 1;
                '''

    SQL_LIST =  '''
                    SELECT id,name,age,tel,sex 
                    FROM user;
                '''            

    SQL_GET_BY_ID = '''
                        SELECT id,name,age,tel,sex 
                        FROM user
                        WHERE id=%s;
                     '''

    SQL_GET_BY_NAME = '''
                            SELECT id,name,age,tel,sex 
                            FROM user
                            WHERE name=%s;
                       '''

    SQL_UPDATE =   '''
                        UPDATE user
                        SET name=%s,
                            age=%s,
                            tel=%s,
                            sex=%s
                        WHERE id=%s;   
                    '''

    SQL_CREATE =   '''
                            INSERT INTO user(name,password,age,tel,sex )
                            VALUES(%s,%s,%s,%s,%s);
                        '''

    SQL_DELETE =   '''
                        DELETE FROM user WHERE id=%s;
                    '''


    def __init__(self, id=None, name='', age=0, tel='', sex=1, password=''):
        self.id = id
        self.name = name
        self.age = age
        self.tel = tel
        self.sex = sex
        self.password = password


    @classmethod
    def valid_login(cls, name, password):
        args = (name, password, )
        cnt, result = DBconnection.execute_mysql(cls.SQL_LOGIN, args, one=True)

        return User(id=result[0], name=result[1], age=result[2], tel=result[3], sex=result[4]) if result else None   


    @classmethod
    def get_list(cls):
        cnt, result = DBconnection.execute_mysql(cls.SQL_LIST)

        return [
                User(id=line[0], name=line[1], age=line[2], tel=line[3], sex=line[4])
                for line in result
            ]


    @classmethod        
    def get_by_id(cls, id):
        cnt, result = DBconnection.execute_mysql(cls.SQL_GET_BY_ID, (id, ), one=True)

        return User(id=result[0], name=result[1], age=result[2], tel=result[3], sex=result[4]) if result else None


    @classmethod  
    def get_by_name(cls, name):
        cnt, result = DBconnection.execute_mysql(cls.SQL_GET_BY_NAME, (name, ), one=True)

        return User(id=result[0], name=result[1], age=result[2], tel=result[3], sex=result[4]) if result else None  


    @classmethod 
    def valid_name_unique(cls, name, uid=None):
        user = cls.get_by_name(name)
        if user is None:
            return True
        else:
            return str(user.id) == uid


    @classmethod
    def valid_update(cls, params):
        is_valid = True
        errors = {}
        user = User()

        user.id = params.get('id', '').strip()
        if cls.get_by_id(user.id) is None:
            is_valid = False
            errors['id'] = '用户信息不存在'    
            
        user.name = params.get('name', '').strip()
        if user.name == '':
            is_valid = False
            errors['name'] = '用户名不能为空'
        elif not cls.valid_name_unique(user.name, user.id):
            is_valid = False
            errors['name'] = '用户名已存在'

        user.age = params.get('age', '0').strip()
        if not user.age.isdigit():
            is_valid = False
            errors['age'] = '年龄格式错误'

        user.tel = params.get('tel', '0').strip()
        user.sex = int(params.get('sex', '1').strip())

        return is_valid, user, errors


    def update(self):
        args = (self.name, self.age, self.tel, self.sex, self.id)
        DBconnection.execute_mysql(User.SQL_UPDATE, args, fetch=False)

        return True


    @classmethod 
    def valid_create(cls, params):
        is_valid = True
        errors = {}
        user = User()
        
        user.name = params.get('name', '').strip()
        if user.name == '':
            is_valid = False
            errors['name'] = '用户名不能为空'
        elif cls.get_by_name(user.name):
            is_valid = False
            errors['name'] = '用户名已存在'

        user.password = params.get('password', '').strip()
        user.password_1 = params.get('password_1', '').strip()
        if user.password == '' or user.password != user.password_1:
            is_valid = False
            errors['password'] = '密码不能为空,且两次密码不匹配'

        user.age = params.get('age', '0').strip()
        if not user.age.isdigit():
            is_valid = False
            errors['age'] = '年龄格式错误'

        user.tel = params.get('tel', '0').strip()
        user.sex = int(params.get('sex', '1').strip())

        return is_valid, user, errors


    def create(self):
        args = (self.name, self.password, self.age, self.tel, self.sex)
        DBconnection.execute_mysql(User.SQL_CREATE, args, fetch=False)

        return True


    @classmethod 
    def delete_by_id(cls, uid):
        DBconnection.execute_mysql(cls.SQL_DELETE, (uid, ), fetch=False)
       
        return True


    def as_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'age' :  self.age,
            'tel' : self.tel,
            'sex' : self.sex,
            'password' : self.password
        }



SQL_CHANGEPASS_USER =   '''
                            UPDATE user
                            SET password=%s
                            WHERE id=%s;                              
                        '''

SQL_PASSWD_COLUMN = ['id', 'password']
SQL_GET_PASSWD_BY_ID = '''
                        SELECT id,password 
                        FROM user
                        WHERE id=%s;
                        '''


def get_passwd_by_id(uid):
    cnt, result = DBconnection.execute_mysql(SQL_GET_PASSWD_BY_ID, (uid, ), one=True)

    return dict(zip(SQL_PASSWD_COLUMN, result)) if result else None  


def valid_passwd(password_old, uid):
    user = get_passwd_by_id(uid)
    if uid is None or user is None or user['password'] != password_old:
        return True
    else:
        return user['id'] == uid


def valid_changepass(params):
    is_valid = True
    errors = {}
    user = {}   
    
    user['id'] = params.get('id', 0).strip()
    if get_user_by_id(user['id']) is None:
        is_valid = False
        errors['id'] = '用户信息不存在'

    user['password_old'] = params.get('password_old', '').strip()
    if user['password_old'] == '':
        is_valid = False
        errors['password'] = '密码不能为空'
    elif valid_passwd(user['password_old'], user['id']):
        is_valid = False
        errors['password'] = '密码认证失败'

    user['password'] = params.get('password', '').strip()
    user['password_1'] = params.get('password_1', '').strip()
    if user['password'] == '' or user['password_1'] == '':
        is_valid = False
        errors['password_new'] = '新密码不能为空'
    elif user['password'] != user['password_1']:
        is_valid = False
        errors['password_new'] = '新密码不匹配'
        
    if is_valid:
        user = {
                  'id' : user['id'],
                  'password' : user['password']
                }

    return is_valid, user, errors


def changepassword(params):
    args = (params['password'], params['id'])
    cnt, result = DBconnection.execute_mysql(SQL_CHANGEPASS_USER, args, fetch=False)

    return True