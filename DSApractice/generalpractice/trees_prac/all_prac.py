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


def transversing(root):
    if root == None:
        return
    print(root.data)
    transversing(root.left)
    transversing(root.right)


def total_leafnodes(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    lc =  total_leafnodes(root.left)
    rc = total_leafnodes(root.right)
    return lc+rc+1


def height(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    lc = height(root.left)
    rc = height(root.right)
    return max(lc,rc)+1


def print_leafnodes(root):
    if root == None:
        return 
    if root.left == None and root.right == None:
        print(root.data)
    print_leafnodes(root.left)
    print_leafnodes(root.right)


def mirror_image(root):
    if root == None:
        return 
    root.left,root.right = root.right,root.left 
    mirror_image(root.left)
    mirror_image(root.right)
    return root

transversing(root)
print("-------------")   
k = total_leafnodes(root)
print(k)     
print("-------------")   
l = print_leafnodes(root)
transversing(k)
print("-------------")   
m = mirror_image(root)
transversing(m)
print("-------------")   
n = height(root)
print(n)
    










    