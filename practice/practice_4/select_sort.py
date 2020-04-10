# encoding: utf-8


def selection_sort(arr):
    """选择排序

    :param arr:需要排序的列表
    :return: 排序完成的列表
    """
    length = len(arr)
    for i in range(length - 1):
        minIndex = i
        for j in range(i + 1, length):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr


lis = [1, 5, 2, 0, 3]
print(selection_sort(lis))
