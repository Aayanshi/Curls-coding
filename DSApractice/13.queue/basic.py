# queue = its just like stack but runs over principle "first in first out", last in and last out

queue = []
def enqueue(x):
    global queue
    return queue.append(x)

def dequeue():
    global queue
    if isempty():
        return "already khali hai"
    return queue.pop(0)

def isempty():
    global queue
    return len(queue)==0

def peek():
    global queue
    return queue[0]


enqueue(2)
enqueue(3)
enqueue(8)
enqueue(66)
dequeue()
re = isempty()
print(re)
l =peek()
print(l)
print(queue)