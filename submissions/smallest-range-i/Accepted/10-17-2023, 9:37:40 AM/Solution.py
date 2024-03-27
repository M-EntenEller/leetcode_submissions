// https://leetcode.com/problems/smallest-range-i

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:

        m = min(nums)
        M = max(nums)
        c = (M+m) // 2 

        for i in range(len(nums)):
            
            if nums[i] < c:
                nums[i] += min(k, c-nums[i])
            elif nums[i] > c:
                nums[i] -= min(k, nums[i]-c)

        return max(nums) - min(nums) 

            
        
        