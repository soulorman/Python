#enconding: utf-8
path = '12.py'

fhandler = open(path,'rt')

for line in fhandler:
    print(line)
fhandler.close()
