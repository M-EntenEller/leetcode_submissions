// https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums.sort()
        last = -1 

        for num in nums:

            if num - last != 1:
                return last + 1

            last = num
        
        return last + 1
            
        
        
        