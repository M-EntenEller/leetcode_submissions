// https://leetcode.com/problems/largest-substring-between-two-equal-characters

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    
        res = -1
        m = {}

        for i, c in enumerate(s):
            
            if c in m:
                m[c].append(i)
            else:
                m[c] = [i]

        for key, value in m.items():

            if len(value) > 1:
                delta = value[-1] - value[0] - 1
                if delta > res:
                    res = delta

        return res

            