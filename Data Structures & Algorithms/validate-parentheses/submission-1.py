class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        clstoOpen={"]":"[",")":"(","}":"{"}
        for c in s:
                if c in clstoOpen:
                        if stack and stack[-1] == clstoOpen[c]:
                                stack.pop()
                        else:
                                return False        
                else:
                        stack.append(c)
        return True if not stack else False                
