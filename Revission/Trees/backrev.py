#trees and its practice after a long time 

class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None

root = Node(1)        
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(6)
root.right.right = Node(7)
root.right.left = Node(9)


#inorder

def inorder(root):
    if root == None:
        return 
    inorder(root.left)
    print(root.data)
    inorder(root.right)
   

def height(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    
    lc = height(root.left)
    rc = height(root.right)
    return max(lc,rc) + 1
    














inorder(root)
print("-----------")
h = height(root)
print(h)