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
        return drop

class Dog(Animal):
    def __init__(self, name, blood=100):
        self.name = name
        self.blood = blood
        self.icon = 'Dog'

class Cat(Animal):
    def __init__(self, name, blood):
        super().__init__(name, blood)
        self.icon = 'Dog'

wangwang = Dog('wangwang')
miaomiao = Cat('miaomiao', 120)


while True:
    lost_blood = wangwang.attack(miaomiao)
    free_blood = miaomiao.get_blood()
    print('wangwang 发起了攻击: miaomiao 失去了 {0} 生命值，还剩 {1} 生命值'.format(lost_blood, free_blood))
    if miaomiao.get_blood() <= 0:
        print('wangwang win')
        break

    lost_blood = miaomiao.attack(wangwang)
    free_blood = wangwang.get_blood()
    print('miaomiao 发起了攻击: wangwang 失去了 {0} 生命值，还剩 {1} 生命值'.format(lost_blood, free_blood))
    if wangwang.get_blood() <= 0:
        print('miaomiao win')
        break

