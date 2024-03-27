// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for c in s:

            if c == "(":
                stack.append(")")
            elif c == "[":
                stack.append("]")
            elif c == "{":
                stack.append("}")
            elif not (stack and stack.pop() == c):
                return False
            
        if stack:
            return False
        
        return True


                
