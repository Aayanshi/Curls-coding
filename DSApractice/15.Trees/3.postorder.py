# postorder
# left -> Right -> Root


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


def postorder_traversing(root):
    if root == None:
        return 
    postorder_traversing(root.left)
    postorder_traversing(root.right)
    print(root.data)


postorder_traversing(root)