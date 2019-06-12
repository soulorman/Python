#encoding: utf-8

src = '/tmp/a.txt'
dest = '/tmp/b.txt'
SIZE = 1024 * 1024

f1 = open(src,'rb')
f2 = open(dest,'wb')

while True:
    btxt = f1.read(SIZE)
    if b'' == btxt:
        break
    f2.write(btxt)

f1.close()
f2.close()
