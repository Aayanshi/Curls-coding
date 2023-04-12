# buble sort 
# it sort in same list without creating new one 
# it work on smaller at left side to bigger at right side 

ar = [8,5,6,3,9,1]

l = len(ar)
for i in range(0,l):
    minu = i
    for j in range(i+1,l):
        if ar[i] > ar[j]:
            minu = j
            (ar[i],ar[j]) == (ar[j],ar[i])

print(ar)