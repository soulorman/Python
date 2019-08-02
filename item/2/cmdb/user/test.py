#encoding: utf-8

import random
class Animal(object):
    def __init__(self, name, blood=100, ):
        self.name = name
        self.blood = blood
        self.icon = 'Animal'

    def get_blood(self):
        return self.blood

    def drop_blood(self, drop):
        self.blood -= drop

    def attack(self, rival):
        drop = random.randint(0, 20)
        rival.drop_blood(drop)

class Dog(Animal):
    def __init__(self, name, blood=100):
        self.name = name
        self.blood = blood
        self.icon = 'Dog'

class Cat(Animal):
    def __init__(self, name, blood):
        super().__init__(name, blood, 'Cat')
        #super(Cat, self).__init__(name, blood, 'Cat')

wangwang = Dog('wangwang')

miaomiao = Cat('miaomiao', 120)


