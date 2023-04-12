# valid paranthesisis by stack 

def valid_p(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if len(stack)==0:
                return "invalid"
            stack.pop()
    
    if len(stack)==0:
        return "valid"
    return "invalid"

s = "(()))))"
res = valid_p(s)
print(res)

"""     stack = []
        st = ""
        for i in s:
            if len(stack)!=0 and stack[-1]==i:
                stack.pop()
            else:
                stack.append(i) 
        for i in stack:
            st = st + i
        return st     """          

''' stack = []
        d = {"(":")","[":"]","{":"}"}
        for i in s :
            if i in d:
                stack.append(i)
            elif len(stack)==0 :
                return False
            elif d[stack[-1]] != i:
                return False
            else:
                stack.pop()
        if len(stack)==0:
            return True
        return False           
            '''