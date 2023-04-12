# preorder traversing
# rule = Root->Left->Right

class Node:
    def __init__ (self, x):
        self.data = x
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(6)
root.right.right = Node(7)
root.right.left = Node(9)


def preorder_traversingg(root):
    if root == None:
        return
    print(root.data)
    preorder_traversingg(root.left)
    preorder_traversingg(root.right)


preorder_traversingg(root)
    



