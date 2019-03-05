

prompt = input('你看到卖西瓜了吗？')
money = 100

if prompt == 'N':
    print('>>>买一个包子')
    print('|||10元')
    money = money - 10
else:
    print('>>>买一斤包子')
    print('|||花费 10元')
    money = money - 10
print('还剩',money)
