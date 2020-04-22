# 插入排序  时间复杂度 O(n^2) 空间复杂度O(1) 稳定

def insertion_sort(collection):
    # 插入排序
    length = len(collection)- 1
    for i in range(1, length):    # 第一个数作为初始有序序列，所以不用比较
        j = i - 1
        while j >= 0 and collection[j + 1] < collection[j]:
            collection[j], collection[j + 1] = collection[j + 1], collection[j]
            j -= 1
    return collection
# [3,1,2,4,5,6]
l = [3,1,2,4,5,0]

print(insertion_sort(l))
