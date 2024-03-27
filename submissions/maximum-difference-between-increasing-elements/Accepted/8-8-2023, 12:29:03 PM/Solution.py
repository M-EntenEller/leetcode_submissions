// https://leetcode.com/problems/maximum-difference-between-increasing-elements

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        md = -1

        n = len(nums)

        for i in range(n-1):
            for j in range(i+1,n):
                diff = nums[j] - nums[i] 
                if diff > md and diff > 0:
                    md = diff 

        return md        

        