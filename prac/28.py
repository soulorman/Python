#encoding: utf-8

from mysort import bubble,DEFAULT_KEY

l1 = [5,4,3]
l2 = [(1,6),(2,5),(3,6)]
l3 = [{'age' : 60},{'age' : 70},{'age' : 50},]


bubble(l1,key=DEFAULT_KEY)
print(l1)
bubble(l2,key=lambda x : x[1])
print(l2)
bubble(l3,key=lambda x : x['age'])
print(l3)
