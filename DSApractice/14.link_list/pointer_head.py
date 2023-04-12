# using current pointer towards linked list 
# adding last node
# printing all data 



class Node:
    def __init__(self,x) :
        self.data = x
        self.next = None


head = None
def add_node_at_end(y):
    global head
    if head == None :
        head = Node(y)
        return
    
    cur = head 
    while (cur.next!= None):
        cur = cur.next
    cur.next = Node(y)  


add_node_at_end(6)
add_node_at_end(7)
add_node_at_end(8)
add_node_at_end(9)

'''print(head.data)
print(head.next.data)
print(head.next.next.data)
print(head.next.next.next.data)
'''

def print_LL():
    global head
    cur = head
    while cur!=None:
        print(cur.data)
        cur = cur.next


print_LL()
