stack = list()

def isEmpty():
    global stack
    return(len(stack)== 0) 

f = isEmpty()
print(f)

def push(n):
    global stack
    stack.append(n)

push(10)
push(7)
push(20)


def pop():
    global stack
    if isEmpty() == True:
        return "Error its empty"
    stack.pop()   

pop()



def peek():
    global stack
    if isEmpty() == True:
        return "Error its empty"  
    return stack[-1]        

re = peek()
print(re) 
print(stack)