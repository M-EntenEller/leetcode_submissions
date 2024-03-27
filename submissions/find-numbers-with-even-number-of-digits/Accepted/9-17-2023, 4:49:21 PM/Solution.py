// https://leetcode.com/problems/find-numbers-with-even-number-of-digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        import math
        res = 0

        for num in nums:

            e = 0.00001
            gp = math.log(num, 10)
            digits = int(gp + e) + 1

            print(gp, digits)
            
            if digits % 2 == 0:
                res += 1
    
        return res