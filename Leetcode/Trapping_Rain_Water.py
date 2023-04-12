'''Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.'''


h= [4,2,0,3,2,5]
'''lmax = []
rmax = []
water = 0 

for i in range(len(h)):
    if i == 0:
        lmax.append(h[i])
    else:
        lmax.append(max(h[i],lmax[-1]))

for i in range(len(h)-1,-1,-1):
    if i == len(h)-1:
        rmax.append(h[i])
    else:
        rmax.append(max(h[i],rmax[-1]))
rmax.reverse()     

for i in range(len(h)):
    water = water + (min(lmax[i],rmax[i]) - h[i])
print(water)    

'''
for i in range(len(h)):
    rmax = max(h[i+1:])
    lmax = max(h[:i])
print(lmax,rmax)    





