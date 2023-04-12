def valid_parenthesis(st):
    ob = 0
    cb = 0
    for i in st:
        if i == "(":
            ob = ob + 1
        elif i == ")":
            cb = cb + 1
        
        if ob>=cb:
            continue
        else:
            return "invalid in loop"
    
    if ob == cb :
        return "valid outside loop"
    else:
        return "invalid"
    
st = "(())((()"
res = valid_parenthesis(st)
print(res)