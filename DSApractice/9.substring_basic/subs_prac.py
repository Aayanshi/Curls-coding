# substring 


def repeat(sub):
    for i in range(len(sub)):
        if sub[i] in sub[:i] + sub[i+1:]:
            return True
    return False 



def sting(st):
    l = len(st)
    maxlength = 0
    for i in range(l):
        for j in range(i,l):
            sub = st[i:j+1]
            if not repeat(sub):
                maxlength = max(maxlength,len(sub))
    return maxlength            


st = "apple"
l = sting(st)
print(l)