'''How Many Numbers Are Smaller Than the Current Number
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]'''

nums = [8,1,2,2,3]
nums2 = []
for i in nums:
    nums2.append(i)
print(nums2)
nums2.sort()

id = 0
while id < len(nums):
    nums[i] = nums[i]
    id = id + 1

a = []
for i in range(len(nums2)):
    a.append(i)

print(a)    
    