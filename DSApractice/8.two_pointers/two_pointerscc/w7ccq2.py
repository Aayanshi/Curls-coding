'''Write a function that reverses a string. The input string is given as an array of characters
Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]'''

# to reverse this string 

f = ["H","a","o","i","u"]

p1 = 0
p2 = len(f)-1
while p1 < p2 :
    v = f[p1]
    f[p1] = f[p2]
    f[p2] = v
    p1 = p1 + 1
    p2 = p2 - 1

print(f)    

# bubble sort 

le = len(f)
for i in range(0,le):
    m = i
    for j in range(1,le):
        if i < j:
            m = j
            (f[i],f[j]) ==  (f[j],f[i])
print(f)            


