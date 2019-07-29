# encoding: utf-8
import json
from django.db import models

DATA_FILE = 'user.data.json'


def get_users():
    f = open(DATA_FILE, 'rt')
    users = json.loads(f.read())
    f.close()

    return users
