#encoding: utf-8

import json

from django.db import models

DATA_FILE = 'user.data.json'


def get_users():
    fhandler = open(DATA_FILE, 'rt')
    users = json.loads(fhandler.read())
    fhandler.close()
    return users

def dump_users(users):
    fhandler = open(DATA_FILE, 'wt')
    fhandler.write(json.dumps(users))
    fhandler.close()
    return True

def valid_login(name, password):
    users = get_users()
    for uid, user in users.items():
        if user['name'] == name and user['password'] == password:
            user['id'] = uid
            return user

    return None

def delete_user(uid):
    users = get_users()
    users.pop(uid, None)
    dump_users(users)
    return True

def get_user(uid):
    users = get_users()
    user = users.get(uid, {})
    user['id'] = uid
    return user

def valid_update_user(params):
    uid = params.get('id', '')
    name = params.get('name', '')
    tel = params.get('tel', '')
    age = params.get('age', '')
    sex = params.get('sex', '')

    is_valid = True
    user = {}
    errors = {}
    users = get_users()

    user['id'] = params.get('id', '').strip()
    if users.get(user['id']) is None:
        errors['id'] = '用户信息不存在'
        is_valid = False

    user['name'] = params.get('name', '').strip()

    for uid, cuser in users.items():
        if cuser['name'] == user['name'] and uid != user['id']:
            errors['name'] = '用户名已存在'
            is_valid = False
            break

    user['age'] = params.get('age', '0').strip()
    if not user['age'].isdigit():
        errors['age'] = '年龄格式错误'
        is_valid = False

    user['tel'] = params.get('tel', '')
    user['sex'] = int(params.get('sex', '0'))

    return is_valid, user, errors

def update_user(params):
    uid = params.pop('id')
    users = get_users()
    users[uid].update(params)
    return dump_users(users)


def valid_create_user(params):
    name = params.get('name', '')
    tel = params.get('tel', '')
    age = params.get('age', '')
    sex = params.get('sex', '')

    is_valid = True
    user = {}
    errors = {}
    users = get_users()

    user['name'] = params.get('name', '').strip()

    if user['name'] == '':
        is_valid = False
        errors['name'] = '用户名不能为空'
    else:
        for uid, cuser in users.items():
            if cuser['name'] == user['name']:
                errors['name'] = '用户名已存在'
                is_valid = False
                break

    user['age'] = params.get('age', '0').strip()
    if not user['age'].isdigit():
        errors['age'] = '年龄格式错误'
        is_valid = False

    user['tel'] = params.get('tel', '')
    user['sex'] = int(params.get('sex', '0'))
    user['password'] = params.get('password', '').strip()

    if user['password'] == '' or params.get('other_password') != user['password']:
        is_valid = False
        errors['password'] = '密码不能为空, 且两次输入密码必须相同'
    
    return is_valid, user, errors

def create_user(params):
    users = get_users()
    uids = [int(key) for key in users]
    uid = max(uids + [0]) + 1
    users[uid] = params
    return dump_users(users)
    