# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def create(list):
    head = ListNode(None)
    current = head

    for i in list:
        val = ListNode(i)
        current.next = val
        current = current.next

    return head

def link_list(head):
    try:
        current = head.next
        while current != None:
            print(current.value)
            current = current.next

    except Exception as e:
        pass

def add(l1,l2):
    head = ListNode(None)
    cur = head
    
    # 方便计数的临时变量
    carry = 0
  
    cur_1 = l1.next
    cur_2 = l2.next

    while (cur_1 or cur_2):
        x = cur_1.value if cur_1 else 0
        y = cur_2.value if cur_2 else 0
        s = x + y + carry
        carry = s // 10   
        cur.next = ListNode(s % 10)
        cur = cur.next
        
        # 处理长短不一
        if (cur_1 !=None): cur_1 = cur_1.next
        if (cur_2 !=None): cur_2 = cur_2.next

        # 处理多一位
        if (carry > 0):
            cur.next = ListNode(1)

    return head

list_1 = [2,4,1,3]
list_2 = [5,6,4]

print(link_list(add(create(list_1),create(list_2))))
