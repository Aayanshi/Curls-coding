

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




#here we will find the total numbers of nodes in the trees

j = 0
def inorder(root):
    global j
    if root == None:
        return 0
    inorder(root.left)
    j = j + 1
    inorder(root.right)
    return j


p = inorder(root)
print(p)

#global variable approach is not appropriate approch we will do alternative approch


def calculate_nodes(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    
    lc = calculate_nodes(root.left)
    rc = calculate_nodes(root.right)
    return lc + rc + 1


total = calculate_nodes
print(total)