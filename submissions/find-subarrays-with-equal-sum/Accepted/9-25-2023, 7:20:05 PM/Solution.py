// https://leetcode.com/problems/find-subarrays-with-equal-sum

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        
        _set = set()

        for i in range(len(nums)-1):

            _sum = nums[i] + nums[i+1]

            if _sum in _set:
                return True
            else: 
                _set.add(_sum)

        return False
                
        