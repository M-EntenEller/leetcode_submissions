// https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0: 
            return 0
        
        if n == 1 or n == 2:
            return 1

        t_3 = 0
        t_2 = 1
        t_1 = 1

        tmp = None

        i = 3
        while i <= n:
            tmp = t_3 + t_2 + t_1
            i += 1
            t_3 = t_2
            t_2 = t_1
            t_1 = tmp

        return tmp


        
            
             
        