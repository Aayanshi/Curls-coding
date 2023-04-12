litz = ["s", "u", "n","d", "e","r"," ","a","a", "i","n", "a"]
l = []
s = ""
for i in litz:
    if i == "a" or i == "i" or i == "e" or i == "o" or i == "u":
        s = s + "$"
    else:     
        s = s + i

l.append(s)

print(l)    