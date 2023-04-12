
class Node:
    def __init__(self,x):
        self.data = x
        self.next = None 


head = None 

def add_end(y):
    global head
    if head == None:
        head = Node(y)
        return 
    
    cur = head
    while (cur.next!=None):
        cur = cur.next
    cur.next = Node(y)


def print_data():
    global head
    cur = head
    while cur!=None:
        print(cur.data)
        cur = cur.next

add_end(28)
add_end(17)
add_end(11)
print_data()
