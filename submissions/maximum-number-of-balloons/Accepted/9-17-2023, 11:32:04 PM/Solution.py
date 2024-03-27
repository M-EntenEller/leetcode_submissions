// https://leetcode.com/problems/maximum-number-of-balloons

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        m = [0] * 26
        base = ord("a")


        for c in text:
            
            m[ord(c)-base] += 1

        char_freq = [("b",1), ("a",1), ("l",2), ("o",2), ("n",1)]
        res = len(text)

        for c, freq in char_freq:

            possible = m[ord(c)-base] // freq

            if possible < res:
                res = possible

        return res





            
             
        