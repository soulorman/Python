#encoding: utf-8

users = []

tpl_title = '|{0:^10s}|{1:^10s}|{2:^5s}|{3:^15s}|'
colums_title = ('ID', 'Name', 'Age', 'Tel')
tpl_body = '|{0:^10d}|{1:^10s}|{2:^5d}|{3:^15s}|'

title = tpl_title.format(colums_title[0],colums_title[1],colums_title[2],colums_title[3])
splitline = '-' * len(title)

users.append((1, 'kk', 29, '136xxxxx'))
users.append((2, 'wd', 28, '136xxxxx'))
users.append((3, 'woniu', 30, '136xxxxx'))

while True:
    op = input('请输入操作(add/del/change/list):')
    if op == 'list':
        print(splitline)
        print(title)
        print(splitline)
        for user in users:
            print(tpl_body.format(user[0],user[1],user[2],user[3]))
        print(splitline)

    elif op == 'add':
        txt = input('请输入用户信息:(name,age,tel):')
        nodes = txt.split(',')
        if len(nodes) != 3:
            print('输入有误')
        else:
            uid = 0
            for user in users:
                if uid < user[0]:
                    uid = user[0]

            nodes[1] = int(nodes[1])
            users.append((uid + 1,) + tuple(nodes))
    elif op == 'del':
        uid = input('请输入删除的用户ID:')
        uid = int(uid)
        for user in users:
            if uid == user[0]:
                users.remove(user)
                print('删除成功!')
                break

    elif op == 'change':
        uid = input('请输入修改用户ID:')
        uid = int(uid)
        exist_user = None
        for user in users:
            if uid == user[0]:
                exist_user = user
                print('你将更改的用户信息:',exist_user)
                break
        if exist_user:
            txt = input('请输入用户信息:(name,age,tel):')
            nodes = txt.split(',')
            if len(nodes) != 3:
                print('输入有误')
            else:
                nodes[1] = int(nodes[1])
                users.remove(exist_user)
                users.append((uid,) + tuple(nodes))
                print('更改完成:',users[-1])
        else:
            print('用户信息不存在')

    elif op == 'exit':
        exit()
    else:
        print('输入错误')
