'''Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.'''


def merge(nums1,nums2,st1,ed1,st2,ed2):
    ed1 = len(nums1) 
    ed2 = len(nums2)
    p1 = st1
    p2 = st2
    c = []
    
    while p1<ed1 and p2<ed2:
        if nums1[p1] < nums2[p2] :
            c.append(nums1[p1])
            p1 = p1 + 1

        else :
            c.append(nums2[p2])
            p2 = p2 + 1

    while p1 < ed1 :
        c.append(nums1[p1])
        p1 = p1 + 1 

    while p2 < ed2 :
        c.append(nums2[p2])
        p2 = p2 + 1

    return c 

def median(c):
    l = 0
    h = len(c)
    mid = (l + h) // 2
    #even
    if h % 2 == 0:
        media = (c[mid-1] + c[mid]) / 2
    else:
        media = c[mid]
    
    return media           

        

if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [3,4]   
    m = len(nums1)
    n = len(nums2)

    v = merge(nums1,nums2,0,m,0,n)
    c = median(v)
    
    print(v,c)
            







