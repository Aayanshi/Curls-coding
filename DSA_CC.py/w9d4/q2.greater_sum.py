# Convert BST to Greater Tree

#Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every
#key of the original BST is changed to the original key plus the sum of all keys 
#greater than the original key in BST.



class Node:
    
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None


root = Node(4)
root.left = Node(1)
root.right = Node(6)
root.left.left = Node(0)
root.left.right = Node(2)
root.left.right.right= Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
root.right.right.right = Node(8)


def Greater_BST(root):
    if root == None :
        return
    










class Node:
    
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None


root = Node(4)
root.left = Node(1)
root.right = Node(6)
root.left.left = Node(0)
root.left.right = Node(2)
root.left.right.right= Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
root.right.right.right = Node(8)


def inorder(root):    #in inorder we travel through left then root and then right
    if root == None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)



def aainu_ka_pyar(root):    #main function
    sum = 0
    def aainu_ka_gussa(root):  #nested function
        nonlocal sum              #nonlocal built in variable to keep the variable 
                                  #same to both function and to get it altered in the 
                                  # recursive calls inside nested function
        if root == None:
            return
    
        aainu_ka_gussa(root.right)    #we are traversing right and left subtrees inside nested function
        root.data = root.data+sum
        sum = root.data
        aainu_ka_gussa(root.left)    #we are traversing right and left subtrees inside nested function
    aainu_ka_gussa(root)             #and then we traverse the nested function on root inside main function
    return inorder(root)




aainu_ka_pyar(root)