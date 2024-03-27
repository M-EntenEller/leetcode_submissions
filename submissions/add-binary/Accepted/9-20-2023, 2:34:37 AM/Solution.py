// https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        rest = 0 
        res = []
        na = len(a)
        nb = len(b)

        if na < nb:
            a = "0" * abs(na-nb) + a
        elif nb < na:
            b = "0" * abs(na-nb) + b

        i = 0
        for i in range(max(na, nb) - 1, -1, -1):

            tmp = int(a[i]) + int(b[i]) + rest
            res.append(tmp % 2)
            rest = tmp // 2

        if rest > 0:
            res.append(1)

        res.reverse()
        res = [str(x) for x in res]
        return "".join(res)       

                

        
        