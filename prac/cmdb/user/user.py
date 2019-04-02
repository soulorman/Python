#encoding: utf-8

import json

DATA_FILE = 'user.data.txt'
DISPLAY_TPL = '|{uid:10d}|{password:20s}|{name:10s}|{age:5d}|{tel:20s}|'

def load_data():
    '''
        读取数据文件并反序列化为dict
    '''
    f = open(DATA_FILE, 'rt')
    cxt = f.read()
    f.close()

    users = json.loads(cxt)
    return {int(key):value for key, value in users.items()}


def save_data(users):
    '''
        序列化users为字符串，并存储到文件        
    '''
    f = open(DATA_FILE, 'wt')
    f.write(json.dumps(users))
    f.close()
    return True


def login():
    users = load_data()
    is_login = False
    for _ in range(3):
        text = input('请输入用户名和密码(name/password):')
        name, password = text.split('/')
        for uid, user in users.items():
            if user['name'] == name and user['password'] == password:
                is_login = True
                break

        if is_login:
            break

    return is_login


def input_add_user():
    is_valid = False
    user = {}
    text = input('请输入用户信息(name,age,tel,passowrd):')
    nodes = text.split(',')
    if len(nodes) != 4:
        print('输入信息有误, 请重新进行操作')
    else:
        if not nodes[1].isdigit():
            print('输入年龄有误，请重新进行操作')
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
    is_valid, user = input_add_user()
    if is_valid:
        users = load_data()
        uid = 1
        if users:
            uid = max(users) + 1

        users[uid] = user
        save_data(users)
        print('添加用户成功')


def input_delete_user():
    is_valid = False
    uid = input('请输入删除用户ID:')
    if not uid.isdigit():
        print('输入信息有误')
    else:
        is_valid = True
        uid = int(uid)
    
    return is_valid, uid


def delete_user():
    is_valid, uid = input_delete_user()
    if is_valid:
        users = load_data()
        users.pop(int(uid), None)
        save_data(users)
        print('删除成功')


def input_update_user():
    users = load_data()
    is_valid, user = False, {}
    uid = input('请输入编辑用户ID:')
    if not uid.isdigit() or int(uid) not in users:
        print('输入信息有误')
    else:
        text = input('请输入用户信息(示例:age,tel,password):')
        nodes = text.split(',')
        if len(nodes) != 3:
            print('输入信息有误, 请重新进行操作')
        else:
            if not nodes[0].isdigit():
                print('输入年龄有误，请重新进行操作')
            else:
                is_valid = True
                uid = int(uid)
                user = {
                    'age' : int(nodes[0]),
                    'tel' : nodes[1],
                    'password' : nodes[2]
                }

    return is_valid, uid, user


def update_user():
    is_valid, uid, user = input_update_user()
    if is_valid:
        users = load_data()
        users[uid].update(user)
        save_data(users)
        print('更改成功')


def list_user():
    users = load_data()
    for key, value in users.items():
        print(DISPLAY_TPL.format(uid=key, name=value['name'], age=value['age'], tel=value['tel'], password=len(value['password']) * '*'))


def find_user():
    users = load_data()
    text = input('请输入查询的字符串:')
    for key, value in users.items():
        if text in value['name']: #if value['name'].find(text) != -1:
            print(DISPLAY_TPL.format(uid=key, name=value['name'], age=value['age'], tel=value['tel'], password=len(value['password']) * '*'))

def main():
    '''
        程序的入口，用于流程的串接和控制
    '''
    login_ok = login()

    if not login_ok:
        print('登陆失败')
        return

    actions = {
        'add' : add_user,
        'delete' : delete_user,
        'update': update_user,
        'list' : list_user,
        'find' : find_user,
    }
    while True:
        operate = input('请输入操作(add/delete/update/find/list/exit):')
        if operate == 'exit':
            break
        func = actions.get(operate)
        if func:
            func()
        else:
            print('输入操作有误')
        

if __name__ == '__main__':
    main()