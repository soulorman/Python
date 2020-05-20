import random

a = []
for i in range(20):
    a.append(random.randint(1,200))

def select(l):
    max = len(l)
    for i in range(max - 1):
        min_index = i
        for j in range(i+1, max):
            if l[j] < l[min_index]:
                min_index = j

        l[min_index], l[i] = l[i], l[min_index]
    return l

select(a)
print(a)
