#encoding:utf-8

import random
guess = random.randint(0,100)
count=0

while  True:
    g = input("please input a number: ")
    count += 1
    g = int(g)
    if guess == g:
        print('ok',g)
    elif guess < g:
        print('da le')
    else:
        print('xiao le')
    if count >= 5:
        print('qu si')
        break
