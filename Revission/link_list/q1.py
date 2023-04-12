class Node:
    def __init__(self,a):
        self.data = a
        self.next = None




head = None
def printll():
    global head
    cur = head
    while cur != None:
        print(cur.data, end = " ")
        cur = cur.next



#inserting node at beginning
def node_At_top(f):
    global head
    if head == None:
        head = Node(f)
        return

    nn = Node(f)
    nn.next =  head
    head = nn 
    


def node_at_end(j):
    global head 
    if head == None:
        head = Node(j)
        return 
    
    cur = head 
    while(cur.next!=None):
        cur = cur.next
    ne = Node(j)
    cur.next = ne




def node_at_kth(x,k): 
    global head
    if head == None:
        head = Node(x)
        return 
    
    c = 0
    cur = head
    while (c!=k-1):
        cur = cur.next
        c = c + 1

    nn = Node(x)   
    nn.next = cur.next 
    cur.next = nn



def sum_link_ll():
    global head
    cur = head
    c = 0
    while(cur!=None):
        c = c + cur.data
        cur = cur.next
    return c


def find_mid():
    global head 
    l = list()
    cur = head
    while cur!=None:
        l.append(cur.data)
        cur = cur.next

    #lets find mid
    li = 0
    h = len(l)-1
    mid = (li+h)//2     
    return  l[mid]


def delete(d):
    global head
    cur = head
    c = 0
    while(c!=d-1):
        cur = cur.next
        c = c + 1
    
    cur.next = cur.next.next
    return printll()    



def delite(p):
    global head
    cur = head
    c = 0
    while(c!=p):
        cur = cur.next
        c = c + 1
    
    cur.data = cur.next.data
    cur.next = cur.next.next
    return printll()    

def reversi():
    global head 
    cur = head 
    prev = None
    
    while(cur!=None):
        nex = cur.next
        
        cur.next = prev
        prev = cur
        cur = nex

    head = prev
    return printll()    















#driver code
node_At_top(1)
node_At_top(2)
node_At_top(3)
node_At_top(8)
node_at_end(4)
node_at_end(9)
node_at_end(6)
node_at_end(7)
node_at_kth(5,1)

printll()
print( )
print("---------------")
l = sum_link_ll()
print(l)

print("---------------")
k = find_mid()
print(k)

print("---------------")
delete(3)

print("---------------")
delite(5)

print("---------------")
r = reversi()
print(r)
