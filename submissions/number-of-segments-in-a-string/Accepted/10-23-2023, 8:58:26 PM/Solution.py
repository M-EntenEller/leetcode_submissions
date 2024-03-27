// https://leetcode.com/problems/number-of-segments-in-a-string

class Solution:
    def countSegments(self, s: str) -> int:

        res = 0
        state = False

        for c in s:

            if c == " ":
                state = False
            else:
                if not state:
                    res += 1
                    state = True
                    
        return res
                 

            


        