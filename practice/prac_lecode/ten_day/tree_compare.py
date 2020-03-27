# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

# 示例 1:
# 输入:       1         1
#           / \       / \
#          2   3     2   3
#         [1,2,3],   [1,2,3]
# 输出: true

# 示例 2:
# 输入:      1          1
#           /           \
#          2             2
#         [1,2],     [1,null,2]
# 输出: false

# 示例 3:
# 输入:       1         1
#           / \       / \
#          2   1     1   2
#         [1,2,1],   [1,1,2]
# 输出: false
        
# encoding: utf-8

# 构建基本的二叉树
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None

# 创建树，查看树
class Tree:
    def __init__(self):
        self.root = None

    # 层次遍历
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

    # 先序遍历
    def preorder(self, root):
        if root is None:
            return []

        result = [root.elem]
        left_elem = self.(root.lchild)
        right_elem = self.preorder(root.rchild)     

        return result + left_elem + right_elem

tree = Tree()
list_1= [1,2,1]
for i in list_1:
    tree.add(i)

tree1 = Tree()
list_2 = [1,1,2]
for j in list_2:
    tree1.add(j)

def compare(tree1,tree2):
    result = True
    if tree1.preorder(tree1.root) != tree2.preorder(tree2.root):
        result = False
    
    return result

print(compare(tree,tree1))

# 核心思想，简单的构建二叉树，并遍历元素进行比较
