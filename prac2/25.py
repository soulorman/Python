#encoding: utf-8


users = {
    1 : {'name':'kk', 'age':29, 'tel':'136'},
    2 : {'name':'wd', 'age':12, 'tel':'1362xxxxxxxx'},
    3 : {'name':'woniu', 'age':34, 'tel':'133xxxxxxxx'}
}
isLogin = False


for _ in range(3):
    txt = input('请输入用户名和密码(users/passwd):')
    username,password = txt.split('/')

    for k,user in users.items():
        if user['name'] == username and user['tel'] == password:
            isLogin =True
            break

    if isLogin:
        break
        
if isLogin:
    print('登录成功')
else:
    print('登录失败')
