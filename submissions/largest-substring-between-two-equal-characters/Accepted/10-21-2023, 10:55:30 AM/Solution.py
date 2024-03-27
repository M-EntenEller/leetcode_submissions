// https://leetcode.com/problems/largest-substring-between-two-equal-characters

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    
        res = -1
        m = {}

        for i, c in enumerate(s):
            
            if c in m:
                res = max(i - m.get(c) - 1, res)
            else:
                m[c] = i

        return res

        

            