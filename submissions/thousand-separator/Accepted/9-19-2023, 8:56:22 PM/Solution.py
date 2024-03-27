// https://leetcode.com/problems/thousand-separator

class Solution:
    def thousandSeparator(self, n: int) -> str:

        res = []
        s = str(n)
        count = 0
        i = len(s) - 1

        while i >= 0:

            res.append(s[i])
            count += 1
            if count == 3 and i > 0:
                res.append(".")
                count = 0
            i -= 1

        res.reverse()
        return "".join(res)
            
            
            

            
            

            
        