// https://leetcode.com/problems/longest-nice-substring

class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        _s = set(s)

        if not s:
            return ""

        for i, c in enumerate(s):

            if c.swapcase() not in _s:
                sl = self.longestNiceSubstring(s[0:i])
                su = self.longestNiceSubstring(s[i+1:])
                return max(sl, su, key=lambda x: len(x))
        
        return s








            
        