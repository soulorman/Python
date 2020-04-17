# encoding: utf-8

def shellSort(arr: list) -> list:
    n = len(arr)
    gap = int(n/2) # gap间隔
    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap = int(gap/2)
    return arr

arr = [ 12, 34, 54, 2, 3]
print (shellSort(arr)) 
