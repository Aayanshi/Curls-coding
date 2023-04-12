'''Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]'''

'''nums = [2,7,11,15]
d = dict()
target = 9
for i in range(len(nums)):
    d[nums[i]] = i
    if target - nums[i] in d:
        arna = d[target-nums[i]]
        aaina = i


print(d)
print([arna,aaina])    





nums= [3,2,4]
di = dict()
target = 6
for i in range(len(nums)):
    di[nums[i]] = i
    if target - nums[i] in di:
        a = di[target-nums[i]] 
        b = i

print([a,b])        
'''


nums = [2,7,11,15]
'''l = len(nums)
target = 9
for i in range(l):
    for j in range(i+1,l):
        if nums[i] + nums[j] == target:
            c = nums[i]
            h = nums[j]  

print(c,h)
'''

'''

def pointers(nums,target):
    nums.sort()
    p1 = 0
    p2 = len(nums)-1
    
    while p1<p2 :
        if (nums[p1]+nums[p2]) < target:
            p1 = p1 + 1
        elif (nums[p1]+nums[p2]) > target:
            p2 = p2 - 1
        else:
            k = (nums[p1], nums[p2])
            return k  
    k = "oops"
    return k           

target = 177
nums = [8,4,6,3,9]
c = pointers(nums,target)
print(c)

'''

nums = [2,7,11,15]
hashtable = {}
target = 18
for i in range(len(nums)):
    if target-nums[i] not in hashtable:
        hashtable[nums[i]] = i
    else :
        v =[hashtable[target-nums[i]],i]    

print(v)

