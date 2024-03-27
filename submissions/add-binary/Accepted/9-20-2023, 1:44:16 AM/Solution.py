// https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        def bi(s):
            agg = 0
            for idx, c in enumerate(s):
                agg += int(c) * 2**(len(s) - 1 - idx)

            return agg

        l = []
        tmp = bi(a) + bi(b)

        if tmp == 0:
            l.append("0")

        while tmp > 0:
            l.append(str(tmp % 2))
            tmp = tmp // 2

        l.reverse()
        return "".join(l) 
        
        