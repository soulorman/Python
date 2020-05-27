def select2(lst):
    n = len(lst)
    for i in range(n - 1):
        min = i
        max = n - 1
        
        for j in range(i+1,n):
            if lst[j] < lst[min]:
                min = j
            if lst[j] > lst[max]:
                max = j
        lst[min],lst[i] = lst[i],lst[min]
        lst[max],lst[n-1] = lst[n-1],lst[max]

a = [3,2,1]
select2(a)
print(a)
