def b_s(li, va):
    low = 0
    high = len(li)
    
    while low <= high:
        mid = (low + high) // 2
        if li[mid] == va:
            return mid
        elif va > li[mid]:
            low = mid + 1
        else:
            high = mid - 1
    
l = [1,2,3,4,5,6,7,8,9]
print(b_s(l,9))
