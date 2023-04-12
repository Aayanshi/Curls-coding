#stack 
stack = []
def empty():
    global stack
    return len(stack)==0

def push(x):
    global stack 
    stack.append(x)

def peek():
    global stack
    if empty():
        return "khali hai"
    else:
        return stack[-1]
    
def pop():
    global stack
    if empty():
        return "you dont love me"
    return stack.pop()

l = empty()
print(l)
push(7)
push(6)
push(5)
pop()
print(stack)
p =peek()
print(p)