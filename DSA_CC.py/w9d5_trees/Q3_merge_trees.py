# mereing two trees (https://leetcode.com/problems/merge-two-binary-trees/description/)

class Node:
    def __init__ (self, x):
        self.data = x
        self.left = None
        self.right = None


root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.right = Node(6)
root1.left.left = Node(6)
root1.right.right = Node(7)
root1.right.left = Node(9)


root2 = Node(20)
root2.left = Node(10)
root2.right = Node(11)
root2.left.right = Node(12)
root2.right.right = Node(13)
root2.right.left = Node(17)

def inorder_traversing(root):
    if root == None:
        return
    inorder_traversing(root.left)
    print(root.data)
    inorder_traversing(root.right)
    


def merge_tree(root1,root2):
    if root1 == None:
        return root2
    
    if root2 == None:
        return root1
    
    root1.data = root1.data + root2.data
    
    merge_tree(root1.left,root2.left)
    merge_tree(root1.right,root2.right)
    
    return root1


m = merge_tree(root1,root2)
inorder_traversing(m)
 

