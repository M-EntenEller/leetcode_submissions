// https://leetcode.com/problems/calculate-money-in-leetcode-bank

class Solution:
    def totalMoney(self, n: int) -> int:
        
        res = 0
        week = 1
        day = 1
        adder = 0

        for i in range(1, n+1):

            adder += 1
            res += adder

            if i % 7 == 0:
                adder = i // 7 

        return res


        