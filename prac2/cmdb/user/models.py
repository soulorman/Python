#enconding: utf-8
import json
from django.db import models
from .dbutils  import DBConnection

class User(object):
    SQL_LOGIN = 'SELECT id,name,age,tel,sex FROM user2 where name=%s and password=%s LIMIT 1'

    SQL_LIST = 'SELECT id,name,age,tel,sex FROM user2'
    
    SQL_COLUMN = ['id','name','age','tel','sex']

    SQL_GET_USER_BY_ID = 'SELECT id,name,age,tel,sex FROM user2 where id=%s'
    SQL_GET_USER_BY_NAME = 'SELECT id,name,age,tel,sex FROM user2 where name=%s'
    SQL_UPDATE = 'UPDATE user2 SET name=%s,age=%s,tel=%s,sex=%s WHERE id=%s'
    SQL_CREATE_USER = 'INSERT INTO user2 (name,password,age,tel,sex) values(%s,%s,%s,%s,%s)'
    SQL_DELETE_USER = 'DELETE FROM user2 WHERE id=%s'

    def __init__(self, id=None, name='', age=0, tel='', sex=1, password=''):
        self.id = id
        self.name = name
        self.age = age
        self.tel = tel
        self.sex = sex
        self.password = password

    @classmethod
    def valid_login(cls,name,password):
        args = (name,password,)
        cnt,result =  DBConnection.execute_sql(cls.SQL_LOGIN,args,one=True)

        return User(id=result[0],name=result[1],age=result[2],tel=result[3],sex=result[4]) if result else None


    @classmethod
    def get_list(cls):
        cnt,result = DBConnection.execute_sql(cls.SQL_LIST)
        return [ 
            User(id=line[0],name=line[1],age=line[2],tel=line[3],sex=line[4])
            for line in result
        ]
    @classmethod
    def get_by_id(cls,id):
        cnt,result = DBConnection.execute_sql(cls.SQL_GET_USER_BY_ID,(id,),fetch=True,one=True)
        return User(id=result[0],name=result[1],age=result[2],tel=result[3],sex=result[4]) if result else None


    @classmethod
    def get_by_name(cls,name):
        cnt,result = DBConnection.execute_sql(cls.SQL_GET_USER_BY_NAME,(name,),fetch=True,one=True)
        return User(id=result[0],name=result[1],age=result[2],tel=result[3],sex=result[4]) if result else None


    @classmethod
    def valid_name_unique(cls,name,id=None):
        user = cls.get_by_name(name)
        if user is None:
            return True
        else:
            return str(user.id) == str(uid)

    @classmethod
    def valid_update_user(cls,params):
        is_valid =True
        user = User()
        errors = {}

        user.id = params.get('id','').strip()
        if cls.get_by_id(user.id) is None:
            errors['id'] = '用户信息不存在'
            is_valid = False

        user.name = params.get('name','').strip()
        if user.name == '':
            is_valid = False
            errors['name'] = '用户名不能为空'
        elif not cls.valid_name_unique(user.name,user.id):
            errors['name'] = '用户名已存在'
            is_valid = False  

        user.age = params.get('age','0').strip()
        if not user.age.isdigit():
            errors['name'] = '年龄格式错误'
            is_valid = False

        user.tel = params.get('tel','').strip()
        user.sex= int(params.get('sex','1').strip())

        return is_valid,user,errors

    def update(self):
        args = (self.name, self.age, self.tel, self.sex, self.id)
        DBConnection.execute_sql(self.SQL_UPDATE,args,fetch=False)
        return True

    @classmethod
    def delete_by_id(cls,id):
        DBConnection.execute_sql(cls.SQL_DELETE_USER,(id,),fetch=False)
        return True

    @classmethod
    def valid_create(cls,params):
        is_valid = True
        user = User()
        errors = {}

        user.name = params.get('name', '').strip()
        if user.name == '':
            is_valid = False
            errors['name'] = '用户名不能为空'
        elif cls.get_by_name(user.name):
                is_valid = False
                errors['name'] = '用户名重复'

        user.age = params.get('age', '0').strip()
        if not user.age.isdigit():
            errors['age'] = '年龄格式错误'
            is_valid = False

        user.tel = params.get('tel', '')
        user.sex = int(params.get('sex', '1'))
        user.password = params.get('password', '').strip()

        if user.password == '' or params.get('other_password') != user.password:
            is_valid = False
            errors['password'] = '密码不能为空, 且两次输入密码必须相同'
        
        return is_valid, user, errors


    def create(self):
        args = (self.name,self.password,self.age,self.tel,self.sex)
        DBConnection.execute_sql(self.SQL_CREATE_USER,args,fetch=False)
        return True

    def as_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'age' : self.age,
            'tel': self.tel,
            'sex' : self.sex,
            'password' : self.password
        }