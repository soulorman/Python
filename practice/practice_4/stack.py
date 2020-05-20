#链表实现栈

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# 栈
class Stack:
    def __init__(self):
        self.head = None
        self.len = 0

    def is_empty(self):
        return not self.len

    # 入栈
    def push(self, value):

        node = Node(value)
        node.next = self.head
        self.head = node
        self.len += 1

    # 出栈    
    def pop(self):
        cur = self.head

        if self.head:
            self.head = self.head.next
            self.len -= 1
        return cur

    def __iter__(self):
        self.cur = self.head

        return self

    def __next__(self):
        if not self.cur:
            raise StopIteration
        try:
            temp = self.cur
            self.cur = self.cur.next
            return temp
        except AttributeError as e:
            raise StopIteration

if __name__ == '__main__':
    stack = Stack()
    print(f"is empty? {stack.is_empty()}")
    print('push')
    stack.push('a')
    stack.push('b')
    stack.push('c')
    stack.push('d')
    
    for i in stack:
        print(i.value)

    print(stack.pop().value)
