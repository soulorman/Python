# 构建基本的二叉树
class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild
        
    def __str__(self):
        return str(self.elem)

A, B, C = [Node(i) for i in 'ABC']
A.lchild, A.rchild = B, C

print(A.rchild)
