# encoding: utf-8

path = 'panduan.py'
SIZE = 3
fhandler = open(path, 'rt')

while True:
    txt = fhandler.read(SIZE)
    if '' == txt:
        break
    print(txt)
fhandler.close()
