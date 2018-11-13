#encoding: utf-8


users = {
     1:{'name' : 'kk', 'age' : 30, 'tel' : '152xxxxxx'}
     2:{'name' : 'kk', 'age' : 30, 'tel' : '152xxxxxx'}

}

while True:
    operate = input('please add/delete/update/find/list: ')
    if 'add' == operate:
        text = input('please user info: ')
        nodes = text.split(',')
        if len(nodes) != 3:
            print('error')
        else:
            if not nodes[1].isdigit():
                print('age error')
            else:
                users[max(users) + 1] = {'name': nodes[0],'age': nodes[1],'tel': nodes[2}
        print('add ok ')
    elif 'delete' == 'operate'
        
