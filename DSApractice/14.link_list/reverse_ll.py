class Node:
    def __init__(self,x):
        self.data = x
        self.next = None 



def reverse(head):
    prev = None 
    cur = head

    while(cur!=None):
        nex = cur.next

        cur.next = prev
        prev = cur
        cur = nex

    head = prev
    return print_data(head)



def print_data(head):
    cur = head
    while cur!=None:
        print(cur.data,end=" ")
        cur = cur.next
    print()
   
 
def list_me(head):
    l = list()
    cur = head
    while(cur!=None):
        l.append(cur.data)
        cur = cur.next
    return l   


head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
head2.next.next.next = Node(8)



'''l = reverse(head2)
print_data(l)'''

reverse(head2)
k = list_me(head2)
print(k)



        