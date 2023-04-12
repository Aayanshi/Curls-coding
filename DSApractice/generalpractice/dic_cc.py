'''Q1. Write a program to find the count of all even no’s and odd no’s in an
array / list
Eg
Input:
[1,2,3,4,5,6,7,8,9,10]
output:
Odd_count = 5
Even_count = 5 (Easy) (5 marks)'''

'''nums = [1,2,3,4,5,6,7,8,9,10]
d = {}
c = 0
f = 0
for i in range(len(nums)):
    if nums[i] % 2 == 0 :
        c = c + 1
    else :
        f = f + 1
d["even"] = c
d["odd"] = f
    
print(c,f,d)    
'''

'''Q3. Write a program to find the count of every vowel in a string
eg.
Input:
envelope
Output :
{
A : 0,
E : 3,
I : 0,
O : 1,
U : 0
}

(Medium)'''

s = "ENVELOPE"
d = {"A":0,"E":0,"I":0, "O":0,"U":0 }
for i in range(0,len(s)):
    if s[i] in"AEIOU":
        if s[i] in d:
            d[s[i]] = d[s[i]]+1
        else:
            d[s[i]] = 1
print(d)
"O(n2)"

  

        


