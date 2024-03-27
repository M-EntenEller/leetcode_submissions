// https://leetcode.com/problems/number-of-arithmetic-triplets

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:

        res = 0
        n = len(nums)

        for i in range(n):

            for j in range(i+1, n):

                if not nums[j] - nums[i] == diff:
                    continue 

                for k in range(j+1, n):

                    if nums[k] - nums[j] == diff:
                        res += 1

        return res
                    
        