import random

def reversePairs(nums):
    size = len(nums)
    if size < 2:
        return 0
    res = 0
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if nums[i] > nums[j]:
                res += 1
    return res

lst = []
for _ in range(20):
    lst.append(random.randint(0,200))
print(lst)
print(reversePairs(lst))
