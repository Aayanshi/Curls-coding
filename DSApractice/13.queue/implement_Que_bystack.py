'''232. Implement Queue using Stacks

Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 
'''

stack1 = []
stack2 = []
l  = 0
p = 0


def isempty():
    if len(stack1)==0 and len(stack2)==0:
        return True
    else:
        return False
    

def peek():
    if len(stack2)==0:
        while len(stack1)>0:
            p = stack1.pop()
            stack2.append(p)
    else:
        return stack2[-1]        
    return stack2[-1]        


def push(x):
    stack1.append(x)
    

def popy():
    global l
    if len(stack2)==0:
        while len(stack1)>0:
            l = stack1.pop()
            stack2.append(l)
    else:
        return stack2.pop()        
    
    return stack2.pop()


    
push(4)
push(5)
push(6)
popy()
c =peek()
print(c)
print(stack2,stack1)

