// https://leetcode.com/problems/maximum-average-subarray-i

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        n = len(nums)

        ms = 0
        for i in range(k):
            ms += nums[i]

        s = ms

        for j in range(k, n):
            s = s + nums[j] - nums[j-k]
            if s > ms:
                ms = s
                   
        return ms / k
              