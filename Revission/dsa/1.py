'''take 5 integer input from user convert it into a list and find the maximum number from the given inputs#'''

'''l = []
for i in range(1,6):
    n = int(input("here= "))
    l.append(n)

print(max(l),min(l),l)

maxi = l[0]
for i in range(1,len(l)):
    if maxi < l[i] :
        maxi  = l[i]
print(maxi)

mini = l[0]
for i in range(1,len(l)):
    if mini > l[i] :
        mini = l[i]
print(mini)''' 
'''aainu = [11,33,45,67,21,3,7,8,9,10,16]
target = (4*4) 
#write a linear search algorithm to obtain target from given list
a = aainu
for i in range(len(a)):
    if target in a:
        if a[i]== target:
            print(i)'''




'''def binary_search(aainu,target):
    l = 0
    h = len(aainu)-1

    while l <= h:
        mid = (l + h) // 2
        if aainu[mid] < target:
            l = mid + 1

        elif aainu[mid] > target:
            h = mid - 1

        else :
            return mid   
    return -1            


aainu = [3,7,8,9,10,16,18,45,67,89,95]
target = 18
k = binary_search(aainu,target)
print(k)'''

a = [11,33,45,67,21,3,7,8,9,10,16]
#sort it 

c = []
for i in range(len(a)):
    mi = a[0]
    
    for i in range(len(a)):
        if mi > a[i] :
            mi = a[i]
            

    c.append(mi)
    a.remove(mi)        

print(c)





                   



