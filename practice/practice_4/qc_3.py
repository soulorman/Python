class Stack():
    """简单实现一个栈，本质就是个list"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


# 此方法与上面例子一样，保持不变
def partition(mylist, start, end):
    # 若选其他元素作为pivot，下面的while内容需要相应更改
    pivot = mylist[end]
    left = start
    right = end

    while left < right:
        while left < right and mylist[left] <= pivot:
            left += 1
        while left < right and mylist[right] >= pivot:
            right -= 1
        if left != right:
            mylist[left], mylist[right] = mylist[right], mylist[left]

    mylist[end], mylist[left] = mylist[left], pivot
    return left


def quick_sort(mylist):
    stack = Stack()
    start = 0
    end = len(mylist) - 1

    if start < end:
        stack.push((start, end))
        while not stack.is_empty():
            start, end = stack.pop()
            mid = partition(mylist, start, end)
            if start < mid - 1:
                stack.push((start, mid - 1))
            if mid + 1 < end:
                stack.push((mid + 1, end))


a= [3,2,1]
quick_sort(a)
print(a)
