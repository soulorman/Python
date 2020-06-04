import random

def merge(left, right):
    merge_list = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merge_list.append(left[i])
            i += 1
        else:
            merge_list.append(right[j])
            j += 1

    while i < len(left):
            merge_list.append(left[i])
            i += 1
    while j < len(right):
            merge_list.append(right[j])
            j += 1
    return merge_list


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    merge(lst[:mid], lst[mid:])

lst = []
for _ in range(20):
    lst.append(random.randint(0,200))

print(merge_sort(lst))
print(lst)
