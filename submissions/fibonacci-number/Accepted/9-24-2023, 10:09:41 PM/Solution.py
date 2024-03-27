// https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1
        
        res = 0
        b2 = 0
        b1 = 1

        i=2
        while i<=n:

            res = b1 + b2
            b2 = b1
            b1 = res
            i += 1

        return res


            
         