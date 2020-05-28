import random
def qc(lst, low, high):
    if low <= high:
        left = partition(lst, low, high)
        qc(lst, low, left - 1)
        qc(lst, left + 1, high)

def partition(lst, low, high):
    key = lst[low]
    left = low
    right = high
    while left < right:
        while left < right and lst[right] >= key:
            right -= 1
        lst[left] = lst[right]
        while left < right and lst[left] <= key:
            left += 1
        lst[right] = lst[left]
    lst[right] = key
    return right

a = []
for _ in range(20):
    a.append(random.randint(0,200))
qc(a,0,len(a) - 1)
print(a)
