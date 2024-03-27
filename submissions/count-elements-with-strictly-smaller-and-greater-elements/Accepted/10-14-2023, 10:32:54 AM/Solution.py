// https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements

class Solution:
    def countElements(self, nums: List[int]) -> int:

        _min = min(nums)
        _max = max(nums)
        res = 0
            
        for num in nums: 

            if num > _min and num < _max:
                    res += 1

        return res

                
        