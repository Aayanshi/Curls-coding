# here we transverse through vertically 
# to store top view we actually store them into dictionary at their axis
# their axis are left -ve and right one is +ve 

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

dict = {}
def top_view(root,axis):
    if root == None:
        return 
    
    dict[axis] = root.data

    top_view(root.left,axis-1)
    top_view(root.right,axis+1)
    return dict


t = top_view(root,0)
print(t)