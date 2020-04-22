# encoding: utf-8


def bubble_sort(arr: list) -> list:
    """冒泡排序

    扔进去一个列表,返回排序好的列表
    :param arr: 需要排序的列表
    :return: 排序好的列表
    """
    count = 0
    list_long = len(arr)
    for i in range(list_long-1):
        for j in range(list_long - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            count += 1
    return arr,count


TEST_LIST = [1,2,3,4,5,6,0]
print(bubble_sort(TEST_LIST))
