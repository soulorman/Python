#enconding: utf-8
import random

class GameAnimal(object):

    def __init__(self,name,blood=100,icon='Animal'):
        self.name = name
        self.blood = blood
        self.icon = icon


    def get_blood(self):
        return self.blood


    def drop_blood(self,drop):
        self.blood -= drop


    def attack(self,rival):
        drop = random.randint(0,20)
        rival.drop_blood(drop)


class Cat(GameAnimal):
    def __init__(self,name,blood=100):
        self.name = name
        self.blood = blood
        self.icon = 'Cat'


class Dog(GameAnimal):
    def __init__(self,name,blood=100):
        super().__init__(name,blood,'Dog')


wangwang = Dog('wangwang')
miaomiao = Cat('miaomiao',120)

while True:
    wangwang.attack(miaomiao)
    if miaomiao.get_blood() <= 0:
        print('['+ wangwang.icon +']' + wangwang.name + ',is win')
        break

    miaomiao.attack(wangwang)
    if wangwang.get_blood() <= 0:
        print('['+ miaomiao.icon +']' + miaomiao.name + ',is win')
        break