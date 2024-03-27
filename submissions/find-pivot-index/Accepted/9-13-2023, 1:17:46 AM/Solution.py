// https://leetcode.com/problems/find-pivot-index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        csum = sum(nums)
        ls = 0

        for idx, num in enumerate(nums):

            tmp = ls + num 

            if ls == csum - tmp:
                return idx

            ls = tmp

        return -1
                  