'''Q-2 ) Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
(5 marks)
You are given two integer arrays nums1 and nums2, sorted in
non-decreasing order, and two integers m and n, representing the number
of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing
order.
The final sorted array should not be returned by the function, but instead be
stored inside the array nums1. To accommodate this, nums1 has a length of
m + n, where the first m elements denote the elements that should be
merged, and the last n elements are set to 0 and should be ignored. nums2
has a length of n.
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6]. The result of
the merge is [1,2,2,3,5,6] with the underlined elements coming
from nums1.
'''

n1 = [1,2,3,0,0,0]
n2 = [2,5,6]
c = []
for i in range(len(n1)):
    if 0 in n1 :
        c.append(0)
        n1.remove(0)
print(n1,c)   

def merge(n1,n2,st1,ed1,st2,ed2):
    p1 = st1
    p2 = st2
    ed1 = len(n1)
    ed2 = len(n2) 
    f = []

    while p1<ed1 and p2<ed2:
        if n1[p1] <n2[p2]:
            f.append(n1[p1])
            p1 = p1 + 1

        else :
            c.append(n2[p2])
            p2 = p2 + 1


    while p1<ed1 :
        f.append(n1[p1])
        p1 = p1 + 1

    while p2<ed2 :
        f.append(n2[p2])
        p2 = p2 + 1

    return f    

res = merge(n1,n2,0,len(n1),0,len(n2))
print(res)


n1 = [1,2,3,0,0,0]
id = 0
for i in range(len(n1)):
    res[i] = n1[i] 
print(n1)    



