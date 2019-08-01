# encoding: utf-8
import json

from django.db import models
from .dbutils import execute_mysql


SQL_LOGIN = '''
                SELECT id,name,age,tel,sex 
                FROM user 
                where name=%s and password=%s LIMIT 1;
            '''

SQL_LIST_COLUMN = ['id','name','age','tel','sex']
SQL_LIST =  '''
                SELECT id,name,age,tel,sex 
                FROM user;
            '''

SQL_USER_COLUMN = ['id','name','age','tel','sex']
SQL_GET_USER_BY_ID = '''
                        SELECT id,name,age,tel,sex 
                        FROM user
                        WHERE id=%s;
                     '''

SQL_GET_USER_BY_NAME = '''
                            SELECT id,name,age,tel,sex 
                            FROM user
                            WHERE name=%s;
                       '''

SQL_UPDATE_USER =   '''
                        UPDATE user
                        SET name=%s,
                            age=%s,
                            tel=%s,
                            sex=%s
                        WHERE id=%s;   
                    '''

SQL_CREATE_USER =   '''
                        INSERT INTO user(name,password,age,tel,sex )
                        VALUES(%s,%s,%s,%s,%s);
                    '''

SQL_DELETE_USER =   '''
                        DELETE FROM user WHERE id=%s;
                    '''

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


def get_users():
    cnt, result = execute_mysql(SQL_LIST)

    return [
            dict(zip(SQL_LIST_COLUMN, line))
            for line in result
        ]


def valid_login(name, password):
    cnt, result = execute_mysql(SQL_LOGIN, (name, password), one=True)

    return dict(zip(SQL_USER_COLUMN, result)) if result else None


def delete_user(uid):
    cnt, result = execute_mysql(SQL_DELETE_USER, (uid, ), fetch=False)
   
    return True


def get_user_by_id(uid):
    cnt, result = execute_mysql(SQL_GET_USER_BY_ID, (uid, ), one=True)

    return dict(zip(SQL_USER_COLUMN, result)) if result else None


def get_user_by_name(name):
    cnt, result = execute_mysql(SQL_GET_USER_BY_NAME, (name, ), one=True)

    return dict(zip(SQL_USER_COLUMN, result)) if result else None  


def valid_name_unique(name, uid=None):
    user = get_user_by_name(name)
    if uid is None or user is None:
        return True
    else:
        return user['id'] == uid


def valid_update_user(params):
    is_valid = True
    errors = {}
    user = {}

    user['id'] = params.get('id', 0).strip()
    if get_user_by_id(user['id']) is None:
        is_valid = False
        errors['id'] = '用户信息不存在'
        
    user['name'] = params.get('name', '').strip()
    if user['name'] == '':
        is_valid = False
        errors['name'] = '用户名不能为空'
    elif valid_name_unique(user['name'], user['id']):
        is_valid = False
        errors['name'] = '用户名已存在'

    user['age'] = params.get('age', 0).strip()
    if not user['age'].isdigit():
        is_valid = False
        errors['age'] = '年龄格式错误'

    user['tel'] = params.get('tel', '0').strip()
    user['sex'] = int(params.get('sex', 1).strip())

    return is_valid, user, errors


def update_user(params):
    args = (params['name'], params['age'], params['tel'], params['sex'], params['id'])
    cnt, result = execute_mysql(SQL_UPDATE_USER, args, fetch=False)

    return True


def valid_create_user(params):
    is_valid = True
    errors = {}
    user = {}
    
    user['name'] = params.get('name', '').strip()
    if user['name'] == '':
        is_valid = False
        errors['name'] = '用户名不能为空'
    elif get_user_by_name(user['name']):
        is_valid = False
        errors['name'] = '用户名已存在'

    user['password'] = params.get('password', '').strip()
    user['password_1'] = params.get('password_1', '').strip()
    if user['password'] == '' or user['password'] != user['password_1']:
        is_valid = False
        errors['password'] = '密码不能为空,且两次密码不匹配'

    user['age'] = params.get('age', 0).strip()
    if not user['age'].isdigit():
        is_valid = False
        errors['age'] = '年龄格式错误'

    user['tel'] = params.get('tel', '0').strip()
    user['sex'] = int(params.get('sex', 1).strip())

    return is_valid, user, errors


def create_user(params):
    args = (params['name'], params['password'], params['age'], params['tel'], params['sex'])
    cnt, result = execute_mysql(SQL_CREATE_USER, args, fetch=False)

    return True


def get_passwd_by_id(uid):
    cnt, result = execute_mysql(SQL_GET_PASSWD_BY_ID, (uid, ), one=True)

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
    cnt, result = execute_mysql(SQL_CHANGEPASS_USER, args, fetch=False)

    return True