// https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits

class Solution:
    def minimumSum(self, num: int) -> int:

        digits = [0] * 4

        for i in range(3, -1, -1):
            
            digits[i] = num % 10
            num = num // 10

        digits.sort()

        return digits[0] * 10 + digits[2] + digits[1] * 10 + digits[3] 


        

                        
        