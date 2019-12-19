# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

class LinkNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def create(s):
    head = LinkNode(None)
    current = head

    for i in s:
        current.next = LinkNode(i)
        current = current.next

    return head.next


def list(head):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next
# 核心思想：
# 递归处理

def link(l1,l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = link(l1.next, l2)
        return l1
    else:
        l2.next = link(l1, l2.next)
        return l2

s1 = '124'
s2 = '134' 
list(link(create(s1),create(s2)))
