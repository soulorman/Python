#encoding: utf-8

src = '/tmp/a.txt'
dest = '/tmp/b.txt'

f1 = open(src,'rt')
f2 = open(dest,'wt')

for line in f1:
    f2.write(line)

f1.close()
f2.close()


