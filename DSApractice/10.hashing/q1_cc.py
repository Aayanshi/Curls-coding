'''Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.'''



def substring(s):
    hashtable = dict()
    st = 0
    ed = 0
    maxlength = 0
    n = len(s)-1

    while ed <= n :
        if s[ed] not in hashtable:
            hashtable[s[ed]] = ed
            cl = ed-st +1
            maxlength = max(maxlength,cl)
            ed = ed + 1 

        else :
            while s[ed] in hashtable :
                hashtable.pop(s[st])
                st = st + 1
            hashtable[s[ed]] = ed 
            ed = ed + 1
    return maxlength    

s = [1,1,1,1]
res = substring(s)
print(res)


    