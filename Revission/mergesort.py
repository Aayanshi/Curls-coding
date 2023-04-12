def mergesort(a,st1,ed1,st2,ed2):
    p1 = st1
    p2 = st2
    c = []
    while p1<=ed1 and p2<=ed2:
        if a[p1] < a[p2] :
            c.append(a[p1])
            p1 = p1 + 1
        else :
            c.append(a[p2])
            p2 = p2 + 1

    while p1<=ed1:
        c.append(a[p1])
        p1 = p1 + 1

    while p2<=ed2:
        c.append(a[p2])
        p2 = p2 + 1

    idx = 0
    while idx < len(c):
        a[idx] = c[idx]
        idx = idx + 1

    return a

def mergefunc(a,low,high):
    mid = (low + high) //2
    if low == high:
        return
    mergefunc(a,low,mid)
    mergefunc(a,mid+1,high)
    mergesort(a,low,mid,mid+1,high)


a = [2,4,6,8,1,3,5,7,9]
n = len(a)-1
m = len(a)-1
mergefunc(a,0,len(a)-1)
print(a)

