'''Given an array of integers nums sorted in ascending order, find the starting and
ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]'''

num = [5,7,7,7,8,8,10,30,56,59,66]
l = 0
h = len(num)-1
s = -1
target = int(input("Enter your number= "))
while l<=h :
    mid = (l+h) // 2 
    if num[mid] < target :
        l = mid + 1
    
    elif num[mid] > target :
        h = mid - 1

    else : 
        s = mid
        h = mid - 1

l = 0
h = len(num) - 1
p = -1
while l<=h :
    mid = (l+h) // 2
    if num[mid] < target :
        l = mid + 1

    elif num[mid] > target:
        h = mid - 1      

    else :
        p = mid 
        l = mid + 1    



print(f"[{s},{p}]")  

 
#joint account
def searchRange(nums, target):
    n = len(nums)

    h = n-1
    res = []
    aainu = -1
    while l<=h:
        mid = (l+h)//2
        
        if nums[mid] > target:
            h = mid-1
        elif nums[mid]< target:
            l = mid+1
        else:
            aainu = mid
            h = mid-1
        
    
    
    l = 0 
    h = n-1
    kubs = -1
    while l <= h:
        mid = (l+h)//2
        if nums[mid] > target:
                h = mid-1
        elif nums[mid]< target:
                l = mid+1
        else:
                kubs = mid
                l = mid+1

        res.append(aainu)    
        res.append(kubs)
        return res


print(("kabir is just my friend and i hate him\n")*10, end = "")



'''A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.'''

nums = [1,2,3,4,4,5,6,7,7,8,10]

l = 0 
h = len(l)




l = 0
h = len(nums) - 1
        
while l < h:
    mid = (l + h) // 2
    if nums[mid] < nums[mid + 1]:
                l = mid + 1
    else:
                h = mid

print(l)
