# here we tranverse through level by level top to bottom writing left to right like in list
#step1 - find height only this can tell the levels cause they are equal
#step2 - make a func that can write nodes by level having parameters of root and level
#step3 - run that func under for loop having till height in range cause only that can stop program

# level is just only distance from root

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



#finf height
def height(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    lc = height(root.left)
    rc = height(root.right)
    return max(lc,rc) + 1

#func to print nodes at every level
def print_nodes_at_level(root,l):
    if root == None:
        return
    if l == 1:
        print(root.data , end=" ")

    print_nodes_at_level(root.left,l-1)  
    print_nodes_at_level(root.right,l-1)  



#driver code
if __name__ == "__main__":
    ht = height(root)
    print(ht)
     
    # here i i parameter for level as height (1,2,3) 
    for i in range(1,ht+1):
        print_nodes_at_level(root,i)    

