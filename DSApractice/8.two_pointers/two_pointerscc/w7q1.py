'''Given an integer array nums, move all 0's to the end of it while maintaining the relative
order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

nums = [0,1,0,3,12]
p1 = 0
p2 = len(nums)
while p1<p2:
    if nums[p1] == 0:
        c = nums[p1]
        nums.append(c)
        nums.remove(nums[p1])
        p1 = p1 + 1
        print(nums)
    else:
        p1 = p1 + 1
        
print(nums)



