#Remove Duplicates from Sorted List




class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


head = None

#function to add a new node at the end of linked list
def add_node_at_end(x):
    global head

    if head == None:
        head = Node(x)
        return
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(x)

#function to print the whole linked list 
def print_linked_list():
    global head

    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

#add at beginning of linked list
def add_at_beginning(x):
    global head
    if head == None:
        head = Node(x)
        return
    blue = Node(x)
    blue.next = head
    head = blue


#function to add a node at desired position in linked list

def add_at_desired_position(k,x):
    global head
    if head == None:
        head = Node(x)
        return
    curr = head
    count = 1
    while count < k-1:
        curr = curr.next
        count = count + 1

    newbud = Node(x)
    newbud.next = curr.next
    curr.next = newbud


# will tell the size of the linklist
def size():
    global head 
    c = 1
    cur = head 
    if head == None:
        return -1 
    while (cur.next != None):
        c = c + 1
        cur = cur.next
    return c        


# will search the element of that
def search(target):
    global head 
    cur = head 

    while (cur.next != None):
        cur = cur.next
        if target == cur.data :
            return True
    return False

    #sol 2
    #while(target!= cur.data):
    #    cur = cur.next
    #   return True    
    #return False


# to get element in that ll
def access(k):
    global head 
    cur = head 
    c = 0

    i = size()
    if i-1 < k:
        return "not in list"
    while (c!=k):
        cur = cur.next
        c = c + 1   
    return cur.data  
    

def delete(n):
    global head 
    c = 0
    node = head
    
    while(c!=n):
        c = c + 1 
        node = node.next
    
    var = node.next.data
    node.data = var
    node.next = node.next.next
    return print_linked_list()


'''def duplicate():
    global head
    
    cur = head
    while(cur!= None):
        
        if cur.data == cur.next.data:    
            cur.data = cur.next.data
            cur.next = cur.next.next 
        cur = cur.next
        
    return print_linked_list()   '''


'''def duplicate():
    global head
    cur = head
    while(cur!= None):
        if cur.data == cur.next.data:
            cur.data = cur.next.data
            cur.next = cur.next.next
            
            if cur.next.next == None:
                cur.data = cur.next.data
                cur.next = None 
        cur = cur.next    
    return print_linked_list()   '''

def duplicate():
    global head
    cur = head

    while(cur != None):
        if cur.next == None:
            break
        elif cur.data == cur.next.data:
            cur.data = cur.next.data
            cur.next = cur.next.next
        else:
            cur=cur.next  
    return print_linked_list()       


def ll():
    global head
    print(head)











#driver code

'''add_node_at_end(17)
add_node_at_end(62)
add_node_at_end(28)
add_node_at_end(23)
add_at_beginning(17)
add_at_beginning(1)'''

'''add_at_desired_position(4,"me")'''
add_at_beginning(4)
add_at_beginning(4)
add_at_beginning(4)
add_at_beginning(3)
add_at_beginning(2)
add_at_beginning(2)
add_at_beginning(1)
add_at_beginning(1)
add_at_beginning(0)
add_at_beginning(0)


print("------------------")
#print_linked_list()

print("---------------")
g = access(5)
print(g)

print("----------------")
#delete(2)

print("_________________")
duplicate()

print("-------------")
print(head)

