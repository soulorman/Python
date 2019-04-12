#enconding: utf-8

class Cat(object):
    def __init__(self, name, age):
        self.__name = name
        self.age = age
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name


miaomiao = Cat('miaomiao', 1)

miaomiao.set_name('kk')
a =miaomiao.get_name()

print(a)


class Cat(object):
    def __init__(self, name, age):
        self.__name = name
        self._age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value
    
miaomiao = Cat('miaomiao', 1)
b = miaomiao.name
print(b)

miaomiao.name = 'test'
c = miaomiao.name

print(c)

