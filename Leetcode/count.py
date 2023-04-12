'''Given an integer num, return the number of digits in num that divide num.
An integer val divides nums if nums % val == 0.'''


'''for i in range(1,num+1):
    if i % num == 0:
        c = c + 1
print(c)   
'''
num = str(input("here= "))
k = 0
for i in num:
    if int(num) % int(i) == 0:
        k = k + 1
print(k)        


'''    def countDigits(self, num: int) -> int:
        numsi = str(num)
        res = 0
        for i in numsi:
            if num % int(i) == 0:
                res += 1
        return res'''


'''
def divible(num):
    c = 0
    if num == 0:
        return c
    c = num // divible(num % 10)
    
num = int(input("= "))
l = divible(num)
print(l)
'''


n = str(121)
def divisible(n):
    stack = []
    l = 0
    for i in n:
        if int(n) % int(i) == 0 :
            l = l + 1
            stack.append(i)
               
    return stack , l

o = divisible(n)
print(o)