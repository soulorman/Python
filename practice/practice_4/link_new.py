#encoding: utf-8

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def create_link(s):
    if len(s) < 1:
        return Node(None)

    head = Node(None)
    cur = head

    for i in s:
        cur.next = Node(i)
        cur = cur.next

    return head

# 增
#头插法
def add_head(node, value):
    ins = Node(value)
    ins.next = node.next
    node.next = ins

#尾插法
def add_tail(node, value):
    ins = Node(value)
    while node.next != None:
        node = node.next

    node.next = ins
    
#插入中间
#按索引插入
def add_index(node, index, value):
    ins = Node(value)
    if index == 0:
        ins.next = node.next
        node.next = ins

    else:
        i = 0
        while i < index:
            node = node.next
            if node is None:
                print('index not')
                return
            i += 1

        ins.next = node.next
        node.next = ins

# 删
# 删头元素
def remove_from_first(node):
    node = node.next
    if node == None:
        print("链表为空，没有元素可以删除！")
        return
    node = node.next
    
    return node

# 删尾元素
def remove_from_last(node):
    node = node.next
    if node == None:
        print("链表为空，没有元素可以删除！")
        return
    
    while(node.next.next != None):
        node = node.next
    
    node.next = None
    

# 删除索引元素
def remove_index(node, index):
    node = node.next
    if node == None:
        print("链表为空，没有元素可以删除！")
        return

    if index == 0:
        node = node.next
    else:
        i = 0
        while i < index-1:
            node = node.next
            if node == None:
                print('index out')
                return
            i += 1

        node.next = node.next.next

# 删除元素
def remove_value(node, value):
    if node == None:
        print("链表为空，没有元素可以删除！")
        return
    
    pre = node
    while node.next != None:
        if pre.next.value == value:
            break
        pre = pre.next
        if pre.next == None:
            print("链表找不到要删除的元素")
            return
        
    pre.next = pre.next.next

# 改
#索引改
def update(node,index,value):
    node = node.next
    if node == None:
        print("链表为空！")
        return

    i = 0
    while i < index:
        node = node.next
        if node == None:
            print('index out')
            return 
        i += 1

    node.value = value

# 元素改
def update(node, value_1, value_2):
    if node == None:
        print("链表为空！")
        return
    
    node = node.next
    while node != None:
        if node.value == value_1:
            node.value = value_2
            break
        node = node.next

# 正查
def print_link(node):
    while node:
        print(node.value)
        node = node.next
# 反查（不改变原链表）
def print_back_link(node):
    if node is None:
        return
    print_back_link(node.next)
    print(node.value)

# 其他操作
# 链表反转
def reverse(node):
    if node == None:
        print("链表为空")
        return

    cur = node
    while(cur != None):
        add_head(cur.val)
        cur = cur.next

    return cur


# 反转
def reverse1(node):
    if node == None:
        print("链表为空")
        return

    last = None 
    while node:
        tmp = node.next
        node.next = last
        last = node
        node = tmp
    return last

# 反转
def reverse2(node):
    if not node or not node.next:
        return node
    else:
        newHead = Node(node.next)
        node.next.next=node
        node.next=None
        return newHead



s = [1,2,3]
a = create_link(s)
reverse2(a)
print_link(a)
