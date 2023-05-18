# how to check is the binary tree  is BST or not ?

class Node:
    def __init__ (self, x):
        self.data = x
        self.left = None
        self.right = None


'''root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(6)
root.right.right = Node(7)
root.right.left = Node(9)'''

'''
root = Node(10)
root.left = Node(7)
root.right = Node(13)
root.left.left = Node(6)
root.left.right = Node(9)
root.right.right = Node(14)
root.right.left = Node(11)'''

root = Node(10)

def Valid_bst(root):

    if root == None:
        return {
                "mine" : float("inf"),
                "maax" : float("-inf"),
                "bst"  : True
        }
    
    if root.left == None and root.right == None:
        return {
                "mine" : root.data,
                "maax" : root.data,
                "bst"  : True
        }
    
    lc = Valid_bst(root.left)
    rc = Valid_bst(root.right)

    if (lc["bst"] is True ) and (rc["bst"] is True) and (lc["maax"] < root.data ) and (root.data < rc["mine"]):
        return {
                "mine" : lc["mine"],
                "maax" : rc["maax"],
                "bst"  : True
        }
    
    else:
        return {
                "mine" : min(root.data,lc["mine"]),
                "maax" : max(root.data,rc["maax"]),
                "bst"  : False
        }


b = Valid_bst(root)
print(b["bst"])