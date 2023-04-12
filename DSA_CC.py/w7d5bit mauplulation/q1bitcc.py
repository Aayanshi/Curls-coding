'''(Q-1 ) Write a program to convert a string of binary number into a decimal
number: (5 marks) (Easy)
eg:
Sample Input
st = “101”
Sample output
5'''

def deci_bin(d):
    binary = ""
    while d > 0 :
        remi = d % 2
        binary = binary + str(remi)
        d = d//2

    return binary[::-1]

d = 5
p = deci_bin(d)
print(p)
