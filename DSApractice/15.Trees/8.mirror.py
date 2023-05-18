# lets make mirror image of trees

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

def mirror(root):
    if root == None:
        return 
    root.left,root.right = root.right,root.left
    mirror(root.left)
    mirror(root.right)
    return root


def preorder(root):
    if root == None:
        return 
    print(root.data)
    preorder(root.left)
    preorder(root.right)


preorder(root)

print("____________________")
res = mirror(root)
preorder(res)