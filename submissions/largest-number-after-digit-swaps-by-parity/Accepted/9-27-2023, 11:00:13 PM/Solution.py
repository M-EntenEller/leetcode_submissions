// https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity

class Solution:
    def largestInteger(self, num: int) -> int:

        def int_to_digits(num):
            digits = []
            while num > 0:
                digits.append(num % 10)
                num = num // 10
            
            digits.reverse()
            return digits

        def digits_to_int(digits):
            res = 0
            n = len(digits)
            
            i=0
            while i < n:

                res += digits[i] * 10**(n-1-i) 
                i += 1
        
            return res
                

        digits = int_to_digits(num)
        even = []
        odd = []

        for i, digit in enumerate(digits): 

            if digit % 2 == 0:
                even.append(digit)
            else:
                odd.append(digit)

        even.sort()
        odd.sort()
        
        for i, d in enumerate(digits):

            if d % 2 == 0:
                digits[i] = even.pop() 
            else:
                digits[i] = odd.pop()

        return digits_to_int(digits)



            


         


        