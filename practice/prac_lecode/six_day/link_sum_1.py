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
    current = head
    text = 0 
    try:
        current_1 = l1.next
        current_2 = l2.next
        while current_1 != None or current_2 != None:
            x = current_1.value if current_1 else 0
            y = current_2.value if current_2 else 0
            a = x + y
            if a // 10 == 0:
                if text != 0:
                    a += text
                    current.next = ListNode(a)
                    current = current.next
                else:
                    current.next = ListNode(a)
                    current = current.next
                text = 0
            else:
                if text == 0:
                    b = a % 10 + text
                    current.next = ListNode(b)
                    current = current.next
                    text = 1

            current_1 = current_1.next
            current_2 = current_2.next

    except Exception as e:
        pass
    return head

list_1 = [2,4]
list_2 = [5,6,4]

print(link_list(add(create(list_1),create(list_2))))
