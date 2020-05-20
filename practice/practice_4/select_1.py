import random

a = []
for i in range(20):
    a.append(random.randint(1,200))

def select_1(l):
    length = len(l)
    for i in range(length - 1):
        min = i
        max = length - 1
        for j in range(i+1,length):
            if l[j] < l[min]:
                min = j
            if l[j] > l[max]:
                max = j
        l[min], l[i] = l[i], l[min]
        l[max], l[length-1] = l[length-1], l[max]


select_1(a)
print(a)
