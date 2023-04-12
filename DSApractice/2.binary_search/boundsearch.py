'''num = [1,1,1,2,2,2,2,3,3,3]
l = 0
h = len(num)-1
target = 2
while l < h:
    mid = (l+h)// 2
    if num[mid] < target:
        l = mid + l 
    elif num[mid]> target :
        h = mid - 1
    elif num[mid] == target:
        a = mid 
        if '''