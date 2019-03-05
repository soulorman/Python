

prompt = input('你看到卖西瓜了吗？')
money = 100

print('>>>买一个包子')
print('|||10元')
money = money - 10
if prompt == 'Y':
   print('买一个西瓜')
   print('|||20元')
   money = money - 20
print('|||还剩 ',money)
