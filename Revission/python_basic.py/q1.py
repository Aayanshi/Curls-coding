''' q1.  Convert a decimal number into binary

Write a function in Python that accepts a decimal number and returns the equivalent binary number.
To make this simple, the decimal number will always be less than 1,024, so the binary number returned 
will always be less than ten digits long.'''


def deci_bin(n):
    binary = ""
    while n > 0:
        remi = n % 2 
        binary = binary + str(remi)
        n = n // 2
    return binary[::-1]

n = int(input("="))
j = deci_bin(n)
print(j)



