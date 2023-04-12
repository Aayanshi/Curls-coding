# question 2.
# Write postorder and inorder traversal function for the tree given
# below, including declaring classes, providing input, and perform the dry run also

class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None 

root = Node(3)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(5)
root.left.right = Node(4)
root.right.right = Node(7)





def preorder(root):
    if root == None:
        return 
    print(root.data)
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    if root == None:
        return 
    inorder(root.left)
    print(root.data)
    inorder(root.right)


def postorder(root):
    if root == None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.data)


preorder(root)
print("=============")
inorder(root)
print("==============")
postorder(root)







