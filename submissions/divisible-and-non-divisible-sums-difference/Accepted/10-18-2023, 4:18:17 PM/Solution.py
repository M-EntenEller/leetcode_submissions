// https://leetcode.com/problems/divisible-and-non-divisible-sums-difference

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:

        num2 = 0
        tmp = m

        while tmp <= n:
            num2 += tmp
            tmp += m
        
        return int(n*(n+1)/2) - (num2 + num2)

            

        