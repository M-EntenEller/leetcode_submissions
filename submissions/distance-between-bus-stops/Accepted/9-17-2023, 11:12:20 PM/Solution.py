// https://leetcode.com/problems/distance-between-bus-stops

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        if not start < destination:
            tmp = start
            start = destination
            destination = tmp

 
        return min(
            sum(distance[start: destination]), 
            sum(distance[0: start]) + sum(distance) - sum(distance[0: destination])
            )

