# encoding: utf-8

def bubble_sort(arr: list) -> list:
    count = 0
    n = 0
    list_long = len(arr) - 1
    for i in range(list_long):
        last = 0
        flag = 0
        for j in range(list_long - i): 
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                flag = 1
                last = j
            count += 1
        list_long = last
        if not flag:
            break
        for x in range(last, n,-1):  
            if arr[x] < arr[x - 1]:
                arr[x-1], arr[x] = arr[x], arr[x-1]
        if not flag:
            break
        n += 1 
    return arr,count

TEST_LIST = [1,2,3,4,5,6,0]
print(bubble_sort(TEST_LIST))
