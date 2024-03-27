// https://leetcode.com/problems/smallest-range-i

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:

        im = nums.index(min(nums))
        iM = nums.index(max(nums))
        c = (nums[iM] + nums[im]) // 2 

        return (nums[iM] - min(k, nums[iM]-c)) - (nums[im] + min(k, c-nums[im]))

            
        
        