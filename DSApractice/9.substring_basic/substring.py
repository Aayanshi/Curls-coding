# hashing basic or intro 

#brute force approach for substring - (continous collection of characters)

def repeat(sub):
    for i in range(len(sub)):
        if sub[i] in sub[:i] + sub[i+1:]:
            return True
    return False


def sting(s):
   maxlength = 0
   l = len(s)
   for i in range(l):
    for j in range(i,l):
        sub = s[i:j+1]
        if not repeat(sub):
            maxlength = max(maxlength,len(sub))
   return maxlength        

s = "APPLE"
lo = sting(s)
print(lo)        
              



