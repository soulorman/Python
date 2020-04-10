# encoding: utf-8


def key1(n):
    return n


def key2(n):
    return n[1]


def key3(n):
    return n['age']


def bubble_sort(arr: list, key: str) -> list:
    """冒泡排序

    扔进去一个列表/元组/字典,返回排序好的列表
    :param arr: 需要排序的列表
    :param key: 依据的排序关键字
    :return: 排序好的列表
    """
    list_long = len(arr)
    for i in range(list_long - 1):
        for j in range(list_long - 1 - i):
            if key(arr[j]) > key(arr[j + 1]):
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr


TEST_LIST = [1, 3, 2]
print(bubble_sort(TEST_LIST, key1))

TEST_TUL = [(1, 2), (5, 6), (0, 1)]
print(bubble_sort(TEST_TUL, key2))

TEST_DICT = [{'name': 'wangyuxi','age':12},{'name': 'wangyu','age':80},{'name': 'wangxi','age':2}]
print(bubble_sort(TEST_DICT, key3))
