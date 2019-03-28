#enconding: utf-8

import json

tpl_title = '|{0:^10s}|{1:^20s}|{2:^10s}|{3:^5s}|{4:^15s}|'
colums_title = ('id','password','name','age','tel')

tpl_body = '|{uid:^10d}|{password:20s}|{name:^10s}|{age:^5d}|{tel:^15s}|'
title = tpl_title.format(colums_title[0],colums_title[1],colums_title[2],colums_title[3],colums_title[4])

splitline = '-' * len(title)

DATA_FILE = 'user.data.txt'

def load_data():
    f = open(DATA_FILE,'rt')
    cxt = f.read()
    f.close()   

    users = json.loads(cxt) 
    return {int(key):value for key,value in users.items()}
 
def save_data(users):
    f = open(DATA_FILE,'wt')
    f.write(json.dumps(users))
    f.close()
    return True

def login():
    users = load_data()
    isLogin = False
    for _ in range(3):
        text = input('请输入用户名和密码(users/passwd):')
        username,password = text.split('/')
        for k,user in users.items():
            if user['name'] == username and user['password'] == password:
                isLogin =True
                break
        
        if isLogin:
            print('ok')
            break
        else:
            print('error')
    return isLogin

def input_add_user():
    is_valid = False
    user = {}

    text = input('请输入用户信息:')
    nodes = text.split(',')
    if len(nodes) !=4:
        print('输入信息有误')
    else:
        if not nodes[1].isdigit():
            print('年龄有误')
        else:
            user = {'name':nodes[0],'age':int(nodes[1]),'tel':nodes[2],'password':nodes[3]}
            is_valid = True
    return is_valid,user

def add_user():
    is_valid,user =  input_add_user()
    if is_valid:
        users = load_data()
        uid = 1
        if users:
            uid = max(users) + 1
        users[uid] = user
        save_data(users)
        print('添加成功')

def input_delete_user():
    is_valid = False
    uid = input('请输入删除的用户ID:')
    if not uid.isdigit():
        print('输入信息有误')

    return is_valid,uid

def delete_user():
    is_valid,uid = input_delete_user()
    if is_valid:
        users = load_data()
        user = users.pop(int(uid),None)
        save_data(users)
        print('删除成功')

def input_update_user():
    users = load_data()
    is_valid, user = False, {}
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
                is_valid = True
                uid = int(uid)
                user = {'age':int(nodes[0]),'tel':nodes[1],'password':nodes[2]}

    return is_valid,uid,user

def update_user():
    is_valid,uid,user = input_update_user()
    if is_valid:
        users = load_data()
        users[uid].update(user)
        save_data(users)
        print('更改成功')

def list_user():
    users = load_data()
    print(splitline)
    print(title)
    print(splitline)
    for key,value in users.items():
        print(tpl_body.format(uid=key,name=value['name'],age=int(value['age']),tel=value['tel'],password=len(value['password']) * '*'))
    print(splitline)

def find_user():
    users = load_data()
    text = input('请输入查找的字符串:')
    for key,value in users.items():
        if text in value['name']:
            print(tpl_body.format(uid=key,name=value['name'],age=int(value['age']),tel=value['tel'],password=value['password'] * '*'))

def main():
    login_ok = login()
    if not login_ok:
        print('登录失败')
        return
    actions = {
        'add' : add_user,
        'delete' : delete_user,
        'update' : update_user,
        'list' : list_user,
        'find' : find_user,
    }
    while True: 
        operate = input('请输入操作(add/delete/update/find/list/exit):')
        if 'exit' == operate:
            break
        func = actions.get(operate)
        if func:
            func()
        else:
            print('输入操作有误')

if __name__ =='__main__':
    main()
