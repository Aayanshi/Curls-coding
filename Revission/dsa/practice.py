class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

head = None
def at_end(y):
    global head
    if head == None :
        head = Node(y)
        return
    c = head
    while (c.next!=None):
        c = c.next 
        
    c.next = Node(y)    


#print(head.data)      

def printll():
    global head 
    c = head
    while (c!=None):
        print(c.data)
        c = c.next


at_end(6)
at_end(4)
at_end(7)
printll()   
   



