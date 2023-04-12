# reverse linlist 

class Node:
    def __init__(self,x) :
        self.data = x
        self.next = None

head = None

head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(9)


def print_ll(head):
    cur = head
    while(cur!=None):
        print(cur.data)
        cur = cur.next
    

def reverse(head):
    prev = None
    cur = head

    while(cur!=None):
        nxt = cur.next

        cur.next = prev
        prev = cur
        cur = nxt

    head = prev    
    return print_ll(head)



reverse(head)

