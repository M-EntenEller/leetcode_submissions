// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        covered = set()

        for _range in ranges:

            lower = max(_range[0], left)
            upper = min(_range[1], right)

            for x in range(lower, upper+1):
               covered.add(x)

            if len(covered) == right-left+1:
                return True

        return False

