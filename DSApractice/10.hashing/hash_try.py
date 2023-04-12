def hash(s):
    hashtable = dict()
    st = 0
    end = 0
    maxlength = 0
    n = len(s)-1

    while end<=n :
        if s[end] not in hashtable:
            hashtable[s[end]] = end
            currentlen = end-st+1
            maxlength = max(maxlength,currentlen)
            end  = end + 1
        else :
            while s[end] in hashtable:
                hashtable.pop(s[st])
                st = st + 1
            hashtable[s[end]] = end
            end = end + 1
    return maxlength               



s = "APPLE"
res = hash(s)
print(res)