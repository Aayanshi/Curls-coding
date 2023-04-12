'''Count the vowels in a string
Create a function in Python that accepts a single word and returns the number of vowels in that word.
In this function,
only a, e, i, o, and u will be counted as vowels — not y.'''


def vowel(s):
    count = 0
    ie= "aeiouAEIOU"
    for i in range(len(s)):
      if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u" :
           count = count + 1
    
    
    #for i in s:
    #   if i in ie:
    #       count = count+1

    
    #d = {}
    #for i in range(len(s)):
    #    d[s[i]] = i
        
    
    return count


s = "aaina"
k = vowel(s)
print(k)
 
