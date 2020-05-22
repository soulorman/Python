class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None

def create_list(list_1):
    if len(list_1) < 1:
        return Node(None)

    head = Node(None)
    cur = head

    for i in list_1:
        cur.next = Node(i)
        cur = cur.next

    return head


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
    if node.next == None:
        return

    while node.next.next != None:
        node = node.next
    node.next = None

# 编号删
def index_del(node, index):
    if node.next == None:
        return

    i = 0
    while i < index - 1:
        node = node.next
        if node.next == None:
            print('meide')
            return
        i += 1
    node.next = node.next.next

# 值删
def value_dev(node, value):
    if node.next == None:
        return

    pre = node
    while pre.next.value != value:
        pre = pre.next
        if pre.next == None:
            print('GG')
            return
    pre.next = pre.next.next


# 改
# 索引改
def index_update(node, index, value):
    cur = node.next
    if cur == None:
        return

    i = 1
    while i < index:  
        cur = cur.next
        if cur == None:
            print('123')
            return
        i += 1
    cur.value = value

# 值改
def value_update(node, value1,value2):
    cur = node.next
    if cur == None:
        return

    while cur.value != value1:
        cur = cur.next
        if not cur:
            return

    cur.value = value2

# 查
def print_link(node):
    while node:
        print(node.value)
        node = node.next


# 反查(不改变原链表)
def print_back_link(node):
    if not node:
        return
    print_back_link(node.next)
    print(node.value)


# 反转链表
# 1.最简单的输出值
def reverse1(node):
    if not node:
        return

    revese(node.next)
    print(node.value)


# 2.反转
def reverse2(node):
    if not node or not node.next:
        return

    revlink = revese(node.next)
    node.next.next = node
    node.next = None
    return revlink


# 3. 转成列表，反转了再做成链表
def reverse3(node):
    if not node and not node.next:
        return  node
    l = []
    while node:
        if node.value != None:
            l.append(node.value)
        node = node.next
    l = l[::-1]
    head = Node(None)
    cur = head
    for i in l:    
        cur.next = Node(i)
        cur = cur.next

    return head

# 4. 非递归
def reverse4(node):
    cur = node
    pre = None
    while cur:
        #cur.next, pre, cur = pre, cur, cur.next
        temp = cur.next
        cur.next = pre # 当前链表指向新链表
        pre = cur  # 赋值给新链表
        cur = temp
    return pre


# 去重1
def remove_dup(node):
    if not node:
        return

    cur = node
    while cur.next:
        if cur.value == cur.next.value:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return node


# 去重2
def remove_dup(node):
    if node is None:
        return

    outCur = node
    while outCur:
        innerCur = outCur.next
        innerPre = outCur
        while innerCur:
            if outCur.value == innerCur.value:
                innerPre.next = innerCur.next
                innerCur = innerCur.next
            else:
                innerPre= innerCur
                innerCur = innerCur.next
        outCur = outCur.next
    return node

# 去重3
def deleteDuplicates(head):
        if not head:
            return None

        head_list = Node(0)     #头指针，不动
        cur_List = head_list        #当前指针

        cur_List.next = Node(head.val)    #指针移动
        cur_List = cur_List.next

        head = head.next      #head链表移动
        while head:           #遍历head链表
            if head.val != cur_List.val:
                cur_List.next =  Node(head.val)
                cur_List = cur_List.next
            head = head.next
        return head_list.next

# 排序

def sortList(node):
    if not node and not node.next:
        return

    l = []
    while node:
        if node.value != None:
            l.append(node.value)
        node = node.next

    l = sorted(l)

    head = Node(None)
    cur = head
    for i in l:    
        cur.next = Node(i)
        cur = cur.next

    return head


# 排序2       
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def partition(start, end):
            node = start.next.next
            pivotPrev = start.next
            pivotPrev.next = end
            pivotPost = pivotPrev
            while node != end:
                temp = node.next
                if node.val > pivotPrev.val:
                    node.next = pivotPost.next
                    pivotPost.next = node
                elif node.val < pivotPrev.val:
                    node.next = start.next
                    start.next = node
                else:
                    node.next = pivotPost.next
                    pivotPost.next = node
                    pivotPost = pivotPost.next
                node = temp
            return [pivotPrev, pivotPost]

        def quicksort(start, end):
            if start.next != end:
                prev, post = partition(start, end)
                quicksort(start, prev)
                quicksort(post, end)

        newHead = Node(0)
        newHead.next = head
        quicksort(newHead, None)
        return newHead.next


# 合并链表
def mergeTwoLists1(l1, l2):
    if not l1: return l2
    if not l2: return l1
    if l1.value <= l2.value:
        l1.next = mergeTwoLists(l1.next,l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1,l2.next)
        return l2

def mergeTwoLists2(l1, l2):
    if l1 and l2:
        if l1.val > l2.val: l1, l2 = l2, l1
        l1.next = mergeTwoLists(l1.next, l2)
    return l1 or l2


# 两数相加
def addTwoNumbers(l1, l2):
    start0 = Node(0)
    node = start0        
    carry = 0           #传递进位
    s = 0
    while(l1 or l2):
        val1 = l1.value if l1 else 0
        val2 = l2.value if l2 else 0
        # 对应位数字相加并加进位
        s = val1 + val2 + carry
        # 更新进位，整除10
        carry = s // 10
        value = s % 10
        node.next = Node(value)

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next


class Stack(object):
    def __init__(self, )





L1 = [1,3,4]
L2 = [1,2,3]
a = create_list(L1)
b = create_list(L2)
print_link(addTwoNumbers(a.next,b.next))
