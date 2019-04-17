#enconding: utf-8
import json
from django.db import models
from .dbutils  import DBConnection



SQL_LOGIN = 'SELECT id,name,age,tel,sex FROM user2 where name=%s and password=%s LIMIT 1'
SQL_LIST = 'SELECT id,name,age,tel,sex FROM user2'
SQL_COLUMN = ['id','name','age','tel','sex']
SQL_GET_USER_BY_ID = 'SELECT id,name,age,tel,sex FROM user2 where id=%s'
SQL_GET_USER_BY_NAME = 'SELECT id,name,age,tel,sex FROM user2 where name=%s'
SQL_UPDATE_USER = 'UPDATE user2 SET name=%s,age=%s,tel=%s,sex=%s WHERE id=%s'
SQL_CREATE_USER = 'INSERT INTO user2 (name,password,age,tel,sex) values(%s,%s,%s,%s,%s)'
SQL_DELETE_USER = 'DELETE FROM user2 WHERE id=%s'

def get_users():
    cnt,result =  DBConnection.execute_sql(SQL_LIST)
    return [dict(zip(SQL_COLUMN,line)) for line in result]


def valid_login(name,password):
    cnt,result =  DBConnection.execute_sql(SQL_LOGIN,(name,password),one=True)
    return dict(zip(SQL_COLUMN,result)) if result else None


def delete_user(uid):
    DBConnection(SQL_DELETE_USER,(uid,),fetch=False)
    return True


def get_user(uid):
    cnt,result = DBConnection.execute_sql(SQL_GET_USER_BY_ID,(uid,),fetch=True,one=True)
    return dict(zip(SQL_COLUMN,result)) if result else None


def get_user_by_name(name):
    cnt,result = DBConnection.execute_sql(SQL_GET_USER_BY_NAME,(name,),fetch=True,one=True)
    return dict(zip(SQL_COLUMN,result)) if result else None


def valid_name_unique(name,uid):
    user = get_user_by_name(name)
    if user is None:
        return True
    else:
        return str(user['id']) == str(uid)


def valid_update_user(params):
    is_valid =True
    user = {}
    errors = {}

    user['id'] = params.get('id','').strip()
    if get_user(user['id']) is None:
        errors['id'] = '用户信息不存在'
        is_valid = False

    user['name'] = params.get('name','').strip()
    if user['name'] == '':
        is_valid = False
        errors['name'] = '用户名不能为空'
    elif not valid_name_unique(user['name'],user['id']):
        errors['name'] = '用户名已存在'
        is_valid = False  

    user['age'] = params.get('age','0').strip()
    if not user['age'].isdigit():
        errors['name'] = '年龄格式错误'
        is_valid = False

    user['tel'] = params.get('tel','').strip()
    user['sex'] = int(params.get('sex','1').strip())

    return is_valid,user,errors


def update_user(params):
    args = (params['name'],params['age'],params['tel'],params['sex'],params['id'])
    DBConnection.execute_sql(SQL_UPDATE_USER,args,fetch=False)
    return True


def valid_create_user(params):
    is_valid = True
    user = {}
    errors = {}

    user['name'] = params.get('name', '').strip()
    if user['name'] == '':
        is_valid = False
        errors['name'] = '用户名不能为空'
    elif get_user_by_name(user['name']):
            is_valid = False
            errors['name'] = '用户名重复'

    user['age'] = params.get('age', '0').strip()
    if not user['age'].isdigit():
        errors['age'] = '年龄格式错误'
        is_valid = False

    user['tel'] = params.get('tel', '')
    user['sex'] = int(params.get('sex', '1'))
    user['password'] = params.get('password', '').strip()

    if user['password'] == '' or params.get('other_password') != user['password']:
        is_valid = False
        errors['password'] = '密码不能为空, 且两次输入密码必须相同'
    
    return is_valid, user, errors


def create_user(params):
    args = (params['name'],params['password'],params['age'],params['tel'],params['sex'])
    DBConnection.execute_sql(SQL_CREATE_USER,args,fetch=False)
    return True