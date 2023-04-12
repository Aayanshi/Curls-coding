# decimal to binary conversion

def d_2_b(n):
    binary = ""
    while n > 0:
        remi = n % 2
        binary = binary + str(remi)
        n = n//2 

    return binary[::-1]

n = int(input("enter your number= "))
c = d_2_b(n)
print(c)       


def deci_bini(n):
    binary = ""
    if n >= 1 :
        return deci_bini(n//2)   
    binary = binary + str(n % 2)  
    return binary[::-1]

     

v = deci_bini(n)
print(v)   
