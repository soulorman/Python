import random
print("归并排序")
lst = []
for _ in range(20):
    lst.append(random.randint(0,200))

#合并两列表
def merge(a,b):#a,b是待合并的两个列表,两个列表分别都是有序的，合并后才会有序
    merged = []
    i,j=0,0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            merged.append(a[i])
            i+=1
        else:
            merged.append(b[j])
            j+=1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged
#递归操作
def merge_sort(c):
    if len(c)<=1:
        return c
    mid = len(c)//2#除法取整
    a = merge_sort(c[:mid])
    b = merge_sort(c[mid:])
    return merge(a,b)
print(merge_sort(lst))
