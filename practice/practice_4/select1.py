a = [3,1,2]

def select1(lst):
    n = len(lst)
    for i in range(n - 1):
        min = i
        for j in range(i+1,n):
            if lst[j] < lst[min]:
                min = j  
        lst[min],lst[i] = lst[i],lst[min]

select1(a)
print(a)
