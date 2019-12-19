# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

class LinkNode:
    def __init__(self, value):
        self.value = value
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
        print(cur.value)
        cur = cur.next
# 核心思想
# 迭代法： 先确定一个新链表的头，然后分别比较链表的值，谁小就指向谁，最后记得返回的时候跳过第一个
def link(head1,head2):
    a = head1
    b = head2

    head = LinkNode(None)
    cur = head

    while a and b:
        if  a.value < b.value:
            cur.next = a
            a = a.next
        else:
            cur.next = b
            b = b.next

        cur = cur.next
    # 如果后面还有的，直接接最后
    cur.next = a if a else b

    return head.next

s1 = '124'
s2 = '134' 
list(link(create(s1),create(s2)))
