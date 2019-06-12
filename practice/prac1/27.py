#enconding: utf-8

path = 'user.data.txt'

fhandler = open(path,'rt')

users = {}

for line in fhandler:
    nodes = line.strip().split(',')
    if len(nodes) == 4:
        users[int(nodes[0])] = {'name' : nodes[1], 'age' : nodes[2], 'tel' : nodes[3], 'password' : ''}
    else:
        users[int(nodes[0])] = {'name' : nodes[1], 'age' : nodes[2], 'tel' : nodes[3], 'password' : nodes[4]}
fhandler.close()

isLogin = False
tpl_title = '|{0:^10s}|{1:^20s}|{2:^10s}|{3:^5s}|{4:^15s}|'
colums_title = ('id','password','name','age','tel')

tpl_body = '|{uid:^10d}|{password:20s}|{name:^10s}|{age:^5d}|{tel:^15s}|'

title = tpl_title.format(colums_title[0],colums_title[1],colums_title[2],colums_title[3],colums_title[4])
splitline = '-' * len(title)

for _ in range(3):
    txt = input('请输入用户名和密码(users/passwd):')
    username,password = txt.split('/')

    for k,user in users.items():
        if user['name'] == username and user['password'] == password:
            isLogin =True
            break

    if isLogin:
        break
    else:
        print('登录失败')
        
if not isLogin:
    print('登录失败')
else:
    print('登录成功')
    while True:
        operate = input('请输入操作(add/delete/update/find/list/exit):')
        if operate == 'add':
            text = input('请输入用户信息:')
            nodes = text.split(',')
            if len(nodes) !=3:
                print('输入信息有误')
            else:
                if not nodes[1].isdigit():
                    print('年龄有误')
                else:
                    uid = 1
                    if users:
                        uid = max(users) + 1
                    users[uid] = {'name':nodes[0],'age':int(nodes[1]),'tel':nodes[2],'password':nodes[3]}
                    print('添加成功')
        elif operate == 'delete':
            uid = input('请输入删除的用户ID:')
            if not uid.isdigit():
                print('输入信息有误')
            else:
                user = users.pop(int(uid),None)
                if user:
                    print('删除成功')
                else:
                    print('删除失败')
        elif operate == 'update':
            uid = input('请输入要修改的用户ID:')
            if not uid.isdigit() or int(uid) not in users:
                print('输入信息有误')
            else:
                text = input('请输入用户信息(不能改名字):')
                nodes = text.split(',')
                if len(nodes) !=3:
                    print('输入信息有误')
                else:
                    if not nodes[0].isdigit():
                        print('年龄有误')
                    else:
                        uid = int(uid)
                        users[uid]['age'] = nodes[0]
                        users[uid]['tel'] = nodes[1]
                        users[uid]['password'] = nodes[2]

                        users[uid] = {'name':users[uid]['name'],'age':int(nodes[0]),'tel':nodes[1],'password':nodes[2]}
                        print('更改成功')
        elif operate == 'list':
            print(splitline)
            print(title)
            print(splitline)
            for key,value in users.items():
                print(tpl_body.format(uid=key,name=value['name'],age=int(value['age']),tel=value['tel'],password=len(value['password']) * '*'))
            print(splitline)
        elif operate == 'find':
            text = input('请输入查找的字符串:')
            for key,value in users.items():
                if text in value['name']:
                    print(tpl_body.format(uid=key,name=value['name'],age=int(value['age']),tel=value['tel'],password=value['password']))
        elif operate == 'exit':
            fhandler = open(path,'wt')
            for k,v in users.items():
                fhandler.write('{0},{1},{2},{3},{4}\n'.format(k,v['name'],v['age'],v['tel'],v['password']))

            fhandler.close()    
    
            print('bye~')
            break
