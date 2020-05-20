import random
a = []
for i in range(20):
    a.append(random.randint(1,200))


#1. 最好理解的递归
def quick_sort_1(l, low, hight):
    # 左边起始值 low 
    # 右边起始值 hight
    # 哨兵
    if low >= hight:
        return l
    key = l[low]
    left = low
    right = hight
    while left < right:
        while left < right and l[right] >= key:
            right -= 1
        l[left] = l[right]

        while left < right and l[left] >= key:
            left += 1
        l[right] = l[left]
    l[right] = key
    quick_sort_1(l, low, left-1)
    quick_sort_1(l, left+1, right)

    return l

quick_sort_1(a,0,len(a)-1)
print(a)

# 1. 选取一个基础值
# 2. 定义2个哨兵left,right
# 3. 先右边哨兵左移，找到比基础值小的，放在left里
# 4. 再左边哨兵右移，找到比基础值大的，放在right里
# 5. 直到哨兵相遇了，交换初始值和当前值
# 6. 重复递归左右两组的数组

