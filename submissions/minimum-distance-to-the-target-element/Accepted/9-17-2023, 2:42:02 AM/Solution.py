// https://leetcode.com/problems/minimum-distance-to-the-target-element

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:

        res = 10**4 + 1

        for idx, num in enumerate(nums): 

            if num == target:
                if abs(idx - start) < res:
                    res = abs(idx - start)

        return res
        