#enconding: utf-8
#write file

user = {
     1 : {'name':'kk','age':30, 'tel': '123xxxx'},
     2 : {'name':'kk1','age':30, 'tel': '123xxxx'},
     3 : {'name':'k2','age':30, 'tel': '123xxxx'},
}

path = 'user.data.txt'

fhandler = open(path,'wt')
for k,v in user.items():
    fhandler.write('{0},{1},{2},{3}\n'.format(k,v['name'],v['age'],v['tel']))
fhandler.close()

