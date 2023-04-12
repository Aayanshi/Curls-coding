class Node:
    def __init__(self,x) :
        self.data = x
        self.next = None

head = None

def node_at_first(y):
    global head
    if head == None :
        head = Node(y)
        return

    node1 = Node(y)
    node1.next = head
    head = node1


def node_at_last(y):
    global head
    if head == None :
        head = Node(y)
        return
    
    cur = head
    while(cur.next != None):
        cur = cur.next
    node2 = Node(y)
    cur.next = node2


def node_at_kth(y,k):
    global head
    if head == None :
        head = Node(y)
        return
    
    cur = head 
    c = 0

    while(c!=k-1):
        c = c + 1
        cur = cur.next
    newnode = Node(y)
    newnode.next = cur.next  
    cur.next = newnode 


def printll():
    global head
    cur = head
    while (cur!=None):
        print(cur.data)
        cur = cur.next


def size():
    global head 
    
    if head == None:
        return -1
    c = 1
    cur = head
    while(cur.next!= None):
        c = c + 1
        cur = cur.next
    return c    


def search(target):
    global head
    cur = head
    c = 0
    while (cur.next!= target):
        if target == cur.data:
            return True
        cur = cur.next
    return False




def deleate(l):
    global head
    cur = head 
    
    while (cur.next.data!=l):
        cur = cur.next
    cur.next = cur.next.next
    return printll()



def del_at_end():
    global head
    cur = head

    while(cur.next.next!= None):
        cur = cur.next
    
    cur.next = None
    return printll()


def del_at_first():
    global head 

    head = head.next
    return printll()




# driver code
node_at_first(7)
node_at_first(6)
node_at_first(5)
node_at_first(4)
node_at_last(8)
node_at_last(9)
node_at_kth(4.5,3)
printll()

print("___________")
s = size()
print(s)

print("__________________")
v = search(4)
print(v)

print("____________________________")
deleate(7)

print("____________________________")
del_at_end()

print("____________________________")
del_at_first()