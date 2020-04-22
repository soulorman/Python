def insert_sort_extend(l):
    for i in range(1,len(l)):
        if l[i] < l[i - 1]:
            num = l[i]
            index = i
            left = 0 
            right = i - 1
           
            # left 相交
            while left <= right:
                mid = (left + right) //2
                if num < l[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            for j in range(i-1,left -1, -1):
                l[j+1] = l[j]

            l[left] = num

    return l
l = [1,3,5,6,7,8,4]
print(insert_sort_extend(l))
