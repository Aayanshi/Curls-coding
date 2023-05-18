# lets code for left view here we only do by printing first number of every level either right or left 
# here we compare by our current level with max level variable


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

'''
max_level = float("-inf")
def left_view(root,current_level):
    global max_level
    if root == None:
        return
    
    if current_level > max_level:
        print(root.data )
        max_level = current_level 

    left_view(root.left,current_level + 1)
    left_view(root.right,current_level + 1) '''  



def left_view(root,current_level,max_level):
    if root == None:
        return
    
    if current_level > max_level[0]:
        print(root.data )
        max_level[0] = current_level 

    left_view(root.left,current_level + 1,max_level)
    left_view(root.right,current_level + 1,max_level) 


if __name__ == "__main__":
    max_level = [-1]
    left_view(root,0,max_level)


