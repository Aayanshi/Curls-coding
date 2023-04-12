# printing leafnodes
# leafnodes are terminating point of trees having no child further........




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

# inorder transversing = left root right
def inorder_leafnodes(root):
    if root == None:
        return
    inorder_leafnodes(root.left)
    if root.left == None and root.right == None:
        print(root.data)
    inorder_leafnodes(root.right)



inorder_leafnodes(root)

    
