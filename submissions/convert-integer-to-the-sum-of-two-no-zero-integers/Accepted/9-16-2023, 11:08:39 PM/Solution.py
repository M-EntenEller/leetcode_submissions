// https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        def check_num(num):
            s = str(num)

            for c in s:

                if c == "0":
                    return False

            return True

        i = 1
        j = n-1

        while i<=j:

            if i == j:
                return [i,i]
            elif check_num(i) and check_num(j):
                return [i,j]

            i += 1
            j -= 1
        