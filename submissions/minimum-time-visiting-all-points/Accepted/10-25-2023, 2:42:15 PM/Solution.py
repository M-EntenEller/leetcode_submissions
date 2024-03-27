// https://leetcode.com/problems/minimum-time-visiting-all-points

class Solution:

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        res = 0
        tmp = points[0]

        for i in range(1, len(points)):

            p = points[i]

            delta_x = abs(p[0] - tmp[0])
            delta_y = abs(p[1] - tmp[1])
            res += max(delta_x, delta_y)

            tmp = p

        return res
            

        