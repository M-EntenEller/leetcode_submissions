// https://leetcode.com/problems/maximum-number-of-balloons

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        m = {"b":0, "a":0, "l":0, "o":0, "n":0}

        for c in text: 

            if m.get(c) != None: 
                m[c] += 1
            
        res = len(text)

        for key, val in m.items():

            if key == "l" or key == "o":
                val = val // 2

            if val < res: 
                res = val    

        return res







            
             
        