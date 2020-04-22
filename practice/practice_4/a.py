# encoding: utf-8

def bubble_sort(arr: list) -> list:
    count = 0
    list_long = len(arr) - 1
    for i in range(list_long):
        last = 0
        for j in range(list_long - i):      # 下标    0  >  1    每次不需要比最后一个 从0开始 所以-i-0
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                last = j
            count += 1

        list_long = last
    return arr,count


TEST_LIST = [1,2,5,7,4,3,6,8,9,10]
print(bubble_sort(TEST_LIST))
