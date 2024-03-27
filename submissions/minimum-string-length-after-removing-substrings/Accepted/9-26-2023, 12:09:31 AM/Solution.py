// https://leetcode.com/problems/minimum-string-length-after-removing-substrings

class Solution:
    def minLength(self, s: str) -> int:

        tmp = s.replace("AB","").replace("CD","")

        while len(tmp) != len(s):
            s = tmp
            tmp = tmp.replace("AB","").replace("CD","")  

        return len(tmp)
        

        
        