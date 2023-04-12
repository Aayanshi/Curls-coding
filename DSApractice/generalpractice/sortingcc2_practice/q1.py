'''Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must be unique and you may return
the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]'''
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
c = []
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i] == nums2[j]:
            c.append(nums1[i])
print(list(set(c)))           



