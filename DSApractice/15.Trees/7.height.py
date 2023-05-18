# height of tree

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

def height(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    
    lc = height(root.left)
    hc = height(root.right)
    return max(lc,hc)+1


k = height(root)
print(k)