# encoding: utf-8

import json

DATA_FILE = 'user.data.txt'
tpl_title = '|{0:^10s}|{1:^10s}|{2:^10s}|{3:^5s}|{4:^15s}|'
colums_title = ('ID', 'Name', 'password', 'Age', 'Tel')
tpl_body = '|{uid:^10d}|{name:^10s}|{password:^10s}|{age:^5d}|{tel:^15s}|'

title = tpl_title.format(colums_title[0],colums_title[1],colums_title[2],colums_title[3],colums_title[4])
splitline = '-' * len(title)

def load_data():
    f = open(DATA_FILE, 'rt')
    cxt = f.read()
    f.close()

    users = json.loads(cxt)
    return {int(key):value for key, value in users.items()}

def save_data(users):
    f = open(DATA_FILE, 'wt')
    f.write(json.dumps(users))
    f.close()


def login():
    users = load_data()
    isLogin = False
    for _ in range(3):
        txt = input('请输入用户名和密码(user/passwd):')
        username, password  = txt.split('/')

        for k, user in users.items():
            if user['name'] == username and user['password'] == password:
                isLogin = True
                break

        if isLogin:
            break
        else:
            print('用户名或者密码错误!!!')

    return isLogin

def valid_user():
    is_valid = False
    user = {}
    text = input('请输入用户信息(name,age,tel,password):')
    nodes = text.split(',')
    if len(nodes) != 4:
        print('输入信息有误，请重新操作')
    else:
        if not nodes[1].isdigit():
            print('输入年龄有误，请重新操作')
        else:
            user = {
                        'name' : nodes[0],
                        'age' : int(nodes[1]),
                        'tel' : nodes[2],
                        'password' : nodes[3]
                    }
            is_valid = True

    return is_valid, user

def add_user():
    is_valid, user = valid_user()
    if is_valid:
        users = load_data()
        uid = 1
        if users:
            uid = max(users) + 1

        users[uid] = user
        save_data(users)
        print('添加用户成功!')

def input_del():
    is_valid = False 
    uid = input('请输入删除的用户ID:')
    if not uid.isdigit():
        print('信息有误')
    else:
        is_valid = True
        uid = int(uid)

    return is_valid, uid


def del_user():
    is_valid, uid = input_del()
    if is_valid:
        users = load_data()
        users.pop(int(uid), None)
        save_data(users)
        print('删除成功')

def valid_update():
    users = load_data()
    is_valid = False
    user = {}
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
                is_valid = True
                uid = int(uid)
                user = {
                        'age' : int(nodes[0]),
                        'tel' : nodes[1],
                }

    return is_valid, uid, user


def update_user():
    is_valid, uid, user = valid_update()
    if is_valid:
        users = load_data() 
        users[uid].update(user)
        save_data(users)
        print('更新用户成功!')


def list_user():
    users = load_data()
    print(splitline)
    print(title)
    print(splitline)
    for k,v in users.items():
        print(tpl_body.format(uid=k,name=v['name'],age=v['age'],tel=v['tel'],password=len(v['password']) * '*'))
    print(splitline)


def find_user():
    users = load_data()
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
            print(tpl_body.format(uid=k,name=v['name'], age=v['age'],tel=v['tel'],password=len(v['password']) * '*'))

    if not exist:
        print('没有找到')

def changepass_user():
    users = load_data()
    change_state = False
    old_pass = False
    for _ in range(3):
        token = input('请再次验证你的信息,输入用户名/密码:')
        nodes = token.split('/')
        username = nodes[0]
        passwd = nodes[1]
        for _,user in users.items():
            if username == user['name'] and passwd == user['password']:
                old_pass = True
                break
        else:
            print('验证未通过，请再试')

        if old_pass:
            break
    if old_pass:
        for _ in range(3):
            passwd_new = input('请输入新密码:')
            passwd_new1 = input('再次输入密码:')
            if passwd_new == passwd_new1:
                user['password'] = passwd_new
                save_data(users)
                change_state = True
                print('密码修改成功')
                break
            else:
                print('密码不一致,请重新输入')

        if not change_state:
            print('信息验证失败,请重试')


def main():
    login_ok = login()
    actions = {
        'add' : add_user,
        'del' : del_user,
        'update' : update_user,
        'list' : list_user,
        'find' : find_user,
        'changepass' : changepass_user,
        'exit' : save_data,
    }

    if not login_ok:
        print('登录超时')
        return False

    while True:
        operate = input('请输入操作(add/del/update/list/find/changepass/exit):')
        if operate == 'exit':
            print('bye')
            break
        func = actions.get(operate)
        if func:
            func()
        else:
            print('输入参数有误') 

if __name__ == '__main__':
    main()