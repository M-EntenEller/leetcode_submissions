// https://leetcode.com/problems/number-of-arithmetic-triplets

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:

        res = 0
        n = len(nums)
        seen = set()

        i = n-1
        while i >= 0:

            if (nums[i] + diff) in seen and (nums[i] + 2*diff) in seen:  
                res += 1

            seen.add(nums[i])
            i -= 1    

        return res
            
            
            

        
                    
        