# lets check parenthesise

def valid_parenthesis(stack):
    ob = cb = 0
    for i in stack:
        if i == "(" :
            ob = ob + 1
        
        else:
            cb = cb + 1

        if ob >= cb :
            continue

        else :
            return "invalid 1"

    if ob == cb :
        return " valid"

    else :
        return "invalid 2"              

stack = "()(("          
l = valid_parenthesis(stack) 
print(l)           

## 

def parenthesis(p):
    stack1 = []
    for i in p:
        if i == "(":
            stack1.append(i)
        else:
            if len(stack1)==0:
                return "empty"
            stack1.pop() # here we pop only "(" cause only we have in stack

    if len(stack1)==0 :
        return "Valid"
    return "invalid"    

p = "(())"
re = parenthesis(p)
print(re)

