# all back to codes after beautiful break....
class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# transversing
#preorder

def preorder(root):
    if root == None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)
    

preorder(root)

print("-----------------------")

def inorder(root):
    if root == None:
        return 
    inorder(root.left)
    print(root.data)
    inorder(root.right)

inorder(root)

print("-----------------------")

def preorder(root):
    if root == None:
        return
    preorder(root.left)
    preorder(root.right)
    print(root.data)

preorder(root)

print("-----------------------")

def leafnodes(root):
    if root == None:
        return
    if root.left == None and root.right == None:
        print(root.data)
    leafnodes(root.left)
    leafnodes(root.right)

leafnodes(root)        

print("-----------------------")

# calculate total nodes
def calculate_nodes(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    lc = calculate_nodes(root.left)
    rc = calculate_nodes(root.right)
    return (lc + rc) + 1
    
c = calculate_nodes(root)
print(c)

print("-----------------------")

def height_nodes(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    lc = height_nodes(root.left)
    rc = height_nodes(root.right)
    return max(lc,rc) + 1
        
v = height_nodes(root)
print(v)        


print("-----------------------")

def mirror(root):
    if root == None:
        return
    root.left ,root.right = root.right ,root.left
    print(root.data)
    mirror(root.left)
    mirror(root.right)

mirror(root)
