// https://leetcode.com/problems/height-checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        res = 0
        bound_count = [0 for _ in range(100)]

        for x in heights:
            
            bound_count[x] += 1

        j = 0

        for i in range(100):
            
            count = bound_count[i]

            while count > 0:

                if heights[j] != i:
                    res += 1

                j += 1
                count -= 1

        return res


                

        


        

        
        

            
        