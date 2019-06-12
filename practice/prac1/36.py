#encoding:utf-8

from mysort.mysort import bubble as sort
from mysort.mysort import DEFAULT_KEY

l1 = [5,4,3]
l2 = [(1, 6), (2, 5), (3, 6)]
l3 = [{'age': 60}, {'age': 70}]

sort(l1,key=DEFAULT_KEY)
print(l1)