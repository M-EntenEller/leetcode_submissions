// https://leetcode.com/problems/total-distance-traveled

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:

        used = 0 

        while mainTank > 0:

            mainTank -= 1
            used += 1
            if used % 5 == 0 and additionalTank > 0: 
                additionalTank -= 1
                mainTank += 1 

        return used * 10
            
            
        