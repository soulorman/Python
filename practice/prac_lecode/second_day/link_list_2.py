# encoding:utf-8
# error use list index!!!
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def create_link(List):

    if len(List) < 3:
        return False
    else:
        for index,_ in enumerate(List):
            current = Node(List[index])
            current.next = Node(List[index+1])
            current = current.next

    return current


def link_list(head):
    current = head

    while current != None:
        print(current.value)
        current = current.next


list = [5,8,1,2]
head = create_link(list)
link_list(head)
