
di = {"aaya":1,"aaina":3,"aaya":2,"ina":4,"aayanshi":4}
target = 4
for i in range(len(di)-1) :
    c = i + i
    if di.keys() == target:
        print(di.keys(c))



'''li = ["a","b","c","e","a","b","f","c"]
di = dict()
for i in range(len(li)):
    if i not in di:
        di[li[i]] = i 
        print(di)
    else:
        di[li[i]] = di[li[i]] + 1     
print(di)     '''
'''
st = 0
target = 6
di = {"a":1,"b":2,"c":4,"e":3,"a":5,"b":7,"f":8,"c":11}
for i in di:
    if target == c:
        c = di[i] + di[st]
        st = st + 1
print(di[i],di[st],)
'''

'''
target = 3
di = {"a":1,"b":2,"c":4,"e":3,"a":5,"b":7,"f":8,"c":11}
for i in di.keys():
    #print(i,"value",di[i])
    if di[i] == target:
        cb = di[i]
        bc = i
        print(bc, "vlue is", cb)
        #c = c + 1  
#print(i,di[i],c)

'''

target = 9
l = [1,2,4,5,6,7,8,10]
d = {}
for i in range(len(l)):
    d[l[i]] = i
    
    if c == target-l[i] :
        j = i
        k = target-l[i]
        # = l[i]
        #k = l[i+1]
print(d[k],d[l[j]])






