'''Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000'''

d = {
"I "  :         1,                
"V "  :         5,
"X "  :         10,
"L"   :         50,
"C"   :         100,
"D"   :         500,
"M"   :         1000
}

'''n = 11
c = n

k = ""

while c > 0:
    c = n % 10 
    b = c // 10'''

t = 0    
for i in d:
    t = d[i]   + t

print(t)
        


