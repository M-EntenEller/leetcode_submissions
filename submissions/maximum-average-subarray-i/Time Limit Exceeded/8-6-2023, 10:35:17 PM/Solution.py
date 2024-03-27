// https://leetcode.com/problems/maximum-average-subarray-i

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        ma = -10**4
        n = len(nums)

        for i in range(n-(k-1)):
            sum = 0
            
            for j in range(k):
                sum += nums[i+j]

            avg = sum/k

            if avg > ma: 
                ma = avg    

        return ma           