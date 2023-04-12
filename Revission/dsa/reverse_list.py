#reverse list
l =[1,2,3,4,5]
k = []
for i in range(len(l)-1,-1,-1):
    k.append(l[i])

l.clear()
print(k,l)