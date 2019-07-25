# encoding: utf-8

users = {
    1 : {'name' : 'kk', 'age' : 30, 'tel' : '152xxxx'},
    2 : {'name' : 'wd', 'age' : 23, 'tel' : '151xxxx'},
    3 : {'name' : 'wd', 'age' : 20, 'tel' : '136xxxx'},
}

path = 'user.data.txt'

fhandler = open(path, 'wt')
for k,v in users.items():
    fhandler.write('{0},{1},{2},{3}\n'.format(k,v['name'],v['age'],v['tel']))
    
fhandler.close()
