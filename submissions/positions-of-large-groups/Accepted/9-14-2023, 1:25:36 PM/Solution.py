// https://leetcode.com/problems/positions-of-large-groups

class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """

        i = j = -1
        last = None
        res = []

        for idx, c in enumerate(s + " "):
            
            if c == last:
                j = idx
            else: 
                if (j - i) >= 2:
                    res.append([i,j])
                i = j = idx

            last = c

        return res
            
            
        