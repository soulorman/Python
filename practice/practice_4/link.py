# encoding: utf-8

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def creat_link(s: list):
    head = Node(None)
    cur = head
     
    for i in s:
        cur.next = Node(i)
        cur = cur.next

    return head

def add(node,value):
    ins = Node(value)
    ins.next = node.next
    node.next = ins
    
    
def list_link(head):
    
    while head:
        print(head.value)
        head = head.next

l = [1,2,3,4,5]
a = creat_link(l)
list_link(a)
add(a, 2)
list_link(a)
add(a, 11)
list_link(a)
