import random
def qc(lst, low, high):
    if low < high:
        stack = [low,high]
        while stack:
            right = stack.pop()
            left = stack.pop()

            mid = partition(lst, left, right)
            if left < mid - 1:
                stack.append(left)
                stack.append(mid-1)
            if right > mid + 1:
                stack.append(mid+1)
                stack.append(right) 

def partition(lst, low, high):
    i = low - 1 
    for j in range(low, high):
        if lst[j] <= lst[high]:
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[high],lst[i+1] = lst[i+1],lst[high]
    return i + 1


a = []
for _ in range(20):
    a.append(random.randint(0,200))
qc(a,0,len(a) - 1)
print(a)

