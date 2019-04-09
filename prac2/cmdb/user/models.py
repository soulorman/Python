#enconding: utf-8

import json

from django.db import models

DATA_FILE = 'user.data.json'

def  get_users():
    fhandler = open(DATA_FILE,'rt')
    users = json.loads(fhandler.read())
    fhandler.close()
    return users

def dump_users(users):
    fhandler = open(DATA_FILE,'wt')
    fhandler.write(json.dumps(users))
    fhandler.close()
    return True

def valid_login(name,password):
    users = get_users()
    for uid,user in users.items():
        if user['name'] == name and user['password'] == password:
            user['id'] = uid
            return user
    return None

def delete_user(uid):
    users = get_users()
    users.pop(uid,None)
    dump_users(users)
    return True
