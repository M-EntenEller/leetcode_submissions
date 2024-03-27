// https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        s = 0

        for num in nums: 
            
            s += num 

        return int((n * (n + 1)) / 2 - s)
        
        
        