import random
arr = []
for i in range(20):
    arr.append(random.randint(0,100))

def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap:
                if alist[j] < alist[j - gap]:
                    alist[j], alist[j - gap] = alist[j - gap], alist[j]
                    j -= gap
                else:
                    break
        gap //= 2

print('排序前:',arr)
shell_sort(arr)
print('排序前:',arr)
