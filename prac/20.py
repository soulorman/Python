#encoding: utf-8

users = {
    1 : {'name':'kk','age':30,'tel':'1'},
    2 : {'name':'kk1','age':30,'tel':'2'},
    3 : {'name':'kk2','age':30,'tel':'3'},
}



for _ in range(3):
    txt = input('please input user,passwd(kk/1): ')
    username,password = txt.split('/')

    for k,user in users.items():
        isLogin =False
        if user['name'] == username and user['tel'] == password:
            isLogin =True
            break
    if isLogin:
        break
    else:
        print('error')

if isLogin:
    print('ok')
else:
    print('error 3')
