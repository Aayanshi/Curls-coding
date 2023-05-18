# level order transversing

class Node:
    def __init__ (self, x):
        self.data = x
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.left = Node(9)
root.right.right = Node(7)



def height(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    
    lc = height(root.left)
    rc = height(root.right)
    return max(lc,rc)+1
        

def print_by_level(root,l):
    if root == None :
        return 

    if l == 1:
        print(root.data,end=" ")

    print_by_level(root.left,l-1)
    print_by_level(root.right,l-1)


ht = height(root)
print(ht)

print("----------------")
for i in range(1,ht+1):
    print_by_level(root,i)
print("----------------")


def left_view(root,current_level,max_level):
    if root == None:
        return 
    
    if current_level > max_level[0]:
        print(root.data, end = " ")
        max_level[0] = current_level 

    left_view(root.left,current_level+ 1,max_level) 
    left_view(root.right,current_level+ 1,max_level)    


print("----------------")
max_level = [-1]
left_view(root,0,max_level)


d = {}
def top_view(root,axis):
    if root == None:
        return 
    
    [axis] = root.data

    top_view(root.left,axis-1)
    top_view(root.right,axis+1)
    return dict 


t = top_view(root,0)
print(t)
