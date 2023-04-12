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



'''k = 0
def inorder_traversing(root):
    global k
    if root == None:
        return 
    inorder_traversing(root.left)
    k = k + root.data
    inorder_traversing(root.right)
    return k


i = inorder_traversing(root)
print(i)
   '''

j = 0
def inorder(root):
    global j
    if root == None:
        return 
    inorder(root.left)
    j = j + 1
    inorder(root.right)
    return j


p = inorder(root)
print(p)

