// https://leetcode.com/problems/maximum-ascending-subarray-sum

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        r = 1
        res = nums[0]
        tmp = res

        while r < len(nums):

            if nums[r] > nums[r-1]:
                tmp += nums[r]
            else:
                if tmp > res:
                    res = tmp
                tmp = nums[r]
            r += 1

        return max(res, tmp)
        