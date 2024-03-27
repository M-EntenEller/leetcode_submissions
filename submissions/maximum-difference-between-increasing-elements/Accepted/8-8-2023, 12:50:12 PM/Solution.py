// https://leetcode.com/problems/maximum-difference-between-increasing-elements

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        md = -1
        rolling_min = nums[0] 
        n = len(nums)

        for i in range(1, n):

            diff = nums[i] - rolling_min
            
            if diff > 0 and diff > md:
                md = diff

            rolling_min = min(rolling_min, nums[i])

        return md
        

        