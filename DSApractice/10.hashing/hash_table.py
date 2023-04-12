#### hashing 

def hashing(c):
    hashtable = dict()
    st = 0
    ed = 0
    maxlength = 0
    l = len(c)-1
    
    while ed <= l:
        if c[ed] not in hashtable :
            hashtable[c[ed]] = ed
            
            cl = ed-st+1
            maxlength = max(cl,maxlength)
            ed = ed + 1
        else :
            while c[st] in hashtable:
                hashtable.pop(c[st])
                st = st + 1
            hashtable[c[ed]] = ed 
            ed = ed + 1    
    return maxlength                


if __name__ == "__main__":
    
    c = "ADOBECODEBANC"
    v = hashing(c)
    print(v)
