# encoding:utf-8

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


def create_link(Lists):
    if len(Lists) < 2:
        return None
    else:
        head = Node(None)
        current = head

        New_Lists = list(set(Lists))
        New_Lists.sort(key=Lists.index)
        for value in New_Lists:
            current.next = Node(value)
            current = current.next

    return head


def del_list(head, node):
    try:
        current = head.next        

        while current != None:
            if current.value == node:
                current.value = current.next.value
                current.next = current.next.next
                break

            current = current.next

    except Exception as e:
        pass


    try:
        current = head.next      
        while current != None:
            print(current.value)
            current = current.next

    except Exception as e:
        pass


node = 5
list_1 = [5,8,1,3,3,6]
head = create_link(list_1)
del_list(head, node)
