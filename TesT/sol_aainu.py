# here i m solving test date = 29/1/23 , time = 10:46
# Q1. ans = option d

# Q2. option A

# Q3. option B

# Q4.  option A
'''List1 = [5, 50, 55, 555, 5555]
List1.count(5)'''

# option B
n =(m for m in range(3))
for m in n:
   print(m)
for m in n:
   print(m)

# option A

'''write a python program to remove the duplicate elements from the given list'''
aainu = ["a", "b", "a", "c", "c"]
d = {}
e = 0
for i in range(len(aainu)):
    d[aainu[i]] = i
print(d)

'''write the code to reverse a string given by user'''
s = (input("write here = "))
print(s[::-1])

def reverse(s):
    l = len(s)
    if l == 0:
        return 
    k = s[0]
    reverse(s[1:])
    print(k,end="") 

reverse(s)  
print()
'''write the recursive program to check if a given number is a palindrome or not'''
# i m sorry yahan pe maine sirf thoda sa dekha
 
'''def palindrome(p):
    if p == 0:
        return s 
    s = 
    mujhe ye smjh nahi aaya     '''


'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a
 given target value.

You must write an algorithm of binary search.'''
#hint : sort it first
num = [15,7,7,7,8,8,6,4,8,10]
nums = sorted(num)
target = 8

s = -1
l = 0
h = len(nums)-1
while l <= h :
    mid = (l+h)//2
    if nums[mid] < target:
        l = mid + 1
    elif nums[mid] > target:
            h = mid -1
    else :
        s = mid 

"i have one doubt at lower and highper bound thats why lefting it here"        



