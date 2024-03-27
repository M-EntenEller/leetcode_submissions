// https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        def check_num(num):
            s = str(num)

            for c in s:

                if c == "0":
                    return False

            return True

        
        for i in range(1, n//2 + 1):

            if check_num(i) and check_num(n-i):
                return [i, n-i] 

        
        