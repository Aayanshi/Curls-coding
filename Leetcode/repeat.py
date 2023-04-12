'''387. First Unique Character in a String
Easy
7.2K
243
Companies
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1'''


'''
c = 0
pt = 0
for i in range(len(s)):c v
    '''


s = "loveleetcode"
def repeat(s):
    d = {} 
    n = len(s)-1
    st = 0
    ed = 0
    c = 0

    while ed <= n:
        if s[ed] not in d:
            hash[s[ed]] = ed
            ed = ed + 1
        else :
            while s[ed] in d:
                c = ed
                st = st + 1
    return c , d          

rev = repeat(s)
print(rev)


