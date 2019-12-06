# encoding:utf-8

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def create_link(List):

    if len(List) < 3:
        return False
    else:
        head = Node(None)
        current = head

        for value in List:
            current.next = Node(value)
            current = current.next

    return head


def link_list(head):
    current = head

    while current != None:
        print(current.value)
        current = current.next


list = [5,8,1,2]
head = create_link(list)
link_list(head)
