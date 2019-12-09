# encoding:utf-8

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


def create_link(List):
    if len(List) < 2:
        return None
    else:
        head = Node(None)
        current = head

        List = set(List)
        for value in List:
            current.next = Node(value)
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

#def del_list(node):



list = [5,5,5,8]
head = create_link(list)
link_list(head)
