#enconding: utf-8

import json

from django.db import models

DATA_FILE = 'user.data.json'

def  get_users():
    fhandler = open(DATA_FILE,'rt')
    users = json.loads(fhandler.read())
    fhandler.close()
    return users

def valid_login(name,password):
    return False