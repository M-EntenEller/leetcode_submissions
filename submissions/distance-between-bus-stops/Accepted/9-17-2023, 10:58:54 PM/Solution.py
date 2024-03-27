// https://leetcode.com/problems/distance-between-bus-stops

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        n = len(distance)
        clockwize = 0 
        i = start

        while i != destination:
            
            clockwize += distance[i]
            i = (i + 1) % n
        
        
        cc = 0
        j = start

        while j != destination: 

            cc += distance[ (j - 1 + n) % n]
            j = (j - 1 + n) % n

        return min(cc, clockwize)

