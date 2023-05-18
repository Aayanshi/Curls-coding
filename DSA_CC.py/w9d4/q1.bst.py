#Q-1 ) Write a program to print nodes in a BST having odd values:


class Node:
    def __init__ (self, x):
        self.data = x
        self.left = None
        self.right = None


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right.left = Node(13)


def odd_bst(root):

    if root == None:
        return
    
    if (root.data) % 2 != 0:
        print(root.data)
        
    odd_bst(root.left)
    odd_bst(root.right)  
    

odd_bst(root)

