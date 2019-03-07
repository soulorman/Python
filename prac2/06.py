#encoding:utf-8

m = 1
while m <= 9:
    i = 1
    while i<=m:
        print(i,'*',m,'=',i*m,\
            end="\t")
        i +=1
    print()
    m +=1