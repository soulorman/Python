# encoding: utf-8

users = {
    1 : {'name' : 'kk', 'age' : 30, 'tel' : '152xxxx'},
    2 : {'name' : 'wd', 'age' : 23, 'tel' : '151xxxx'},
    3 : {'name' : 'wd', 'age' : 20, 'tel' : '136xxxx'},
}

tpl_title = '|{0:^10s}|{1:^10s}|{2:^5s}|{3:^15s}|'
colums_title = ('ID', 'Name', 'Age', 'Tel')
tpl_body = '|{uid:^10d}|{name:^10s}|{age:^5d}|{tel:^15s}|'

title = tpl_title.format(colums_title[0],colums_title[1],colums_title[2],colums_title[3])
splitline = '-' * len(title)
isLogin = False


for _ in range(3):
    txt = input('请输入用户名和密码(user/passwd):')
    username, password  = txt.split('/')

    for k, user in users.items():
        if user['name'] == username and user['tel'] == password:
            isLogin = True
            break

    if isLogin:
        break
    else:
        print('登录失败')

if not isLogin:
    print('三次失败')
else:
    while True:
        operate = input('请输入操作(add/del/update/list/find/exit):')
        if 'add' == operate:
            text = input('请输入用户信息(示例:kk,30,152xxxx):')
            nodes = text.split(',')
            if len(nodes) != 3:
                print('输入信息有误，请重新操作')
            else:
                if not nodes[1].isdigit():
                    print('输入年龄有误，请重新操作')
                else:
                    uid = 1
                    if users:
                        uid = max(users) + 1

                    users[uid] = {
                                        'name' : nodes[0],
                                        'age' : int(nodes[1]),
                                        'tel' : nodes[2]
                                    }
                    print('添加用户成功!')

        elif 'del' == operate:
            uid = input('请输入删除的用户ID:')
            if not uid.isdigit():
                print('信息有误')
            else:
                user = users.pop(int(uid), None)
                if user:
                    print('删除成功')
                else:
                    print('删除失败，用户不存在')

        elif 'update' == operate:
            uid = input('请输入要更新的用户ID: ')
            if not uid.isdigit() or int(uid) not in users:
                print('信息有误')
            else:
                text = input('请输入用户信息(示例:30,152xxxx):')
                nodes = text.split(',')
                if len(nodes) != 2:
                    print('输入信息有误，请重新操作')
                else:
                    if not nodes[0].isdigit():
                        print('输入年龄有误，请重新操作')
                    else:
                        users[int(uid)]['age'] = int(nodes[0])
                        users[int(uid)]['tel'] = nodes[1]
                        print('更新用户成功!')

        elif 'list' == operate:
            print(splitline)
            print(title)
            print(splitline)
            for k,v in users.items():
                print(tpl_body.format(uid=k,name=v['name'],age=v['age'],tel=v['tel']))
            print(splitline)

        elif 'find' == operate:
            text = input('请输入要查询的用户名:')
            #1. 如果数据重复，会只显示最后一个
            #end_print = '没有找到'
            #for k,v in users.items():
            #    if v['name'].find(text) != -1:
            #        end_print = tpl_body.format(uid=k,name=v['name'], age=v['age'],tel=v['tel'])

            #print(end_print)
            #2. for k,v in users.items():
            #   if v['name'].find(text) != -1:
            #        print(tpl_body.format(uid=k,name=v['name'], age=v['age'],tel=v['tel']))
            # 这里是for的else，如果for里的语句执行完成，就执行else，如果没有执行完成，也就是break了就不执行else
            #else:
            #    print('没有找到')

            # 3. 考虑到了用户名重复的情况
            exist = False
            for k,v in users.items():
                if v['name'].find(text) != -1:
                    exist = True
                    print(tpl_body.format(uid=k,name=v['name'], age=v['age'],tel=v['tel']))

            if not exist:
                print('没有找到')

        elif 'exit' == operate:
            print('bye~')
            exit()
