// https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        def man_dist(p):    
            return abs(p[0]-x) + abs(p[1]-y)

        res = -1
        _min = 10**5

        for i, point in enumerate(points): 
            
            if x == point[0] or y == point[1]:
                md = man_dist(point)
                if md < _min:
                    res = i
                    _min = md

        return res

        
        
        