# encoding:utf-8

users = []
users.append((1,'kk',29,'136xxxxxxxx'))
users.append((2,'wd',12,'1362xxxxxxxx'))
users.append((3,'woniu',34,'133xxxxxxxx'))

'''
让用户从控制台输入format:name,age,tel
'''
tpl_title = '|{0:^10s}|{1:^10s}|{2:^5s}|{3:^15s}|'
colums_title = ('id','name','age','tel')

tpl_body = '|{0:^10d}|{1:^10s}|{2:^5d}|{3:^15s}|'

title = tpl_title.format(colums_title[0],colums_title[1],colums_title[2],colums_title[3])
splitline = '-' * len(title)

while True:
    op = input('请输入操作:(add/list/edit/delete)')
    if op == 'list':
        print(splitline)
        print(title)
        print(splitline)
        for user in users:
            print(tpl_body.format(user[0],user[1],user[2],user[3]))
        print(splitline)
    elif op == 'add':
        txt = input('请输入用户信息:(name,age,tel)')
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
    elif op == 'delete':
        uid = int(input('请输入要删除的ID: '))
        for user in users:
            if uid == user[0]:
                users.remove(user)
                break
    elif op == 'edit':
        exists_user = None
        uid = int(input('请输入用户ID： '))
        for user in users:
            if uid == user[0]:
                exists_user = user
                break
        if exists_user:
            txt = input('请输入用户信息:(name,age,tel)')
            nodes = txt.split(',')
            if len(nodes) != 3:
                print('输入信息错误')
            else:
                users.remove(exists_user)
                nodes[1] = int(nodes[1])
                users.append((uid,)+tuple(nodes))
        else:
            print('用户信息不存在')
    elif op == 'find':
        name = input('请输入用户名:' )
        print(splitline)
        print(title)
        print(splitline)
        for user in users:
            if user[1] == name:
                print(tpl_body.format(user[0],user[1],user[2],user[3]))
        print(splitline)
