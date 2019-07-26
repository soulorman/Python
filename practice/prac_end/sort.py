# encoding:utf-8

# 列表
def key(n):
    return n

# 元组
def key2(n):
    return  n[1]

# 字典
def key3(n):
    return  n['age']

def buble(l, key):
    length = len(l)
    for j in range(length-1):
        for i in range(length-1):
            if key(l[i]) > key(l[i+1]):
                l[i+1],l[i] = l[i],l[i+1]

l1 = [6,1,2,10]
buble(l1,key)
print(l1)

l2 = [(1,2),(2,3),(8,8),(1,1)]
buble(l2,key2)
print(l2)

l3 = [{'name':'kk','age':12},{'name':'wd','age':29}]
buble(l3,key3)
print(l3)
