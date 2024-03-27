// https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        def check_num(num):
            s = str(num)

            for c in s:

                if c == "0":
                    return False

            return True

        i = 0
        while i <= n//2:

            if check_num(i) and check_num(n-i):
                return [i, n-i] 

            i += 1

        
        