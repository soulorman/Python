import random

def qc1(lst):
    if len(lst) <= 1:
        return lst
    else:
        key = lst[0]
        left = [ e for e in lst[1:] if e <= key ]
        right = [ e for e in lst[1:] if e > key ]
        return qc1(left) + [key] + qc1(right)

a = []
for _ in range(20):
    a.append(random.randint(0,200))
print(qc1(a))
