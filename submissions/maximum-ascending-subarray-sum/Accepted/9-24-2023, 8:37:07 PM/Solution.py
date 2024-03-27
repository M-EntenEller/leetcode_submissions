// https://leetcode.com/problems/maximum-ascending-subarray-sum

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        l = 0
        r = 1
        res = nums[0]
        tmp = res

        while r < len(nums):

            if nums[r] > nums[r-1]:
                tmp += nums[r]
            else:
                l = r
                if tmp > res:
                    res = tmp
                tmp = nums[l]
            r += 1

        return max(res, tmp)
        