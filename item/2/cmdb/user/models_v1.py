# encoding: utf-8
import json
from django.db import models

DATA_FILE = 'user.data.json'

def get_users():
    f = open(DATA_FILE, 'rt')
    users = json.loads(f.read())
    f.close()

    return users


def dump_users(users):
    f = open(DATA_FILE, 'wt')
    f.write(json.dumps(users))
    f.close()

    return True


def valid_user(name, password):
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
    is_valid = True
    errors = {}
    user = {}
    users = get_users()

    user['id'] = params.get('id', 0).strip()
    if users.get(user['id']) is None:
        errors['id'] = '用户信息不存在'
        is_valid = False
    
    user['name'] = params.get('name', '').strip()
    
    for uid, cuser in users.items():
        if cuser['name'] == user['name'] and uid != user['id'] :
            errors['name'] = '用户名已存在'
            break

    user['age'] = params.get('age', 0).strip()
    if not user['age'].isdigit():
        errors['age'] = '年龄格式错误'
        is_valid = False

    user['tel'] = params.get('tel', '0').strip()
    user['sex'] = int(params.get('sex', 1).strip())

    return is_valid, user, errors


def update_user(params):
    uid = params.pop('id')
    users = get_users()

    users[uid].update(params)
    
    return dump_users(users)


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