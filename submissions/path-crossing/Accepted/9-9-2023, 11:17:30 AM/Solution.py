// https://leetcode.com/problems/path-crossing

class Solution:
    def isPathCrossing(self, path: str) -> bool:

        visited_points = set()
        active_point = (0,0)
        visited_points.add(active_point)

        def move(ap, c):
            if c == "N":
                return (ap[0], ap[1] + 1)
            if c == "S":
                return (ap[0], ap[1] - 1)
            if c == "E":
                return (ap[0] + 1, ap[1])
            if c == "W":
                return (ap[0] - 1, ap[1])

        for c in path:
            active_point = move(active_point, c)
            if active_point in visited_points:
                return True
            visited_points.add(active_point)

        return False




        