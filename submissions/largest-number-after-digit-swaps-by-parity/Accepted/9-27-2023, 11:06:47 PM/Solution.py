// https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity

class Solution:
    def largestInteger(self, num: int) -> int:

        digits = [int(d) for d in str(num)]
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

        return int("".join([str(d) for d in digits]))



            


         


        