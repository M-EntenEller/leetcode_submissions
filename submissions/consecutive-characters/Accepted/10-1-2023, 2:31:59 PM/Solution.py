// https://leetcode.com/problems/consecutive-characters

class Solution:
    def maxPower(self, s: str) -> int:

        state = s[0]
        res = 0
        tmp = 1

        for i in range(1, len(s)):

            if s[i] == state:
                tmp += 1
            else: 
                if tmp > res:
                    res = tmp
                state = s[i]
                tmp = 1

        return max(tmp, res)

            

            


        
        