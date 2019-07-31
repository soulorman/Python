# encoding: utf-8
import json
from django.db import models

import MySQLdb

MYSQL_HOST = '192.168.31.103'
MYSQL_PORT = 13306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DB = 'cmdb'
MYSQL_CHARSET = 'utf8'

SQL_LOGIN = '''
                SELECT id,name,age,tel,sex 
                FROM user 
                where name=%s and password=%s LIMIT 1;
            '''

SQL_LIST_COLUMN = ['id','name','age','tel','sex']
SQL_LIST = '''
                SELECT id,name,age,tel,sex 
                FROM user;
            '''

SQL_GET_USER_COLUMN = ['id','name','age','tel','sex']
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

SQL_UPDATE_USER = '''
                     UPDATE user
                     SET name=%s,
                        age=%s,
                        tel=%s,
                        sex=%s
                    WHERE id=%s;   
                    '''



def valid_user(name, password):
    conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB, charset=MYSQL_CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_LOGIN,(name,password))
    result = cur.fetchone()
    cur.close()
    conn.close()

    return {'id' : result[0], 'name' : result[1]} if result else None


def get_users():
    conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB, charset=MYSQL_CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_LIST)
    result = cur.fetchall()
    cur.close()
    conn.close()

    return [dict(zip(SQL_LIST_COLUMN, line)) for line in result]


def delete_user(uid):
    users = get_users()
    users.pop(uid, None)
    dump_users(users)

    return True


def get_user_by_id(uid):
    conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB, charset=MYSQL_CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_GET_USER_BY_ID, (uid, ))
    result = cur.fetchone()
    cur.close()
    conn.close()

    return dict(zip(SQL_GET_USER_COLUMN, result)) if result else None


def get_user_by_name(name):
    conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB, charset=MYSQL_CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_GET_USER_BY_NAME, (name, ))
    result = cur.fetchone()
    cur.close()
    conn.close()

    return dict(zip(SQL_GET_USER_COLUMN, result)) if result else None  


def valid_name_unique(name, uid):
    user = get_user_by_name(name)
    if uid is None:
        return True
    else:
        if user is None:
            return True
        else:
            return str(user['id']) == str(uid)


def valid_update_user(params):
    is_valid = True
    errors = {}
    user = {}

    user['id'] = params.get('id', 0).strip()
    if get_user_by_id(user['id']) is None:
        errors['id'] = '用户信息不存在'
        is_valid = False
    
    user['name'] = params.get('name', '').strip()
    if user['name'] == '':
        is_valid = False
        errors['name'] = '用户名不能为空'
    elif not valid_name_unique(user['name'], user['id']):
        errors['name'] = '用户名已存在'
        is_valid = False

    user['age'] = params.get('age', 0).strip()
    if not user['age'].isdigit():
        errors['age'] = '年龄格式错误'
        is_valid = False

    user['tel'] = params.get('tel', '0').strip()
    user['sex'] = int(params.get('sex', 1).strip())

    return is_valid, user, errors


def update_user(params):
    conn = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB, charset=MYSQL_CHARSET)
    cur = conn.cursor()
    args = (params['name'], params['age'], params['tel'], params['sex'], params['id'])
    cur.execute(SQL_UPDATE_USER, args)
    conn.commit()
    cur.close()
    conn.close()
    return True


def valid_add_user(params):
    is_valid = True
    errors = {}
    user = {}
    users = get_users()
    
    user['name'] = params.get('name', '').strip()
    for uid, cuser in users.items():
        if cuser['name'] == user['name'] and uid == user['id']:
            errors['name'] = '用户名已存在'
            is_valid = False
            break

    user['password'] = params.get('password', '').strip()
    user['password_1'] = params.get('password_1', '').strip()
    if user['password'] != user['password_1']:
        errors['password'] = '密码不匹配'
        is_valid = False

    user['age'] = params.get('age', 0).strip()
    if not user['age'].isdigit():
        errors['age'] = '年龄格式错误'
        is_valid = False

    user['tel'] = params.get('tel', '0').strip()
    user['sex'] = int(params.get('sex', 1).strip())

    return is_valid, user, errors


def add_user(params):
    users = get_users()
    uid = 1
    if users:
        uid = int(max(users)) + 1
    
    users[uid] = params

    return dump_users(users)


def valid_changepass(params):
    is_valid = True
    errors = {}
    user = {}
    users = get_users()
    
    user['id'] = params.get('id', 0).strip()
    if users.get(user['id']) is None:
        errors['id'] = '用户信息不存在'
        is_valid = False

    user['password_old'] = params.get('password_old', '').strip()
    for uid, cuser in users.items():
        if cuser['password'] != user['password_old'] and uid == user['id']:
            errors['password_old'] = '旧密码错误'
            is_valid = False
            break

    user['password'] = params.get('password', '').strip()
    user['password_1'] = params.get('password_1', '').strip()
    if user['password'] != user['password_1']:
        errors['password_new'] = '新密码不匹配'
        is_valid = False

    return is_valid, user, errors


def changepassword(params):
    users = get_users()
    uid = params.pop('id')
    user = params.get('password','')
    if user:
        password = {
                    'password' : user
                }

    users[uid].update(password)

    return dump_users(users)