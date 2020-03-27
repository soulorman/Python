# 构建基本的二叉树
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None

# list_1 = [1,2,3]
# list_2 = [1,2,3]

# A, B, C = [ Node(i) for i in list_1 ]
# A.lchild, A.rchild = B, C

# D, E, F = [ Node(i) for i in list_2 ]
# D.lchild, D.rchild = E, F

class Tree:
    def __init__(self):
        self.root = None

    def add(self, elem):
        node = Node(elem)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)          
                if pop_node.lchild is None:
                    pop_node.lchild = node         
                    return
                elif pop_node.rchild is None:
                    pop_node.rchild = node      
                    return
                else:
                    q.append(pop_node.lchild)     
                    q.append(pop_node.rchild)

    def traverse(self):
        if self.root is None:
            return None

        q = [self.root]
        res = [self.root.elem]

        while q != []:
            pop_node = q.pop(0)
            if pop_node.lchild is not None:
                q.append(pop_node.lchild)
                res.append(pop_node.lchild.elem)

            if pop_node.rchild is not None:
                q.append(pop_node.rchild)
                res.append(pop_node.rchild.elem)

        return res


    def preorder(self, root):
        if root is None:
            return []

        result = [root.elem]
        left_elem = self.preorder(root.lchild)
        right_elem = self.preorder(root.rchild)     

        return result + left_elem + right_elem

    def inorder(self, root):
        if root is None:
            return []

        result = [root.elem]
        left_elem = self.inorder(root.lchild)
        right_elem = self.inorder(root.rchild)     

        return left_elem + result + right_elem

    def postorder(self, root):
        if root is None:
            return []

        result = [root.elem]
        left_elem = self.postorder(root.lchild)
        right_elem = self.postorder(root.rchild)     

        return left_elem + right_elem + result

tree = Tree()
for i in range(10):
    tree.add(i)

print(tree.traverse())
print(tree.preorder(tree.root))
print(tree.inorder(tree.root))
print(tree.postorder(tree.root))
