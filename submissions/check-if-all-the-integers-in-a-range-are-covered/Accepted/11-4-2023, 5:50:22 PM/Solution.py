// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        s = set(range(left,right+1))
        covered = set()

        for r in ranges: 

            for x in s:

                if r[0] <= x and x <= r[1]:
                    covered.add(x)
        
        return len(covered) == right-left+1
    
        