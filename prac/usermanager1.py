#encoding: utf-8
path = 'user.data.txt'
fhandler = open(path,'rt')
users = {}
for line in fhandler:
    nodes = line.strip().split(',')
    users[int(nodes[0])] = {'name': nodes[1],'age': nodes[2],'tel': nodes[3]}
fhandler.close()
tpl = '|{uid:10d}|{name:10s}|{age:5d}|{tel:20s}|'
while True:
    operate = input('please add/delete/update/find/list/exit: ')
    if 'add' == operate:
        text = input('please user info(kk,30,152xxxxx): ')
        nodes = text.split(',') 
        if len(nodes) != 3:
            print('ge shi error')
        else:
            if not nodes[1].isdigit():
                print('age error')
            else:
                uid = 1
                if users:
                    uid = max(users) + 1
                users[uid] = {'name': nodes[0],'age': int(nodes[1]),'tel': nodes[2]}
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
            text = input('please update user info(30,152xxxxx): ')
            nodes = text.split(',')
            if len(nodes) != 2:
                print('ge shi error')
            else:
                if not nodes[0].isdigit():
                    print('age error')
                else:
                    users[int(uid)]['age'] = nodes[0]   
                    users[int(uid)]['tel'] = nodes[1]   
                    users[int(uid)] = {'name': users[int(uid)]['name'],'age' : nodes[0],'tel' : nodes[1]}
                    print('update ok')
    elif 'list' == operate:
        for key,value in users.items():
            print(tpl.format(uid=key,name=value['name'],age=int(value['age']),tel=value['tel']))
    elif 'find' == operate:
        text = input('please input select char: ')
        for key,value in users.items():
            if text in value['name']:
                print(tpl.format(uid=key,name=value['name'],age=int(value['age']),tel=value['tel']))
    elif 'exit' == operate:
        fhandler = open(path,'wt')
        for k,v in users.items():
            fhandler.write('{0},{1},{2},{3}\n'.format(k,v['name'],v['age'],v['tel']))
        fhandler.close()
        break
