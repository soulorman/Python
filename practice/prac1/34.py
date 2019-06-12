#encoding:utf-8

import mysort

l1 = [5,4,3]
l2 = [(1, 6), (2, 5), (3, 6)]
l3 = [{'age': 60}, {'age': 70}]

mysort.bubble(l1,key=mysort.DEFAULT_KEY)
print(l1)
