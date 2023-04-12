'''Q-3 ) Sort Colors
https://leetcode.com/problems/sort-colors/submissions/
(5 marks)
Given an array nums with n objects colored red, white, or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order red,
white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue,
respectively.
You must solve this problem without using the library's sort function.
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
 '''

nums = [2,0,2,1,1,0]

l = len(nums)

for i in range(0,l):
    mini = i
    for j in range(i+1,l):
        if nums[i] > nums[j]:
            mini = j
            (nums[mini],nums[i]) = (nums[i],nums[mini])
print(nums)            
            
             