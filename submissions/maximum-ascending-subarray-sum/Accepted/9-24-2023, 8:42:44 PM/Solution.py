// https://leetcode.com/problems/maximum-ascending-subarray-sum

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        res = nums[0]
        tmp = res

        for i in range(1, len(nums)):

            if nums[i] > nums[i-1]:
                tmp += nums[i]
            else:
                res = max(res, tmp)
                tmp = nums[i]
        
        return max(res, tmp)
        