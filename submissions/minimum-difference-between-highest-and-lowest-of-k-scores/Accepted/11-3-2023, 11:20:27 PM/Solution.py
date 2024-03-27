// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort()
        res = nums[k-1] - nums[0]

        for i in range(1, len(nums) - k + 1):
            
            diff = nums[i + k - 1] - nums[i]

            if diff < res:
                res = diff

        return res
            
        