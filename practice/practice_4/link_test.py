class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None

#增加
# 头插
def head_add(node, value):
    ins = Node(value)
    ins.next = node.next
    node.next = ins

# 尾插
def tail_add(node, value):
    while node.next != None:
        node = node.next
    node.next = Node(value)

# 中间插
def mid_add(node, index, value):
    ins = Node(value)

    for _ in range(index - 1):
        node = node.next
        if node is None:
            print('meide')
            return

    ins.next = node.next
    node.next = ins

#删除:
# 头删
def head_del(node):
    if node.next == None:
        return 
    node.next = node.next.next

# 尾删
def tail_del(node):
    

# 编号删，值删

def create_list(list_1):
    if len(list_1) < 1:
        return Node(None)

    head = Node(None)
    cur = head

    for i in list_1:
        cur.next = Node(i)
        cur = cur.next

    return head

def print_link(node):
    while node:
        print(node.value)
        node = node.next

def print_back_link(node):
    if not node:
        return
    print_back_link(node.next)
    print(node.value)


L1 = [1,2,3]
L2 = []
a = create_list(L1)
head_del(a)
print_link(a)
