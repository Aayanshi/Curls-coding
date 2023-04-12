
class Node:
    def __init__(self,x) :
        self.data = x
        self.next = None


head = None

def add_at_beginning(y):
    global head
    if head == None:
        head = Node(y)
        return
    nn = Node(y)
    nn.next = head
    head = nn

def add_at_kth(k,y):
    global head 
    
    if head == None:
        head = Node(y)
        return 
    
    c = 1
    cur = head
    while(c != k-1):
        cur = cur.next
        c = c + 1

    newn = Node(y)  
    newn.next = cur.next 
    cur.next = newn 
    

def at_end(y):
    global head
    if head == None:
        head = Node(y)
        return 

    cur = head
    while(cur.next!= None) :
        cur = cur.next 

    node = Node(y)
    cur.next = node


def printi():
    global head
    cur = head
    while(cur != None):
        print(cur.data)
        cur = cur.next


add_at_beginning(3)
add_at_beginning(2)
add_at_beginning(1)
add_at_kth(3,3.4)
at_end(17)    
at_end(28)    
printi()   



