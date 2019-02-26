#encoding: utf-8
path = 'user.data.txt'
fhandler = open(path,'rt')
users = {}
for line in fhandler:
    nodes = line.strip().split(',')
    if len(nodes) == 4:
        users[int(nodes[0])] = {'name': nodes[1],'age': nodes[2],'tel': nodes[3],'password': ''}
    else:
        users[int(nodes[0])] = {'name': nodes[1],'age': nodes[2],'tel': nodes[3],'password': nodes[4]}

fhandler.close()
tpl = '|{uid:10d}|{password:20s}|{name:10s}|{age:5d}|{tel:20s}|'
isLogin =False
for _ in range(3):
    txt = input('please input user,passwd(kk/1): ')
    username,password = txt.split('/')

    for k,user in users.items():
        if user['name'] == username and user['password'] == password:
            isLogin =True
            break
    if  isLogin:
        break
    else:
        print('error')

if not isLogin:
    print('error3')
else:
    print('ok')

    while True:
        operate = input('please add/delete/update/find/list/exit: ')
        if 'add' == operate:
            text = input('please user info(kk,30,152xxxxx,password): ')
            nodes = text.split(',')
            if len(nodes) != 4:
                print('ge shi error')
            else:
                if not nodes[1].isdigit():
                    print('age error')
                else:
                    uid = 1
                    if users:
                        uid = max(users) + 1
                    users[uid] = {'name': nodes[0],'age': int(nodes[1]),'tel': nodes[2],'password': nodes[3]}
                    print('add ok ')
        elif 'delete' == operate:
            uid = input('please input id: ')
            if not uid.isdigit():
                print('info error')
            else:
                user = users.pop(int(uid),None)
                if user:
                    print('del ok')
                else:
                    print('del error')
        elif 'update' == operate:
            uid = input('please edit id: ')
            if not uid.isdigit() or int(uid) not in users:
                print('info error')
            else:
                text = input('please update user info(30,152xxxxx,password): ')
                nodes = text.split(',')
                if len(nodes) != 3:
                    print('ge shi error')
                else:
                    if not nodes[0].isdigit():
                        print('age error')
                    else:
                        users[int(uid)]['age'] = nodes[0]
                        users[int(uid)]['tel'] = nodes[1]
                        users[int(uid)] = {'name': users[int(uid)]['name'],'age' : nodes[0],'tel' : nodes[1],'password' : nodes[2]}
                        print('update ok')
        elif 'list' == operate:
            for key,value in users.items():
                print(tpl.format(uid=key,name=value['name'],age=int(value['age']),tel=value['tel'],password=len(value['password']) * '*'))
        elif 'find' == operate:
            text = input('please input select char: ')
            for key,value in users.items():
                if text in value['name']:
                    print(tpl.format(uid=key,name=value['name'],age=int(value['age']),tel=value['tel'],password=len(value['password']) * '*'))
        elif 'exit' == operate:
            fhandler = open(path,'wt')
            for k,v in users.items():
                fhandler.write('{0},{1},{2},{3},{4}\n'.format(k,v['name'],v['age'],v['tel'],v['password']))
            fhandler.close()
            break
