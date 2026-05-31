class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        stack=[]
        for i in range(n):
            if s[i]=='{' or s[i]=='(' or s[i]=='[':
                stack.append(s[i])
            elif stack and s[i]=='}' and stack[-1]=='{':
                stack.pop()
            elif stack and s[i]==')' and stack[-1]=='(':
                stack.pop()
            elif stack and s[i]==']' and stack[-1]=='[':
                stack.pop()
            else:
                return False
        return len(stack)==0
            
            
        