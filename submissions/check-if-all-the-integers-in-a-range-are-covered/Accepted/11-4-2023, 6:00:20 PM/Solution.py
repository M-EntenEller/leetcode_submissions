// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        covered = set()
        target_count = right-left +1
        i = 0
        nums = ranges

        while i<len(nums) and len(covered) < target_count:

            for j in range(left, right+1):

                if nums[i][0] <= j and j<= nums[i][1]:
                    covered.add(j)

            i += 1
        
        return len(covered) == target_count
        