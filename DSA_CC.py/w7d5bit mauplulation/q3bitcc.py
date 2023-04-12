'''Write a function to perform XOR between two positive integers: (5
\marks), do not use the xor op`erator.
(oldsaxzEasy)
Sample Input:
A = 5
B = 3
Sample Output:A^B = 6
explanation:
Take two inputs A and B as integers. => A = 5 , B = 3 Convert them to
binary, => A = 101, B = 011 perform XOR operation, => A^B = 110 return
resultant binary number as decimal number . => (110)2 =
(6)10'''

def xor_binary(n1,n2,k):
    
    if n1 == n2 :
        return 0
    k = n1 | n2
    return bin(k)        

n1 = 5
n2 = 3
k = ""
vins = xor_binary(n1,n2,k)    
print(vins)

c = 4
l = 3
h = 4 ^ 3
print(h)

