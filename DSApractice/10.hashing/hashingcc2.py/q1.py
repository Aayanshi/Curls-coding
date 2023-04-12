'''Given an array of integers nums containing n + 1 integers where each integer is
in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only
constant extra space.
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2
'''
'''nums = [1,3,4,2,2]
d = {}
ed = len(nums)
st = 0
for i in nums:
    if i not in d:
        d[i] = 1
    else:
        print(i) ''' 


'''You are given an integer array nums. The unique elements of an array are the elements that appear
exactly once in the array.
Return the sum of all the unique elements of nums.
Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.'''

'''nums = [1,2,3,2]
d = {}
ed = len(nums)
c = 0
for i in nums:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1  
print(d)         

for i in d.keys():        
    if d[i]==1:
        c = c + i
print(c) 
'''


'''Write a function to find the longest common prefix string amongst an array of
strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
'''
'''d = {}
strs = ["flower","flow","flight"]
st = 0
ed = 0
while nums[ed] < len(strs)-1:
    if nums[ed]




    print(d)    '''



s = ["flower","flow","flight"]
st = 0
ed = 0
hashtable = {}
prefix = ""
l = len(s)
for i in s:
    if i not in hashtable:
        hashtable[i] = i
    else:
        print(i)    











'''while ed <= l:
    if s[ed] not in hashtable:
        hashtable[s[ed]] = ed
        ed = ed + 1
    else:
        if s[st] in hashtable:
            hashtable[s[ed]] = hashtable[s[ed]] + ed
            print(hashtable[s[ed]])
            ed = ed + 1
         '''







