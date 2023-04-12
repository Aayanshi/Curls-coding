# find next greater element
def Greater_no_next_door(a):
    n = len(a)
    b = [-1]* n
    stack = []

    for idx,val in enumerate(a):
        if len(stack)==0:
            stack.append(idx)
        else:
            while len(stack)!=0 and a[stack[-1]] < val:
                x = stack.pop()
                b[x] = val
            stack.append(idx)

    #if len(stack)!=0:
    #    x = stack.pop()
    #    b[x] = -1 

    return b               

a = [2,1,7,4,6,8,1,9]                    
vins = Greater_no_next_door(a)
print(vins)
