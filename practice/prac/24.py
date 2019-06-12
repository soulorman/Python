#encoding: utf-8
def key(n):
    return n
def key2(n):
    return n[1]
def key3(n):
    return n['age']

def bubble(l,key):
    length = len(l)
    for j in range(length - 1):
        for i in range(length -1):
            if key(l[i]) > key(l[i+1]):
                l[i+1],l[i] = l[i],l[i+1]
l1 = [5,4,3]

bubble(l1,key)
print(l1)

def cmp2(n1,n2):
    return n1[1] > n2[1]

l2 = [(1,6),(2,5),(3,6)]

bubble(l2,key2)
print(l2)



