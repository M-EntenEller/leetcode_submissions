// https://leetcode.com/problems/count-special-quadruplets

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0

        for i in range(n - 3):

            for j in range(i + 1, n - 2):

                for k in range(j +1, n-1):

                    for l in range(k+1, n):

                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            res += 1

        return res