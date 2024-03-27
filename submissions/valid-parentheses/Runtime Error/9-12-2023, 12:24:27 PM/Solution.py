// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for c in s:
            
            if c == "{" or c=="[" or c=="(":
                stack.append(c)
                continue

            popped = stack.pop()

            if c == "}":
                if popped == "{":
                    continue
            elif c == "]":
                if popped == "[":
                    continue
            elif c == ")":
                if popped == "(":
                    continue
            
            return False

        return not stack
