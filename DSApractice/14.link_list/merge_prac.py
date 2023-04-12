#merge linklist
class Node:
    def __init__(self,x):
        self.data = x
        self.next = None


def merge(head1,head2):
    p1 = head1
    p2 = head2
    head3 = None

    while(p1!=None and p2!=None):
        if p1.data < p2.data :
            if head3 == None:
                head3 = Node(p1.data)
                cur = head3 
            else:
                cur.next = Node(p1.data)
                cur = cur.next 
            p1 = p1.next
        
        else:
            if head3 == None:
                head3 = Node(p2.data)
                cur = head3
            else:
                cur.next = Node(p2.data)
                cur = head3     
            p2 = p2.next


    while(p1!=None):
        cur.next = Node(p1.data)
        cur = cur.next 
        p1 = p1.next


    while(p2!=None):
        cur.next = Node(p2.data)
        cur = cur.next 
        p2 = p2.next            

    return head3




def printl(head):
    cur = head
    while(cur!=None):
        print(cur.data,end=" ")
        cur = cur.next
    print() 


head1 = Node(11)
head1.next = Node(13)    
head1.next.next = Node(15)     



head2 = Node(12)
head2.next = Node(14)    
head2.next.next = Node(16)     
head2.next.next.next = Node(20)


printl(head1)
printl(head2)

res = merge(head1,head2)
printl(res)







