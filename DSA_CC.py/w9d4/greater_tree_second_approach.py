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


'''def dfs(node, val):
    if node.right:
        val = dfs(node.right, val) 
        val += node.val 
        node.val = val 
        if node.left: 
            val = dfs(node.left, val) 
            return val 
    dfs(root, 0) 
    return root
        '''

def inorder(root):    #in inorder we travel through left then root and then right
    if root == None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)


def greater_tree(root):
    k = 0
    def convert(root):
        nonlocal k
        if root == None:
            return 
        convert(root.right)
        k = k + root.data
        root.data = k
        convert(root.left)
        return root
    convert(root)
    return inorder(root)

greater_tree(root)







        

