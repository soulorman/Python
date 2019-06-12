#enconding: utf-8
from djongo import models
import hashlib

def encrypt_password(password):
    if not isinstance(password, bytes):
        password = str(password).encode()

    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()

class Hardware_Information(models.Model):
    Host_Name = models.CharField(max_length=32, null=False, default='')
    Describe = models.CharField(max_length=1024,null=False, default='')

class User(models.Model):
    name = models.CharField(max_length=32, null=False, default='')
    password = models.CharField(max_length=512, null=False,default='')
    age = models.IntegerField(null=False, default=0)
    tel = models.CharField(max_length=32, null=False,default='')
    sex = models.BooleanField(null=False, default=True)
    create_time = models.DateTimeField(null=False)

    def as_dict(self):
        return {
            'id' : self.id, 
            'name' : self.name, 
            'age' : self.age, 
            'tel': self.tel, 
            'sex' : self.sex, 
            'password' : self.password
        }