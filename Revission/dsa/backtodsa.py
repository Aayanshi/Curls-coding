arr = [12,23,45,14,16,19,6]
    #  0  1  2   3   4  5  6
#write a code to find the lcm of 2 and 3 

"linear search"

'''target = 6
for i in range(len(arr)):
    if arr[i] == target :
        print(i)
'''
"binary search"

li = [5, 6, 12, 14, 16, 19, 23, 45]
#[6, 12, 14, 16, 19, 23, 45]
# 0   1   2   3   4   5   6
def bsearch(li):
    l = 0                     
    h = len(arr)-1
    target = 6
    
    
    while l <= h:
        mid = (l+h)//2
        
        if li[mid] < target :
            l = mid + 1
        
        elif li[mid] > target:
            h = mid - 1
    
        else :
            return mid
    return -1
    
k = bsearch(li)
print(k)




