def QuickSort_No_Stack(nums:list,left:int,right:int) -> list:
    temp = [left,right]
    
    while temp:
        j = temp.pop()  # j = right
        i = temp.pop()  # i = left
        
        index = getIndex(nums,i,j)
        
        if i < index-1:   # 压入堆栈 注意左右边界的顺序
            temp.append(i)
            temp.append(index-1)
        
        if j > index+1:
            temp.append(index+1)
            temp.append(j)
        
    return nums

a = [3,2,1]
QuickSort_No_Stack(a,0,len(a)-1)

print(a)

