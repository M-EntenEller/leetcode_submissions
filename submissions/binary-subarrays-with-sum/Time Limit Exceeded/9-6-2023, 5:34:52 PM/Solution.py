// https://leetcode.com/problems/binary-subarrays-with-sum

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        n = len(nums)    
        s = 0
        count = 0

        while s < n:
            e = s + 1
            while e <= n:
                _sum = sum(nums[s:e])
                if _sum == goal:
                     count += 1
                elif _sum > goal:
                    break
                e += 1
                
            s += 1

        return count

        
            
    