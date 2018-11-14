#enconding: utf-8
#readfile

path = 'user.data.txt'

fhandler = open(path,'rt')

for line in fhandler:
    print(line)

fhandler.close()
