// https://leetcode.com/problems/longest-nice-substring

class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        def is_nice(s):
            _set = set(s)

            for x in _set:

                inverse = x.lower() if x.isupper() else x.upper()
                if not inverse in _set:
                    return False

            return True 

        res = ""

        for i in range(len(s)):

            for j in range(i+1, len(s) + 1):
               
                if is_nice(s[i:j]) and len(s[i:j]) > len(res):
                    res = s[i:j]

        return res
                

            
        