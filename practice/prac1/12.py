# encoding:utf-8

users = []
users.append((1,'kk',29,'136xxxxxxxx'))
users.append((2,'wd',12,'1362xxxxxxxx'))
users.append((3,'woniu',34,'133xxxxxxxx'))


'''
让用户从控制台输入format:name,age,tel
'''

while True:
    txt = input('请输入用户信息:(name,age,tel): ')
    nodes = txt.split(',')
    if len(nodes) != 3:
        print('输入信息错误')
    else:
        uid = 0
        for user in users:
            if uid < user[0]:
                uid = user[0]
        nodes[1] = int(nodes[1])
        users.append((uid + 1,)+tuple(nodes))
    print(users)
