#lets convert decimial to binary 
# we first find reminder by node and store it
# then find quotient of that number 
# do thi again till it will be zero or less than than that
# base of binary will be "2"
# new quotent will be new decimal

def decimal_to_binary(deci):
    binary = ""
    while deci>0:
        reminder  = deci % 2
        binary = binary+str(reminder)
        deci = deci // 2
    return binary[::-1]    

deci = 7
vins = decimal_to_binary(deci)
print(vins)

b = 5 & 3
print(b)