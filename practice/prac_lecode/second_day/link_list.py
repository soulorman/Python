# encoding:utf-8

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value


def create_link(List):
    head = Node(None)
    current = head

    if len(List) < 3:
        return False

    for value in List:
        node = Node(value)
        current.set_next(node)
        current = node

    return head


def link_list(head):
    current = head.get_next()

    while current is not None:
        print(current.get_value())
        current = current.get_next()


list = [5,8,1,2]
head = create_link(list)
link_list(head)
