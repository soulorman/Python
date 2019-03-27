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
    f.write(json.dumps(user))
    f.close()
    return True

def login(users):
    return True
    isLogin = False
    for _ in range(3):
        text = input('请输入用户名和密码(users/passwd):')
        username,password = txt.split('/')
        for user in users:
            if user['name'] == username and user['password'] == password:
                isLogin =True
                break
        if isLogin:
            break
    return isLogin

def add_users(users):
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
def delete_users(users):
    uid = input('请输入删除的用户ID:')
    if not uid.isdigit():
        print('输入信息有误')
    else:
        user = users.pop(int(uid),None)
        if user:
            print('删除成功')
        else:
            print('删除失败')
def update_users(users):
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
def list_users(users):
    print(splitline)
    print(title)
    print(splitline)
    for key,value in users.items():
        print(tpl_body.format(uid=key,name=value['name'],age=int(value['age']),tel=value['tel'],password=len(value['password']) * '*'))
    print(splitline)
def find_users(users):
    text = input('请输入查找的字符串:')
    for key,value in users.items():
        if text in value['name']:
            print(tpl_body.format(uid=key,name=value['name'],age=int(value['age']),tel=value['tel'],password=value['password']))

def main():
    users = load_data()
    login_ok = login(users)

    if not login_ok:
        print('登录失败')
        return
    while True: 
        operate = input('请输入操作(add/delete/update/find/list/exit):')
        if 'add' == operate:
            add_users(users)
        if 'delete' == operate:
            delete_users(users)
        if 'update' == operate:
            update_users(users)
        if 'find' == operate:
            find_users(users)
        if 'list' == operate:
            list_users(users)
        if 'exit' == operate:
            save_data(users)
            break
if __name__ =='__main__':
    main()