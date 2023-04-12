'''Given an array of positive integers nums, return the maximum possible sum of an
ascending subarray in nums.
A subarray is defined as a contiguous sequence of numbers in an array.
A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r,
numsi < numsi+1. Note that a subarray of size 1 is ascending.
Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65'''

p = [10,20,30,5,10,50]
c = len(p)
su = 0
r = []
for i in range(c):
    su = su + p[i]
    r.append(su)

print(r)    




















'''for i in range(0,c):
    s = 0
    for j in range(1,c):
        s = p[i] + p[j]
        
        if s < i+1 :
            break

            
        else :
            continue

print(s)

'''