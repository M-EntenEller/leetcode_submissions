// https://leetcode.com/problems/minimum-time-visiting-all-points

class Solution:

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        res = 0
        tmp = points[0]

        for p in points:

            delta_x = p[0] - tmp[0]
            delta_y = p[1] - tmp[1]

            cost = 0

            while delta_x != 0 or delta_y != 0:

                if delta_x != 0:
                    step = 1 if delta_x > 0 else -1
                    tmp[0] += step
                    delta_x += (-1) * step  
                    cost += 1

                if delta_y != 0:
                    step = 1 if delta_y > 0 else -1
                    tmp[1] += step
                    delta_y += (-1) * step
                    cost += 1

                res += 1 if cost > 0 else 0

        return res
            

        