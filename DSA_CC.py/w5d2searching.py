### ccc of search 1

''' q1 (7.5 marks)
Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1'''

num = [-1,0,3,5,9,12]
target = int(input("here= "))



def array(num,target):
    l = 0
    h = len(num)-1

    while l <= h :
        mid = (l+h) // 2
        if num[mid] < target :
            l = mid+1
    
        elif num[mid] > target :
            h = mid - 1
    
        else :
            return mid
    return -1                    

ans = array(num,target)
print(ans)





###### q3. sum of rows n columns 
def sumrows(fuc):     
    n = len(fuc)
    m = len(fuc[0])
    print(f" {n} x {m} dimension")
    
    
    l = [ ]
    for i in range(n):
        sum = 0
        for j in range(m):
        
            if i == 0 :
                sum = sum + fuc[i][j]
                
            
            elif i == 1 :
                sum = sum + fuc[i][j]
                

            elif i == 2 :
                sum = sum + fuc[i][j]
                

            elif i == n-1 :
                sum = sum + fuc[i][j]
        
        l.append(sum)                   
    
    print(l)


fuc = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ] 

sumrows(fuc)
    

####### his way  
m = len(fuc)
n = len(fuc[0])
listrowsum = []
for i in range(m):
    sumrow = 0
    for j in range(n):
        sumrow = sumrow + fuc[i][j]
    listrowsum.append(sumrow)
print(listrowsum)


#print sum of columns as list(sum of each column as an element)
m = len(fuc)
n = len(fuc[0])
listcolsum = []
for i in range(m):
    sumcol = 0
    for j in range(n):
        sumcol = sumcol + fuc[j][i]
    listcolsum.append(sumcol)
print(listcolsum)
     
