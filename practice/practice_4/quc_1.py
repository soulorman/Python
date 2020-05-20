a = [1,2,3,5,0,9]
def quick_sort_1(l, low, high):
    if low >= high:
        return
    # 哨兵
    key = l[low]
    left = low
    right = high

    while left < right:
        while left < right and l[right] >= key:
            right -= 1
        l[left] = l[right]
        while left < right and l[left] < key:
            left += 1
        l[right] = l[left]
    l[right] = key
    quick_sort_1(l, low, left-1)
    quick_sort_1(l, left+1,high)
    
    return l

quick_sort_1(a, 0, len(a)-1)
print(a)
