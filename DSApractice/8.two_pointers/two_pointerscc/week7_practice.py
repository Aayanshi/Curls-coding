'''Given an integer array nums sorted in non-decreasing order, return an array of the
squares of each number sorted in non-decreasing order.
Example 1:
Input: nums = [-4,-1,0,3,10]'''

nums = [-4,-1,0,3,10]
sq = [] 
for i in range(len(nums)):
    c = nums[i] * nums[i]
    sq.append(c)

print(sq)


def merge(sq,st1,ed1,st2,ed2):
    v = []
    p1 = st1
    p2 = st2
    while p1<=ed1 and p2<=ed2 :
        if sq[p1] < sq[p2] :
            v.append(sq[p1])
            p1 = p1 + 1
        else :
            v.append(sq[p2])
            p2 = p2 + 1

    while p1 <= ed1:
        v.append(sq[p1])
        p1 = p1 + 1

    while p2 <= ed2 :
        v.append(sq[p2])
        p2 = p2+1

    id = 0
    while id < len(v):
        sq[st1+id] = v[id]
        id = id + 1
    return sq   



def merge_sort(sq,low,high):
    mid = (low + high)//2
    if low == high :
        return 
    merge_sort(sq,low,mid)
    merge_sort(sq,mid+1,high)
    merge(sq,low,mid,mid+1,high)


#sq = [16, 1, 0, 9, 100]
merge_sort(sq,0,len(sq)-1)       
print(sq)

