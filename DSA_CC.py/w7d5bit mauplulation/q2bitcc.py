'''(Q2) Write a function that takes an unsigned integer and returns the number of '1' bits
it has (also known as the Hamming weight).
Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has
a total of three '1' bits.
'''

'''def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= n - 1
        return count'''


''' result = 0
for _ in range(32):
	result += n & 1
	n >>= 1
return result'''       



'''
c = 0
n = 0o00000000000000000000000000001011
for i in range(30,32):
    n = n >> 1
    c = c + 1
  
print(c, n)



def count(n): 
    v = 0      
    while n :
        v = v + 1
        n = n & n-1
        print(n,n-1)
    return v    

vins = count(n)
print(vins)'''


c = "0o00000000000000000000000000001011"
b = str(c)
k = 0
for i in range(len(c)):
    if c[i] == "1":
        k = k + 1
        print(i,k)
   
print(k)       


'''b = 0o00000000000000000000000000001011
counti = 0
while b:
    b = b >> 1
    c = c + 1
print(b, c)
print(type(b))


'''

'''c = 0o00000000000000000000000000001011 - 1
n = b & c
print(n,c)'''