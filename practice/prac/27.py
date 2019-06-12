#encoding: utf-8

import mysort

l1 = [5,4,3]
l2 = [(1,6),(2,5),(3,6)]
l3 = [{'age' : 60},{'age' : 70},{'age' : 50},]


mysort.bubble(l1,key=mysort.DEFAULT_KEY)
print(l1)
mysort.bubble(l2,key=lambda x : x[1])
print(l2)
mysort.bubble(l3,key=lambda x : x['age'])
print(l3)
