#question12
baina = [12,23,34,45,12,23,34,45,56,56,34,23,12,2,2,2,2]
d = {}
for i in range(len(baina)):
    if baina[i] not in d:
        d[baina[i]] = 1
        
    else:
        d[baina[i]] = d[baina[i]] + 1

print(d)
l = []
p = max(d.values())
for i in d.keys():
    if d[i] == p:
        print(i) 


'''Q3. Write a program to find the count of every vowel in a string
eg.
Input:
envelope
Output :
{
A : 0,
E : 3,
I : 0,
O : 1,
U : 0
}'''

st = "envelope"
d = {}
for i in "aeiou":
    d[i] = 0   
for i in range(len(st)):
    if st[i] in d:
        d[st[i]] = d[st[i]] + 1
        
        "O(n)"
    
print(d)    



'''Find a pair with the given sum in an array
Google Translate Icon
Given an unsorted integer array, find a pair with the given sum in it.
For example,
Input:
nums = [8, 7, 2, 5, 3, 1]
target = 10
Output:
Pair found (8, 2)
or
Pair found (7, 3)
 
Input:
nums = [5, 2, 6, 8, 1, 9]
target = 12
Output: Pair not found
'''
'''d = {}

nums = [8, 7, 2, 5, 3, 1]
target = 10
for i in nums:
    if target-i in d:
        c = target-i 
        k = i
    else:
        d[i] = i    

print([c,k])   

for i in nums:
    if target - i not in d:
        d[i] = i
    else:
        c = target-i 
        k = i   

print([c,k])         

'''
nums = [2,7,11,15]
target = 22
d = {}
c = 0
for i in range(len(nums)):
    if target-nums[i] in d:
        c = i,d[target-nums[i]]
    else:
        d[nums[i]] = i    

print(c)