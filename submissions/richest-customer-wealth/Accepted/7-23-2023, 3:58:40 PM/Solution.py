// https://leetcode.com/problems/richest-customer-wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        max = 0
        
        for row in accounts: 
            
            sum = 0

            for x in row: 
                sum += x

            if sum > max:
                max = sum

        return max