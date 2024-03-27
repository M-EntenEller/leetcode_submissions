// https://leetcode.com/problems/find-numbers-with-even-number-of-digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        res = 0

        for num in nums:

            if len(str(num)) % 2 == 0:
                res += 1

        return res