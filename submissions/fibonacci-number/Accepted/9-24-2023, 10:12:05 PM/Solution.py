// https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1

        res = 0    
        f2 = 0
        f1 = 1

        for i in range(2, n+1):

            res = f1 + f2
            f2 = f1
            f1 = res

        return res 


            
         