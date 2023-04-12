'''1047. Remove All Adjacent Duplicates In String'''
s = "abbaca"
stack = []
for i in range(len(s)):
    stack.append(s[0])
    for j in range(i+1,len(s)):

        
        if s[j] != stack[-1]:
           stack.append(s[i])
        else:
            stack.pop() 
            
print(stack)



'''if i == stack[-1]:
    stack.pop()
    '''
    
    




'''
s = "abbaca"
for i in s:
    if stack and i == stack[-1] :
        stack.pop()
    else:
        stack.append(i)    
        

print(stack)            '''

'''class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        stack.append(s[0])
        for i in range(1,len(s)):
            if len(stack)==0:
                stack.append(s[i])
            elif stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        inu = ""
        for i in stack:
            inu = inu+i
        return inu'''

##fuckkkkkkkkkkkkkkkoffffffffffffffffffffffffffstackkkkkkkkkkkk        