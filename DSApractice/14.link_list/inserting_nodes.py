# we will insert node at diferent places

class Node:
    def __init__(self,x):
        self.data = x
        self.next = None



head = None

#adding at last so that we can create some nodes for rest of the places
def add_node_at_end(y):
    global head
    if head == None :
        head = Node(y)
        return
    
    cur = head 
    while (cur.next!= None):
        cur = cur.next
    cur.next = Node(y)  



def print_LL():
    global head
    cur = head
    while cur!=None:
        print(cur.data)
        cur = cur.next


# inserting node at first position 
def adding_node_at_first(y):
    global head
    if head == None:
        head = Node(y)
        return
    node = Node(y)
    node.next = head
    head = node 




#inserting node at k-th position 
def adding_node_at_btw(k,y):
    global head 
    if head == None:
        head = Node(y)
        return
    
    
    c = 1
    cur = head
    while(c!=k-1):
        cur = cur.next
        c = c + 1
    newnode = Node(y)
    newnode.next = cur.next 
    cur.next = newnode



adding_node_at_first(9)
adding_node_at_first(8) 
adding_node_at_first(7)
adding_node_at_btw(3,7.5) 
add_node_at_end(10)
print_LL()
