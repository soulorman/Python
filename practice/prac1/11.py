# encoding:utf-8

users = []
users.append((1,'kk',29,'136xxxxxxxx'))
users.append((2,'wd',12,'1362xxxxxxxx'))
users.append((3,'woniu',34,'133xxxxxxxx'))

tpl_title = '|{0:^10s}|{1:^10s}|{2:^5s}|{3:^15s}|'
colums_title = ('id','name','age','tel')

tpl_body = '|{0:^10d}|{1:^10s}|{2:^5d}|{3:^15s}|'

title = tpl_title.format(colums_title[0],colums_title[1],colums_title[2],colums_title[3])
splitline = '-' * len(title)

print(splitline)
print(title)
print(splitline)

for user in users:
    print(tpl_body.format(user[0],user[1],user[2],user[3]))
print(splitline)



